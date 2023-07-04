import os
import logging
import azure.functions as func
from msgraph.core import GraphClient, TokenCredential
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

def get_secret(secret_name):
    kv_uri = f"https://{os.environ['KEY_VAULT_NAME']}.vault.azure.net"
    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=kv_uri, credential=credential)
    return client.get_secret(secret_name).value

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    device_id = req.params.get('device_id')
    if not device_id:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a device_id in the query string or in the request body for a personalized response.",
             status_code=200
        )
    else:
        # Get the GraphClient NOTE: THIS NEEDS REVISION, need to work out where to create GraphClient and how to pass it to the functions
        client = get_graph_client()

        # Perform actions
        device_sync(client, device_id)
        lock_device(client, device_id)
        notify_recipients(client, device_id)

        return func.HttpResponse(f"Device enforcement action taken for {device_id}!", status_code=200)

def get_graph_client():
    # Get the client ID from Azure Key Vault
    client_id = get_secret('YOUR_CLIENT_ID')

    # Get the client secret from Azure Key Vault
    client_secret = get_secret('YOUR_CLIENT_SECRET')

    # Get the tenant ID from Azure Key Vault
    tenant_id = get_secret('YOUR_TENANT_ID')

    # Create the GraphClient with the credentials NOTE: THIS NEEDS REVISION, need to work out where to create GraphClient and how to pass it to the functions
    credentials = TokenCredential(client_id, client_secret, tenant_id)
    return GraphClient(credential=credentials)

def device_sync(client, device_id):
    # Call the Graph API to sync the device
    client.api('/deviceManagement/managedDevices/{device_id}/syncDevice').post()

def lock_device(client, device_id):
    # Call the Graph API to lock the device
    client.api('/deviceManagement/managedDevices/{device_id}/remoteLock').post()

def notify_recipients(client, device_id):
    # Specify the recipient email addresses
    recipients = ['email1@domain.com', 'email2@domain.com']

    # Specify the subject of the email
    subject = 'Compliance Enforcement Action Taken'

    # Specify the body content of the email
    body = f'Device enforcement action has been taken for device: {device_id}.'

    # Send the email to each recipient
    for recipient in recipients:
        client.api('/me/sendMail').post({
            'message': {
                'subject': subject,
                'body': {
                    'contentType': 'Text',
                    'content': body
                },
                'toRecipients': [
                    {'emailAddress': {'address': recipient}}
                ]
            },
            'saveToSentItems': 'false'
        })
