from django.shortcuts import render
from oauth.models import User
from helpers.requests_helpers import *
from django.template import Library

# Create your views here.
def home(request, user_name):
	user = User.objects.get(user_name=user_name)
	if user.github_data:
		return render(request, 'main/index.html', {'user_name': user_name, 'github_data': user.github_data})
	
	github_data = gtihub_api_request("GET", user.access_token, "/user/repos")
	user.github_data = github_data
	user.save()
	return render(request, 'main/index.html', {'user_name': user_name, 'github_data': github_data})

register = Library()
@register.filter
def modulo(value, arg): 
	return int(value) % int(arg)
