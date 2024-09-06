# Python allows you to catch specific types of errors, but what if you want to be able to catch any type
# of error in an `except` block for debugging and logging purposes? Catching any type of error requires a 
# bit more work. This module can be used to catch any type of error in a plain `except` block. For example:
"""
@app.get("/api/get-todos")
async def get_todos(request: Request):
    try:
        response = { "todos": ["Eat", "Sleep", "Debug Code"] }
        return response
    except:
        logging.error(format_error("main.py"))
"""

# If you want to catch a specific type of error, then you should catch that error like you normally
# would in Python instead of using this module to catch that specific type of error. For example:
"""
except TypeError:
    logging.error("This is a message for a TypeError exception.")
"""

# The ideas used for formatting errors were found here: https://pythonprogramming.net/headless-error-handling-intermediate-python-tutorial/
# You can catch all errors and error messages with `sys.exc_info()`.

import sys

def format_error(file_name):
    """Formats an error object (no matter what error type) into a formatted string.

    file_name -- The name of the file where this function is being called
    """
    return f"""
    FILE NAME: {file_name}
    LINE NUMBER: {sys.exc_info()[2].tb_lineno}
    ERROR TYPE: {sys.exc_info()[0]}
    ERROR MESSAGE: {sys.exc_info()[1]}"""
