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

    # Extract chart_v2 for a given stock
    querystring_list= qs.analysis_query_string(auto_complete_list)

    details_activity= [
        context.call_activity('details', querystring) for
            querystring in querystring_list]
        
    details_list= yield context.task_all(details_activity)

    #Moving out the file to blob
    fm.get_details_mover_out(details_list)

    return "Success!"

main= df.Orchestrator.create(orchestrator_function)
