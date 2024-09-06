# db_session.py
from contextlib import contextmanager

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, event
from utils.logging_config import setup_logging
from utils.db_engine import wps_engine, create_db_engine, serializable_wps_engine
import models as models

logger = setup_logging(__name__)


# def get_binds():
#     return {
#         models.EventTable: event_engine,
#     }


# Create sessionmaker for the MySQL database
mysql_session = sessionmaker(autocommit=False, autoflush=False, bind=wps_engine)
# mysql_session.configure(binds=get_binds())


serializable_session = sessionmaker(autocommit=False, autoflush=False, bind=serializable_wps_engine)


# Define the event listener
def after_commit_listener(session):
    logger.critical("============================================================= Custom commit message: Transaction committed successfully")


# Attach the after_commit_listener to the sessionmaker
event.listen(mysql_session, 'after_commit', after_commit_listener)


def get_db():
    """
    Context manager for handling WPS database sessions.
    """
    wps_db = mysql_session()
    try:
        yield wps_db
    finally:
        wps_db.close()


def get_serializable_db():
    """
    Context manager for handling WPS database sessions with SERIALIZABLE isolation level.
    """
    serializable_db = serializable_session()
    try:
        yield serializable_db
    finally:
        serializable_db.close()