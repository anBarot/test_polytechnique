from django.shortcuts import redirect
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import requests

from oauthlib.oauth2 import WebApplicationClient

token_url = 'https://api.notion.com/v1/oauth/token'
server_url = "http://localhost:8000"
redirect_uri = f"{server_url}/notion/redirect"

authorization_base_url = 'https://api.notion.com/v1/oauth/authorize'

@login_required
def notion_auth_start(request):
    client = WebApplicationClient(settings.NOTION_CLIENT_ID)
    authorize_request_url = client.prepare_request_uri(
        authorization_base_url, redirect_uri)
    return redirect(authorize_request_url)

@login_required
def notion_redirect(request):
    url = request.get_full_path()
		
    client = WebApplicationClient(settings.NOTION_CLIENT_ID)
    client.parse_request_uri_response(url)
    
    token_request_params = client.prepare_token_request(token_url, url, redirect_uri)

    auth = requests.auth.HTTPBasicAuth(
        settings.NOTION_CLIENT_ID, settings.NOTION_CLIENT_SECRET)
    response = requests.post(
        token_request_params[0], headers=token_request_params[1], data=token_request_params[2], auth=auth)
    return HttpResponse(response)