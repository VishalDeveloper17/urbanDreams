from django.shortcuts import render
from .models import *

# Create your views here.
def mainpage(request):
	apartments = Apartment.objects.all()
	total_apartments = apartments.count() 
	context = {'apartments':apartments, 'total_apartments': total_apartments}

	return render(request,'dash.html',context)
