# Import libraries
import os
import pandas as pd
import numpy as np
import requests
import json
import time
import random
import sys
from shared.fun_request import miner

# Override default settings
sys.setrecursionlimit(10000)

import shared.function_mover as fm
import shared.query_string as qs

def main(querystring_list):
    """
    DESCRIPTION: The purpose of this function is to extract the list of news
                  clippings from asx and nasdaq.
    INPUT: query string dictionary
    OUTPUT: auto_complete dictionary
    """

    # Extract news details for a given stock
    url= "https://apidojo-yahoo-finance-v1.p.rapidapi.com/news/v2/get-details"

    details_dict_list= list()
    for querystring in querystring_list:
        details_dict= miner(url, querystring)
        details_dict_list.append(details_dict)
        
    return details_dict_list