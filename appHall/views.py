from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

from .models import User
from .forms import UserRegisterForm, isOwnerForm

# Create your views here.

def index(request):
	context = {}
	return render(request, 'index.html', context,)
	# return HttpResponse("Index Page")

def user(request):
	""" Create a new user or owner.	"""
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		sub_form = isOwnerForm(request.POST)

		if form.is_valid() and sub_form.is_valid():

			# Prepare the User model.
			new_user = form.save(commit=False)

			# Add the condition ForeignKey by saving the secondary form we setup.
			# new_user.is_owner = sub_form.save()

			# Save the main object and continue
			new_user.save()

			return HttpResponseRedirect(reverse('appHall:index'))

	else:
		form = UserRegisterForm()
		sub_form = isOwnerForm()
	
	return render(request, 'register.html', {'form': form, 'sub_form': sub_form})