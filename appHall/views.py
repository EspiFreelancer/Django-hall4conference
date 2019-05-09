from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

from .models import User
from .forms import UserRegisterForm

# Create your views here.

def index(request):
	context = {}
	return render(request, 'index.html', context,)
	# return HttpResponse("Index Page")

def user(request):
	""" Create a new user or owner.	"""
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			new_user = form.save()

			return HttpResponseRedirect(reverse('appHall:index'))

	else:
		form = UserRegisterForm()
	
	return render(request, 'register.html', {'form': form})