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

def get_graph_client():
    client_id = get_secret('YOUR_CLIENT_ID')
    client_secret = get_secret('YOUR_CLIENT_SECRET')
    tenant_id = get_secret('YOUR_TENANT_ID')
    credentials = TokenCredential(client_id, client_secret, tenant_id)
    return GraphClient(credential=credentials)

def device_sync(client, device_id):
    client.api(f'/deviceManagement/managedDevices/{device_id}/syncDevice').post()

def notify_recipients(client, device_id):
    recipients = ['email1@domain.com', 'email2@domain.com']
    subject = 'Compliance Enforcement Action Taken'
    body = f'Device enforcement action has been taken for device: {device_id}.'
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

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    device_id = req.params.get('device_id')
    if not device_id:
        return func.HttpResponse(
             "Please pass a device_id in the query string or in the request body.",
             status_code=400
        )
    else:
        client = get_graph_client()
        device_sync(client, device_id)
        notify_recipients(client, device_id)
        return func.HttpResponse(f"Device synchronization and notification action taken for {device_id}!", status_code=200)
