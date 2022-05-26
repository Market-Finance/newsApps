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

def main(name:str):
    """
    DESCRIPTION: The purpose of this function is to extract the list of news
                  clippings from asx and nasdaq.
    INPUT: query string dictionary
    OUTPUT: auto_complete dictionary
    """
    auto_complete_list= fm.auto_complete_mover_in()

    # Extract news details for a given stock
    url= "https://apidojo-yahoo-finance-v1.p.rapidapi.com/news/v2/get-details"
    querystring_list= qs.details_query_string(auto_complete_list)

    details_dict_list= list()
    for querystring in querystring_list:
        details_dict= miner(url, querystring)
        details_dict_list.append(details_dict)

    #Moving out the file to blob and datalake
    fm.details_mover_out(details_dict_list)
    return details_dict_list