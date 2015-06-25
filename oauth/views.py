from django.shortcuts import render, render_to_response
from credentials import *
from django.http import HttpResponseRedirect
import requests, json
import urllib
import urllib2

API_BASE_URL = "https://api.github.com"
# Create your views here.
def index(request):
	return render(request, 'index.html')

def github_oauth(request):
	if request.GET.get('code', None):
		code = request.GET['code']
		state = request.GET['state']
		access_token_url = "https://github.com/login/oauth/access_token"
		payload = {
			'client_id': CLIENT_ID,
			'client_secret': CLIENT_SECRET,
			'code': code,
			'redirect_uri': "http://localhost:8888/home"																																																																																																																																										
		}
		payload = urllib.urlencode(payload)
		r = urllib2.Request(access_token_url, payload)
		response = urllib2.urlopen(r).read()
		access_token = response.split('=')[1].split('&')[0]
		req = urllib2.Request(API_BASE_URL + "/user")
		req.add_header('Authorization', 'token ' + access_token)
		resp = urllib2.urlopen(req)
		content = json.loads(resp.read())
		print content

	else:
		base_url = "https://github.com/login/oauth/authorize"
		redirect_uri = "http://localhost:8888/github_oauth"
		scope = 'user,public_repo,repo'
		oauth_url = base_url + "?client_id=" + CLIENT_ID + "&redirect_uri=" + redirect_uri + "&scope=" + scope + "&state=" + STATE
		return HttpResponseRedirect(oauth_url)

# def home(request):
# 	if request.method == 'GET':
# 		code = request.GET['code']
# 		state = request.GET['state']
# 		if state == STATE:
# 			access_token_url = "https://github.com/login/oauth/access_token"
# 			payload = {
# 				'client_id': CLIENT_ID,
# 				'client_secret': CLIENT_SECRET,
# 				'code': code,
# 				'redirect_uri': "http://localhost:8888/"																																																																																																																																										
# 			}
# 			r = requests.post(access_token_url , data)