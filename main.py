import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


# import  responses

def call_api(url):
    """
    Basic usage
    :param url: the url of the API
    :return: True if status code is 200, False otherwise
    """
    r = requests.get(url)
    return True if r.status_code == 200 else False

def call_name():
    return True

def call_age():
    return True

def call_age():
    return True

