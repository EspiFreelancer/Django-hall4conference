from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	context = {}
	return render(request, 'index.html', context,)
	# return HttpResponse("Index Page")

def user(request):
	return HttpResponse("User registration or login")
