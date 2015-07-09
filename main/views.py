from django.shortcuts import render
from oauth.models import User
from helpers.requests_helpers import *
from django.template import Library
import json
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from operator import itemgetter

# Create your views here.
def home(request, user_name):
	user = User.objects.get(user_name=user_name)
	print user.required_github_data
	if user.required_github_data:
		return render(request, 'main/index_profile.html', {'user_name': user_name, 'github_data': user.required_github_data, 'user':user})
	
	github_data = gtihub_api_request("GET", user.access_token, "/user/repos")
	required_github_data = []
	for index, data in enumerate(github_data):
		required_github_data.append({
			'name': data['name'],
			'description': data['description'],
			'url': data['svn_url'],
			'language': data['language'],
			'stars': data['stargazers_count'],
			'forks': data['forks_count'],
			'position': index,
			'positionx': index/3 + 1,
			'positiony': index % 3 + 1
		})
	user.github_data = github_data
	user.required_github_data = required_github_data
	print required_github_data
	user.save()
	return render(request, 'main/index_profile.html', {'user_name': user_name, 'github_data': required_github_data})

@require_http_methods(["PUT", "POST"])
def update(request, user_name):
	print user_name
	# print request.POST.iterlists()
	data_as_dict = dict(request.POST.iterlists())
	print data_as_dict
	# print user_name
	github_data = json.loads(data_as_dict.keys()[0])
	print github_data
	# print github_data
	required_github_data = github_data.get("github_data", None)
	print required_github_data
	if required_github_data and user_name:
		required_github_data = sorted(required_github_data, key=itemgetter('position'))
		user = User.objects.get(user_name=user_name)
		if user:
			user.required_github_data = required_github_data
			user.save()
		return HttpResponse(status=204)
	return HttpResponse(status=400)



