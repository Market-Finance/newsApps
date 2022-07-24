from shared import mover as mo

def auto_complete_mover_in():
    """
    DESCRIPTION: The purpose of this function is to download auto complete
                 from blob storage location 
    INPUT: None
    OUTPUT: encoded string 
    """
    # Blob file path and file_name source files
    blob_file_path= 'MarketFinance/common/auto_complete_new'
    blob_file_name= 'auto_complete.json'

    data= mo.blob_storage_download(blob_file_path, blob_file_name)
    return data

def details_mover_out(inMemory_data):
    """
    DESCRIPTION: The purpose of this function is to move mined news 
                 to its desired blob storage and data lake location
    INPUT: NONE
    OUTPUT: status string
    """
    # Blob file path and file_name destination
    blob_file_path= 'MarketFinance/news'
    blob_file_name= 'details.json'

    # Data lake path and file_name destination
    data_lake_file_path= 'news/details'
    data_lake_file_name= 'details'

    mo.blob_storage_upload(inMemory_data, blob_file_path, blob_file_name)
    mo.data_lake_storage_upload(inMemory_data, data_lake_file_path, data_lake_file_name)
    return "Success"