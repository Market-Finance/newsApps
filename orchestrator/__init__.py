import logging
import json
import os
from datetime import datetime
import azure.functions as func
import azure.durable_functions as df

from shared import query_string as qs
from shared import function_mover as fm


def orchestrator_function(context: df.DurableOrchestrationContext):

    auto_complete_list= fm.auto_complete_mover_in()
    querystring_list= qs.details_query_string(auto_complete_list)
    list_querystrings= qs.getSublists(querystring_list,5)

    news_details_activity= [context.call_activity('details', querystring) for querystring in list_querystrings]
    
    news_details_list= yield context.task_all(news_details_activity)

    #Moving out the file to blob and datalake
    fm.details_mover_out(news_details_list)

    return "Success!"

main= df.Orchestrator.create(orchestrator_function)