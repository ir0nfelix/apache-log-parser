LOG_URL = 'http://www.almhuette-raith.at/apache-log/access.log'
LOG_FILE_PATH = 'media'
CHUNK_SIZE = 10240

# TODO details regex group
LOG_COMPILE = r'(?P<ip_address>[\d\.]+)\s+(?P<other_1>\S+)\s+(?P<other_2>\S+)\s+' \
              r'\[(?P<datetime>\S+)\s+.*\]\s+"(?P<method>\S+)\s+(?P<uri>\S+) HTTP.*"\s+' \
              r'(?P<response_code>\d+)\s+(?P<response_size>\S+)\s+\.*\n?'

DATE_AND_HM_FORMAT = '%d-%m-%Y_%H:%M'
DATETIME_LOG_FORMAT = '%d/%b/%Y:%H:%M:%S'

