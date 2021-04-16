import re
from collections import Generator
from datetime import datetime

import requests
from django.utils.timezone import make_aware

from infrastructure.constants import (
    LOG_FILE_PATH,
    LOG_URL,
    CHUNK_SIZE, LOG_COMPILE,
    DATETIME_LOG_FORMAT,
    DATE_AND_HM_FORMAT
)
from logs.models import LogEntity


class LogProcessor:
    filename = datetime.now().strftime(DATE_AND_HM_FORMAT)

    def __call__(self, *args, **kwargs):
        self.pull_log()
        self.create_logs()

    def create_logs(self) -> None:
        log_obj_list = [
            LogEntity(
                datetime=make_aware(datetime.strptime(kwargs.pop('datetime'), DATETIME_LOG_FORMAT)),
                response_code=int(kwargs.pop('response_code')),
                response_size=(lambda x: int(x) if x.isdigit() else 0)(kwargs.pop('response_size')),
                **kwargs
            ) for kwargs in self._parse_from_file()
        ]
        LogEntity.objects.bulk_create(log_obj_list, batch_size=len(log_obj_list))

    def pull_log(self) -> None:
        response = requests.get(LOG_URL, stream=True)
        with open(f'{LOG_FILE_PATH}/{self.filename}.log', 'wb') as log_file:
            for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                log_file.write(chunk)

    def _parse_from_file(self) -> Generator:
        with open(f'{LOG_FILE_PATH}/{self.filename}.log', 'r') as log_file:
            fields = [
                f.get_attname() for f in LogEntity._meta.fields if f.get_attname() not in ('id', 'details')
            ]
            match_obj_list = [re.compile(LOG_COMPILE).match(line) for line in log_file.readlines()]

            return (
                dict([(f, match.group(f)) for f in fields]) for match in match_obj_list if match is not None
            )
