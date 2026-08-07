import inspect
import logging
import os
from datetime import datetime
from pathlib import Path


def _get_log_base_name():
    # Prefer the actual pytest test module and function names when available.
    for frame_info in inspect.stack():
        path = Path(frame_info.filename)
        stem = path.stem

        if path.suffix == ".py":
            if frame_info.function and frame_info.function.startswith("test_"):
                return f"{frame_info.function}_{stem}"

            if stem.startswith("test_") or stem.endswith("_test"):
                if frame_info.function and frame_info.function != "<module>":
                    return f"{frame_info.function}_{stem}"
                return stem

    # Prefer the calling function or module name next.
    caller = inspect.stack()[1]
    if caller.function and caller.function != "<module>":
        return caller.function

    module = inspect.getmodule(caller.frame)
    if module and getattr(module, "__file__", None):
        return Path(module.__file__).stem

    return "default"


def customLogger(loglevel):
    logger_name = _get_log_base_name()
    logger = logging.getLogger(logger_name)

    # Set the logging level based on the provided loglevel argument
    if isinstance(loglevel, str):
        loglevel = loglevel.upper()
        level_map = {
            "DEBUG": logging.DEBUG,
            "INFO": logging.INFO,
            "WARNING": logging.WARNING,
            "ERROR": logging.ERROR,
            "CRITICAL": logging.CRITICAL,
        }

        if loglevel not in level_map:
            raise ValueError("Invalid log level: {}".format(loglevel))

        numeric_level = level_map[loglevel]
    elif isinstance(loglevel, int):
        numeric_level = loglevel
    else:
        raise ValueError("Invalid log level: {}".format(loglevel))

    logger.setLevel(numeric_level)

    # Create a console handler to output logs to the console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(numeric_level)

    # Create a formatter for the log messages
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)

    # Create a file handler to save logs under a logs folder at the AutomationFramework package root
    project_root = Path(__file__).resolve().parents[1]
    logs_dir = project_root / "logs"
    logs_dir.mkdir(exist_ok=True)

    safe_logger_name = "".join(ch if ch.isalnum() or ch in "-_" else "_" for ch in logger_name)
    safe_logger_name = safe_logger_name or "default"

    timestamp = datetime.now().strftime("%d%m%Y-%H%M%S")
    log_file = logs_dir / f"{safe_logger_name}_{timestamp}.log"
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(numeric_level)
    file_handler.setFormatter(formatter)

    # Add handlers to the logger
    if not logger.handlers:
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger