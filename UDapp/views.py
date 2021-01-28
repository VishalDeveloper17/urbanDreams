from django.shortcuts import render,redirect
from django.http import HttpResponse
from UDAdminApp.views import *
# Create your views here.

def index(request):
	return render(request,'pages/index.html')
def login(request):
	return render(request,'pages/login.html')
def signup(request): 
	return render(request,'pages/signup.html')

def submit(request):
	if request.method == 'POST':
		name = request.POST['unm']
		passw = request.POST['pwd']

		context = {'name':name, 'passw':passw}
		return render(request,'dash.html', context)
		#return redirect('mainpage')

