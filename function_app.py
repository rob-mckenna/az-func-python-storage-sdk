import azure.functions as func
import logging, os, base64
from datetime import datetime, timedelta
from azure.storage.blob import generate_blob_sas, BlobSasPermissions, BlobServiceClient

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="HttpExample")
def HttpExample(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )

@app.function_name(name="GetBlobSASTokens")
@app.route(route="GetBlobSASTokens")
def GetBlobSASTokens(req: func.HttpRequest) -> func.HttpResponse: 
    logging.info('GetBlobSASTokens function processed a request.')

    logging.info('Create the BlobServiceClient object which will be used to create a container client')
    # Create the BlobServiceClient object which will be used to create a container client
    blob_service_client = BlobServiceClient.from_connection_string(os.environ["TargetStorageConnection"])
    container_name = "customer01"
    container_client = blob_service_client.get_container_client(container_name)

    logging.info('List the blobs in the container')
    # List the blobs in the container
    blob_list = container_client.list_blobs()
    # create a json object
    blob_json = {}
    # Add the blob names and the url to the json object
    permissions = 'r'

    account_key, account_name, url = extract_connection_string_parts(os.environ["TargetStorageConnection"])

    for blob in blob_list:
        blob_json[blob.name] = url + '/' + container_name + '/' + blob.name + '?' + \
            generate_sas_token(account_key, account_name, container_name, blob.name)

    logging.info('Return the blob json object')
    return func.HttpResponse(
        f"{blob_json}",
        status_code=200
        )

def extract_connection_string_parts(connection_string):
    parts = connection_string.split(";")
    account_name = parts[1].split("=")[1]
    account_key = parts[2].split("=")[1]
    url = "https://" + account_name + ".blob.core.windows.net"
    return account_key, account_name, url

def generate_sas_token(account_key, account_name, container_name, blob_name):
    # Encode the account key as base64
    account_key_bytes = account_key.encode('utf-8')
    account_key_base64 = base64.b64encode(account_key_bytes).decode('utf-8')

    # Set the start time and expiry time for the SAS token
    start_time = datetime.utcnow()
    expiry_time = start_time + timedelta(hours=1)

    # Generate the SAS token for the blob
    sas_token = generate_blob_sas(
        account_name=account_name,
        container_name=container_name,
        blob_name=blob_name,
        account_key=account_key_base64,
        permission=BlobSasPermissions(read=True),
        start=start_time,
        expiry=expiry_time
    )

    # Return the SAS token
    return sas_token