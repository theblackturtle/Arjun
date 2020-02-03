import re
import json
import time
import random
import warnings
import requests

import core.config

warnings.filterwarnings("ignore")  # Disable SSL related warnings


def requester(url, data, headers, GET, delay):
    if core.config.globalVariables["jsonData"]:
        data = json.dumps(data)
    if core.config.globalVariables["stable"]:
        delay = random.choice(range(3, 10))
    time.sleep(delay)
    headers["Host"] = re.search(r"https?://([^/]+)", url).group(1)
    if GET:
        try:
            response = requests.get(url, params=data, headers=headers, verify=False)
        except Exception:
            return None
    elif core.config.globalVariables["jsonData"]:
        try:
            response = requests.post(url, json=data, headers=headers, verify=False)
        except Exception:
            return None
    else:
        try:
            response = requests.post(url, data=data, headers=headers, verify=False)
        except Exception:
            return None
    return response
