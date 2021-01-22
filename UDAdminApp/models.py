from django.db import models

# Create your models here.


class Apartment(models.Model):
	ap_Id = models.CharField(max_length=10,primary_key=True)
	ap_name = models.CharField(max_length=200, null=True,blank=False)
	flat_count = models.IntegerField(blank=False)
	floor = models.IntegerField(blank=False)

	def __str__(self):
		return self.ap_name
