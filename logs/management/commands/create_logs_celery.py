from django.core.management.base import BaseCommand

from logs.tasks import create_logs_delay


class Command(BaseCommand):
    help = 'Pull apache logs from URL and save to DB'

    def handle(self, *args, **options):
        create_logs_delay.delay()
