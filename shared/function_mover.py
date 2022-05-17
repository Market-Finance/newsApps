from shared import mover as mo

def get_details_mover_out(inMemory_data):
    """
    DESCRIPTION: The purpose of this function is to move mined news 
                 to its desired blob storage and data lake location
    INPUT: NONE
    OUTPUT: status string
    """
    # Blob file path and file_name destination
    blob_file_path= 'MarketFinance/news'
    blob_file_name= 'get_details.json'

    # Data lake path and file_name destination
    data_lake_file_path= 'common/get_details'
    data_lake_file_name= 'get_details'

    mo.blob_storage_upload(inMemory_data, blob_file_path, blob_file_name)
    mo.data_lake_storage_upload(inMemory_data, data_lake_file_path, data_lake_file_name)
    return "Success"