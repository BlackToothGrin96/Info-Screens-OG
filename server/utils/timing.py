import os
import datetime
from functools import wraps
from utils.logging_config import setup_logging
import inspect

# Set up logger for this module
logger = setup_logging(__name__)


def timing_decorator(func):
    """
    A decorator to measure the execution time of a function.

    This decorator wraps a function and measures the time it takes to execute it.
    The execution time is logged at the info level.

    Args:
        func (function): The function to be timed.

    Returns:
        wrapper (function): The wrapped function.
    """

    @wraps(func)
    async def wrapper(*args, **kwargs):
        # Record the start time
        start_time = datetime.datetime.now()
        # Execute the function and store the result
        result = await func(*args, **kwargs)
        # Record the end time
        end_time = datetime.datetime.now()
        # Calculate the duration in milliseconds
        duration = (end_time - start_time).total_seconds() * 1000
        # Round the duration to 3 decimal places
        duration = round(duration, 3)
        # Get the file name of the function that called the timing decorator
        file_name = os.path.basename(inspect.getfile(func))
        # Log the function name, file name, execution time, and arguments
        logger.info(f"FUNCTION '{func.__name__}' FROM FILE '{file_name}' EXECUTED IN {duration:.3f} MILLISECONDS WITH ARGS {args} AND KWARGS {kwargs}")
        # Return the result of the function
        return result
    return wrapper