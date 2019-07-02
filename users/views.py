from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from .forms import SignUpForm

# Create your views here.
def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			newuser = form.save(commit=False)
			email = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password1')
			newuser.username = email # Save email as username.
			newuser.save()
			user = authenticate(username=email, password=raw_password)
			login(request, user)
			return redirect('home')
	else:
		form = SignUpForm()
	return render(request, 'registration/signup.html',{'form':form})