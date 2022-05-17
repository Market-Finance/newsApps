from datetime import datetime
from datetime import timedelta


def details_query_string(data:list):
    """
    DESCRIPTION: The purpose of this method is to extract
    the query string for the stock get news analysis API
    INPUT: List of JSON [Auto complete]
    OUTPUT: List of query strings- List of dictionaries
    """
    news_uuid_list = list()
    for i in range(len(data)):
        if data[i]['auto_complete']['news'] != []:
            for ns in range(len(data[i]['auto_complete']['news'])):
                uuid = data[i]['auto_complete']['news'][ns]['uuid']
                region = data[i]['region']
                queryString_dict = {"uuid":uuid, "region":region}
                news_uuid_list.append(queryString_dict)
    
    queryString_list = []
    for i in range(len(news_uuid_list)):
        if news_uuid_list[i] not in news_uuid_list[i + 1:]:
            queryString_list.append(news_uuid_list[i])

    return queryString_list