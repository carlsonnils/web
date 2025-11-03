import os
from datetime import datetime

import toml


FILE_NAME = "request_options.toml"


def load_options() -> dict:
    if not os.path.exists(FILE_NAME):
        f = open(FILE_NAME, mode="w")
        f.close()

    options = toml.load(FILE_NAME)

    return options


def write_options(options: dict):
    f = open(FILE_NAME, mode="w")
    toml.dump(options, f)


def check_request_trigger(options: dict) -> bool:
    datetime_format = "%Y-%m-%d %H:%M:%S"

    last_time = options.get("last_request_time", "1900-01-01 00:00:00")
    time_since = datetime.today() - datetime.strptime(last_time, datetime_format)

    if time_since.total_seconds() > 60 * 10: # ten minutes
        options.update({"last_request_time": datetime.today().strftime(datetime_format)})
        write_options(options)
        return True

    return False
