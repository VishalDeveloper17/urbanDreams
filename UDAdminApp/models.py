from django.db import models
from month.models import MonthField

# Create your models here.


class Blocks(models.Model):
	block_No = models.CharField(max_length=10,primary_key=True)
	block_name = models.CharField(max_length=200, null=True,blank=False)
	flat_count = models.IntegerField(blank=False)
	floor = models.IntegerField(blank=False)

	def __str__(self):
		return self.block_No

class Flats(models.Model):
	VACAN = (
		('vacant', 'vacant'),
		('avail', 'avail')
		)
	SIZE = (
		('1BHK', '1BHK'),
		('2BHK', '2BHK'),
		('3BHK', '3BHK')
		)
	block = models.ForeignKey(Blocks, null=True, on_delete=models.SET_NULL)
	flat_No = models.CharField(primary_key=True, max_length=200, blank=False)
	vacancy = models.CharField(max_length=20, null=True, choices=VACAN)
	size = models.CharField(max_length=20,null=True, choices=SIZE)
	price = models.CharField(max_length=100000000, null=True)
	floor = models.IntegerField(blank=False)

	def __str__(self):
		return self.flat_No

class Maintenance(models.Model):
	STATUS = (
		('paid', 'paid'),
		('un-paid','un-paid')
		)
	flat = models.ForeignKey(Flats, null=True, on_delete=models.SET_NULL)
	payment_status = models.CharField(max_length=20, null=True, blank=False, choices=STATUS)
	month = MonthField("Month Value", help_text="some help...")

	def __str__(self):

		return self.flat.flat_No


class Services(models.Model):
	s_name = models.CharField(max_length=20, null=True, blank=False)
	s_charge = models.CharField(max_length=100000,null=True, blank=False)

	def __str__(self):
		return self.s_name