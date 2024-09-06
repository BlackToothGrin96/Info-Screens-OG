# db_engine.py

from urllib.parse import urlparse
from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool
from utils.logging_config import setup_logging
from __init__ import WPS_URI, EVENT_TABLE_URI

logger = setup_logging(__name__)

def create_db_engine(uri, engine_name, isolation_level=None):
    try:
        # Create a SQLAlchemy engine with an optional isolation level
        engine = create_engine(uri, echo=False, poolclass=NullPool, isolation_level=isolation_level)
        logger.debug(f'SQLALCHEMY {engine_name} ENGINE CREATED SUCCESSFULLY with isolation level {isolation_level}')
        return engine
    except Exception as e:
        raise ConnectionError(f'PROBLEM CREATING {engine_name} ENGINE: {str(e)}')


wps_uri_parsed = urlparse(WPS_URI)
event_table_uri_parsed = urlparse(EVENT_TABLE_URI)

wps_ip = wps_uri_parsed.hostname
event_table_ip = event_table_uri_parsed.hostname

wps_port = wps_uri_parsed.port
event_table_port = event_table_uri_parsed.port

logger.info(f"WPS IP: {wps_ip}, Port: {wps_port}")
logger.info(f"Event Table IP: {event_table_ip}, Port: {event_table_port}")

# Create engines
wps_engine = create_db_engine(WPS_URI, "WPS")
# event_engine = create_db_engine(EVENT_TABLE_URI, "EVENT")
# Create a serializable engine
serializable_wps_engine = create_db_engine(WPS_URI, "WPS", isolation_level='SERIALIZABLE')