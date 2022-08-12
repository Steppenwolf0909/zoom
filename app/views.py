from django.shortcuts import render
import jwt
from time import time
import requests
import json
from zoom.settings import env
key = env('API_KEY')
secret = env('API_SECRET')


def home (request):
    return render(request, 'home.html')

def link(request):
    return render(request, 'link.html', {"url": createMeeting()})

def getToken():
    return jwt.encode({'iss': key, 'exp': time() + 111111111}, secret, algorithm='HS256')

def createMeeting():
    headers = {'authorization': 'Bearer ' + getToken(),
               'content-type': 'application/json'}
    resp = requests.post(
        f'https://api.zoom.us/v2/users/me/meetings',
        headers=headers, data=json.dumps({})).text
    return json.loads(resp)["start_url"]



