import json
import os
import tempfile
from datetime import datetime, timedelta

import requests

epoch = datetime.utcfromtimestamp(0)


def unix_time_millis(dt):
    return int((dt - epoch).total_seconds() * 1000.0)


def start_of_day(dt):
    return dt.replace(hour=0, minute=0, second=0, microsecond=0)


def end_of_day(dt):
    return dt.replace(hour=23, minute=59, second=59, microsecond=999999)


def end_of_month(dt):
    next_month = dt.replace(day=28) + timedelta(days=4)
    return end_of_day(next_month - timedelta(days=next_month.day))


def start_of_month(dt):
    return dt.replace(day=1, hour=0, minute=0, second=0, microsecond=0)


def write_jsonfile_to_tmp_dir(filename, json_data):
    tmp_dir = tempfile.mkdtemp()
    full_path = os.path.join(tmp_dir, filename)
    with open(full_path, 'w') as json_file:
        json_file.write(json.dumps(json_data))
        json_file.flush()
    return full_path


def download_to_json(download_url):
    return json.loads(requests.get(download_url).content)