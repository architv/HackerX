from django.db import models
# Create your models here.

class TimeStampedModel(models.Model):
	created = models.DateTimeField(auto_now=True)
	modified = models.DateTimeField(auto_now_add=True)

	class Meta:
		abstract = True

class User(TimeStampedModel):
	user_name = models.CharField(max_length=20, unique=True, blank=False)
	avatar_url = models.URLField(max_length=200)
	num_followers = models.IntegerField()
	num_following = models.IntegerField()
	access_token = models.CharField(max_length=250)
	email = models.EmailField(unique=True, blank=False)
	num_repos_public = models.IntegerField()
	location = models.CharField(max_length=100)
	blog_url = models.URLField()
	company = models.CharField(max_length=75)

	class Meta:
		db_table = 'github_user'

	def _get_profile(self):
		""" Return the profile url for the person. """
		return "https://github.com/%s" % (self.user_name)	