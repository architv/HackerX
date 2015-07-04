from django.shortcuts import render, redirect
from credentials import *
from django.http import HttpResponseRedirect
import requests, json
import urllib, urllib2
from .models import User
from django.db import models

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
			'redirect_uri': REDIRECT_URI + "/home,																																																																																																																																									
		}
		payload = urllib.urlencode(payload)
		r = urllib2.Request(access_token_url, payload)
		response = urllib2.urlopen(r).read()
		access_token = response.split('=')[1].split('&')[0]
		try:
			user = User.objects.get(access_token = access_token)
			return redirect('main.views.home', user_name=user.user_name)
		except User.DoesNotExist:
			req = urllib2.Request(API_BASE_URL + "/user")
			req.add_header('Authorization', 'token ' + access_token)
			resp = urllib2.urlopen(req)
			content = json.loads(resp.read())
			new_user = User.objects.create(
				user_name=content['login'],
				email = content['email'],
				avatar_url = content['avatar_url'],
				num_followers = content['followers'],
				num_following = content['following'],
				access_token = access_token,
				num_repos_public = content['public_repos'],
				location = content['location'],
				blog_url = content['blog'],
				company = content['company'],
			)
			return redirect('main.views.home', user_name=content['login'])

	else:
		base_url = "https://github.com/login/oauth/authorize"
		redirect_uri = REDIRECT_URI + "/github_oauth"
		scope = 'user,public_repo,repo'
		oauth_url = base_url + "?client_id=" + CLIENT_ID + "&redirect_uri=" + redirect_uri + "&scope=" + scope + "&state=" + STATE
		return HttpResponseRedirect(oauth_url)