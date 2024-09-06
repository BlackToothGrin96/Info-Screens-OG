import os
import logging


class ColoredFormatter(logging.Formatter):
    """
    A custom logging formatter that adds color to log messages based on their level.

    Attributes:
        WHITE (str): ANSI escape code for white color.
        LIGHT_BLUE (str): ANSI escape code for light blue color.
        GREEN (str): ANSI escape code for green color.
        YELLOW (str): ANSI escape code for yellow color.
        MAGENTA (str): ANSI escape code for magenta color.
        RED (str): ANSI escape code for red color.
        RESET (str): ANSI escape code to reset color.
    """
    WHITE = "\033[97m"
    LIGHT_BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    MAGENTA = "\033[35m"
    RED = "\033[91m"
    RESET = "\033[0m"

    def format(self, record):
        """
        Formats a log record with color based on its level.

        Args:
            record (logging.LogRecord): The log record to format.

        Returns:
            str: The formatted log record.
        """
        levelname = record.levelname
        message = record.msg

        time = self.WHITE + self.formatTime(record, "%Y-%m-%d %H:%M:%S.%f")[:-2] + self.RESET

        if record.levelno == logging.DEBUG:
            levelname = f"{self.LIGHT_BLUE}{levelname}{self.RESET}"
            message = f"{self.LIGHT_BLUE}{message}{self.RESET}"

        elif record.levelno == logging.INFO:
            levelname = f"{self.GREEN}{levelname}{self.RESET}"
            message = f"{self.WHITE}{message}{self.RESET}"

        elif record.levelno == logging.WARNING:
            levelname = f"{self.YELLOW}{levelname}{self.RESET}"
            message = f"{self.YELLOW}{message}{self.RESET}"

        elif record.levelno == logging.ERROR:
            levelname = f"{self.RED}{levelname}{self.RESET}"
            message = f"{self.RED}{message}{self.RESET}"

        elif record.levelno == logging.CRITICAL:
            levelname = f"{self.MAGENTA}{levelname}{self.RESET}"
            message = f"{self.MAGENTA}\033[7m{message}{self.RESET}"

        record.levelname = levelname
        record.msg = message
        record.asctime = time  # Set formatted time
        return super().format(record)


def get_log_level(level: str) -> int or ValueError:
    """
    Converts a log level string to its corresponding integer value.

    Args:
        level (str): The log level string.

    Returns:
        int: The corresponding log level integer.
    """
    match level:
        case 'DEBUG':
            return 10
        case 'INFO':
            return 20
        case 'WARNING':
            return 30
        case 'ERROR':
            return 40
        case 'CRITICAL':
            return 50
        case _other:
            return 10


logger_configured = False


def setup_logging(name: str):
    """
    Sets up a logger with a custom colored formatter.

    This function sets up a logger with a custom colored formatter and a stream handler.
    The logger is configured to log messages from the "PIL.PngImagePlugin" module at the WARNING level or higher.
    The log level is determined by the 'LOGS_LEVEL' environment variable.

    Args:
        name (str): The name of the logger.

    Returns:
        logging.Logger: The configured logger.
    """
    global logger_configured
    if not logger_configured:
        log_format = "%(asctime)-10s %(levelname)20s: %(lineno)4d: %(name)-55s - %(message)s"
        # log_format = "%(asctime)-10s %(levelname)20s: %(lineno)4d: %(name)-30s - %(message)s"

        formatter = ColoredFormatter(log_format)

        handler = logging.StreamHandler()
        handler.setFormatter(formatter)

        logging.getLogger("PIL.PngImagePlugin").setLevel(logging.WARNING)
        custom_logger = logging.getLogger()
        uvicorn_access = logging.getLogger("uvicorn.access")
        uvicorn_access.handlers = [handler]
        uvicorn_logger = logging.getLogger("uvicorn")
        uvicorn_logger.handlers = [handler]
        custom_logger.addHandler(handler)
        logging.getLogger("pdfminer").setLevel(logging.CRITICAL)
        logging.getLogger("urllib3").setLevel(logging.CRITICAL)

        logging_level = get_log_level(os.getenv('LOGS_LEVEL'))

        custom_logger.setLevel(logging_level)

        logger_configured = True
    return logging.getLogger(name)