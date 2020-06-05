import argparse
import os
import logging
from datetime import datetime
import requests
import json
import config
def api_call():
    url_var = config.url
    #print(url_var)
    response = requests.get(url_var)
    print(response.headers)
    data = response.text
    parsed = json.loads(data)
    print(json.dumps(parsed, indent=4))

if (__name__ == '__main__'):
    api_call()

