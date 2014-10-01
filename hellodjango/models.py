from django.db import models

class Hello(models.Model):
	name = models.CharField(max_length=50, blank=True, null=True)
	description = models.TextField(max_length=250, blank=True, null=True)
	created_at = models.DateTimeField()
	modified_at = models.DateTimeField()

	def __unicode__(self):
		return self.id