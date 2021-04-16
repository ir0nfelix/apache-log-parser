from django.core.management.base import BaseCommand

from infrastructure.utils import LogProcessor


class Command(BaseCommand):
    help = 'Pull apache logs from URL and save to DB'

    def handle(self, *args, **options):
        log_processor = LogProcessor()
        log_processor()
