import os
import logging
from dotenv import load_dotenv

override_ip_based_env_file = False
override_ip = ".env.docker"


if os.getenv("DOCKER_ENV") is not None:
    pass
else:

    import socket

    def detect_network():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            network = ip.split('.')[2]

            if override_ip_based_env_file:
                dotenv_path = override_ip
                return dotenv_path
            else:
                if network == '0':
                    dotenv_path = ".env.home"
                    return dotenv_path
                elif int(network) > 0:
                    dotenv_path = ".env.dev.work"
                    return dotenv_path
        finally:
            s.close()

    env_file = detect_network()
    load_dotenv(env_file)


from utils.logging_config import setup_logging

logger = setup_logging(__name__)

logger.info("ENVIRONMENT VARIABLES LOADED")

current_file_path = os.path.abspath(os.path.dirname(__file__))
app_directory = os.path.abspath(os.path.join(current_file_path, os.pardir))
top_level_directory = os.path.abspath(os.path.join(current_file_path, os.pardir, os.pardir))
very_top_level_directory = os.path.abspath(os.path.join(current_file_path, os.pardir, os.pardir, os.pardir))

# # Access the environment variables
ENV_NAME = os.getenv('ENV_NAME')
LOGS_LEVEL = os.getenv('LOGS_LEVEL')
SERVER_IP = str(os.getenv('SERVER_IP'))
DOWNLOAD_FILES = os.getenv("DOWNLOAD_FILES", False)
SKIP_PRINTING = os.getenv("SKIP_PRINTING", False)
CACHE_TTL = int(os.getenv("CACHE_TTL", 3600))
CACHE_SIZE = int(os.getenv("CACHE_SIZE", 1024))

FILE_NAME = os.getenv("workflows.json")
DEFAULT_JSON_CONFIG = os.getenv("DEFAULT_JSON_CONFIG")

# WPS_URI = "mysql+pymysql://root:helloworld@192.168.1.155:15606/wps?charset=utf8"
WPS_URI = "mysql+pymysql://staging:YKc5BUpQ5fqG2Wz@192.168.1.3/wps?charset=utf8"
# os.getenv("WPS_URI")
EVENT_TABLE_URI = os.getenv("EVENT_TABLE_URI")

REDIS_PICKING_LOCK = os.getenv("REDIS_PICKING_LOCK", False)
REDIS_LOCK_TIMEOUT = int(os.getenv("REDIS_LOCK_TIMEOUT", 10))
REDIS_AUTO_EXPIRE = int(os.getenv("REDIS_AUTO_EXPIRE", 10))
REDIS_URL = os.getenv("REDIS_URL")
REDIS_PORT = os.getenv("REDIS_PORT")
# REDIS_DB = int(os.getenv('REDIS_DB'))

LABELS_URL = os.getenv("LABELS_URL")
EXTRA_DOCS_URL = os.getenv("EXTRA_DOCS_URL")
LOCAL_EXTRA_DOCS_FOLDER = os.getenv("LOCAL_EXTRA_DOCS_FOLDER")
LOCAL_LABEL_FOLDER = os.getenv("LOCAL_LABEL_FOLDER")
LOCAL_AUX_LABEL_FOLDER = os.getenv("LOCAL_AUX_LABEL_FOLDER")
LOCAL_ZPL_FOLDER = os.getenv("LOCAL_ZPL_FOLDER")

picking_start_status = "OPEN"
picking_new_status = "NEW"

EFM_ZPL_FOLDER = os.getenv("EFM_LABEL_SERVER")
# EXTRA_DOCS_FOLDER_PATH = os.path.abspath(os.path.join(app_directory, LOCAL_EXTRA_DOCS_FOLDER))
# COURIER_LABEL_FOLDER_PATH = os.path.abspath(os.path.join(app_directory, LOCAL_LABEL_FOLDER))
# AUX_LABELS_FOLDER_PATH = os.path.abspath(os.path.join(app_directory, LOCAL_AUX_LABEL_FOLDER))
# ZPL_LABEL_FOLDER_PATH = os.path.abspath(os.path.join(app_directory, LOCAL_ZPL_FOLDER))

# BATCH_PRINT_SIZE = int(os.getenv('BATCH_PRINT_SIZE'))
PRINTER_NAME = os.getenv("PRINTER_NAME")
CUPS_SERVER = os.environ.get("CUPS_SERVER", None)

# LA_MODA = os.getenv("LA_MODA")
# STATUS_OOS = os.getenv("STATUS_OOS")
# STATUS_OPEN = os.getenv("STATUS_OPEN")
STATUS_NEW = os.getenv("STATUS_NEW")
STATUS_ASSIGNED = os.getenv("STATUS_ASSIGNED")
# STATUS_PICKED = os.getenv("STATUS_PICKED")
# STATUS_CONSOLIDATE = os.getenv("STATUS_CONSOLIDATE")
# DOWNLOAD_FILES = os.getenv("DOWNLOAD_FILES", False)

EVENTS_ACTIVE = os.getenv("EVENTS_ACTIVE", False)

logger.info(f'CURRENT ACTIVE ENV IS: {ENV_NAME}')
logger.info(f'CURRENT LOGS LEVEL IS SET TO LEVEL: {LOGS_LEVEL}')
logger.info(f'SERVER IP: {SERVER_IP}')
logger.debug(f'PRINTING STATUS: {"NOT ACTIVE" if SKIP_PRINTING else "ACTIVE"}')
logger.debug(f'DOWNLOADING STATUS: {"ACTIVE" if DOWNLOAD_FILES else "NOT ACTIVE"}')
logger.critical(f'EVENTS ACTIVE: {"ACTIVE" if EVENTS_ACTIVE else "NOT ACTIVE"}')
logger.info(f'REDIS PICKING QUEUE: {"ACTIVE" if REDIS_PICKING_LOCK else "NOT ACTIVE"}')
logger.info(f'REDIS PICKING QUEUE TIMEOUT: {REDIS_LOCK_TIMEOUT} SECONDS')
logger.info(f'REDIS PICKING QUEUE AUTO EXPIRE: {REDIS_AUTO_EXPIRE} SECONDS')
logger.info(f"CUPS PRINT SERVER IP: {CUPS_SERVER}")


# todo move to the database
non_valid_efm_statuses = ["CANCELLED", "SHIPPED", "REMOVED", "RECALL", "RECALLED", "DS-PROCESS, ""DS-CREATE_"]

PACKED_ORDERS_TIME_DELTA = int(os.getenv("PACKED_ORDERS_TIME_DELTA", 7))

make_commits = False

logger.warning(f"MAKE COMMITS: {make_commits}")