import logging
import json
import os
from datetime import datetime
import azure.functions as func
import azure.durable_functions as df

from shared import query_string as qs
from shared import function_mover as fm

def orchestrator_function(context: df.DurableOrchestrationContext):

    yield context.call_activity('details', "None")

    return "Success!"

main= df.Orchestrator.create(orchestrator_function)
