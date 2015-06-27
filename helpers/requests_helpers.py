import requests, json
import urllib, urllib2

GITHUB_API_BASE_URL = "https://api.github.com"

def gtihub_api_request(request_type, access_token, endpoint):
	if request_type == "GET":
		req = urllib2.Request(GITHUB_API_BASE_URL + endpoint)
		req.add_header('Authorization', 'token ' + access_token)
		resp = urllib2.urlopen(req)
		return json.loads(resp.read())