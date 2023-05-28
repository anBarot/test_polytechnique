from django.shortcuts import redirect
from django.conf import settings

from oauthlib.oauth2 import WebApplicationClient

server_url = "http://localhost:8000" # The URL of this server
redirect_uri = f"{server_url}/notion/redirect"

authorization_base_url = 'https://api.notion.com/v1/oauth/authorize'

def notion_auth_start(request):
    client = WebApplicationClient(settings.NOTION_CLIENT_ID)
    authorize_request_url = client.prepare_request_uri(
        authorization_base_url, redirect_uri)
    return redirect(authorize_request_url)