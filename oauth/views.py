from django.shortcuts import render, render_to_response

# Create your views here.
def index(request):
	render_to_response(request, 'index.html')