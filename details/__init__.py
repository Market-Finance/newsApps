# Import libraries
import os
import pandas as pd
import numpy as np
import requests
import json
import time
import random
import sys
from shared.fun_request import *

# Override default settings
sys.setrecursionlimit(10000)

def main(querystring):
    """
    DESCRIPTION: The purpose of this functin is to extract the list of news
                  clippings from asx and nasdaq.
    INPUT: query string dictionary
    OUTPUT: auto_complete dictionary
    """
    url= "https://apidojo-yahoo-finance-v1.p.rapidapi.com/news/v2/get-details"
    details_dict= miner(url, querystring)
    return details_dict