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

		if form.is_valid():

			# Save User model.
			new_user = form.save()

			# This check if the second form is full.
			if sub_form.is_bound:
				sub_form = isOwnerForm(request.POST)

				if sub_form.is_valid():
					
					# Prepare the Owner model.
					new_owner = sub_form.save(commit=False)

					# Add the ForeignKey to primary model.
					new_owner.user_count_id = new_user.id

					# Save the Owner model and continue.
					new_owner.save()

			return HttpResponseRedirect(reverse('appHall:index'))

	else:
		form = UserRegisterForm()
		sub_form = isOwnerForm()
	
	return render(request, 'register.html', {'form': form, 'sub_form': sub_form})