from django.db import models

# Create your models here.
class Feedback(models.Model):
	"""docstring for Feedback"""
	name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	feedback = models.TextField()
	rating = models.IntegerField(default=0, null=True)
	dateTime = models.DateTimeField(auto_now_add=True, blank=True)

	def __str__(self):
		return self.name + "(" + self.email + ")"
		