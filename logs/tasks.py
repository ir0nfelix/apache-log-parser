from infrastructure.celery import app

from infrastructure.utils import LogProcessor


@app.task(ignore_result=True)
def create_logs_delay():
    log_processor = LogProcessor()
    log_processor()
