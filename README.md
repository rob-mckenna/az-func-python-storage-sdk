# Azure Function Python Storage SDK sample

This repo is a sample demonstrating an Azure Function written in Python which leverages the Azure Storage SDK for Python.
The function will list blob files in a storage account and then creates a service SAS token for each blob.

It uses a target storage account with a blob container named "customer01".  This is where you'll load target files.

An application setting named "TargetStorageConnection" is required for the target storage account's connection string.

Helpful links:

[Quickstart: Azure Blob Storage client library for Python](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-python?tabs=managed-identity%2Croles-azure-portal%2Csign-in-azure-cli)

[Example: Access Azure Storage using the Azure libraries for Python](https://learn.microsoft.com/en-us/azure/developer/python/sdk/examples/azure-sdk-example-storage-use?tabs=cmd)

[Azure Storage client libraries for Python](https://learn.microsoft.com/en-us/python/api/overview/azure/storage?view=azure-python)

[Delegate access by using a shared access signature](https://learn.microsoft.com/en-us/rest/api/storageservices/delegate-access-with-shared-access-signature)

[Create a service SAS for a blob with Python](https://learn.microsoft.com/en-us/azure/storage/blobs/sas-service-create-python)

Note: This function originated from this quickstart [Quickstart: Azure Blob Storage client library for Python](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-python?tabs=managed-identity%2Croles-azure-portal%2Csign-in-azure-cli).  The quickstart logic has been left in place for testing purposes.

Additional links:
[Create a user delegation SAS for a blob with Python](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-user-delegation-sas-create-python)