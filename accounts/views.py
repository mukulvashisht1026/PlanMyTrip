from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import UserForm
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout


def signup(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			new_user = User.objects.create_user(**form.cleaned_data)
			return redirect('/')
	else:
		form = UserForm()
		return render(request,'accounts/signup.html',{'form':form})


# Create your views here.
def login(request):
	if request.method == 'POST':
		# form = AuthenticationForm(request=request, data=request.POST)
		if True:
			username = request.POST.get('username')
			password = request.POST.get('password')
			# print(username,password)
			user = authenticate(username=username, password=password)
			print(user,request)
			if user is not None:
				auth_login(request, user)
				# messages.info(request, f"You are now logged in as {username}")
				return redirect('/')
			else:
				return HttpResponse("try again!!")
				# messages.error(request, "Invalid username or password.")
		# else:
			# messages.error(request, "Invalid username or password.")
	# form = AuthenticationForm()
	return render(request = request,
                    template_name = "registration/login.html")


def logout(request):
	auth_logout(request)
	return redirect('/')