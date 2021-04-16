import multiprocessing

import os

bind = "0.0.0.0:8000"

workers = os.environ.get('GUNICORN_WORKER_COUNT', multiprocessing.cpu_count() + 1)

threads = workers
user = 'django'
group = 'django'
worker_class = 'sync'
max_requests = 1000
max_requests_jitter = 100
