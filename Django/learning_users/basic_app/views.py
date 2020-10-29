from django.shortcuts import render
from basic_app.forms import UserForm,UserProfileInfoForm

# Login
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')

# decorator requires user to first be logged in before they can be loggedout
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("You are logged in, Nice")

def register(request):

    # Assume not registed at first
    registered = False
    
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

    # check for form vaildity
        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            # Hashes password
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            # sets up 1 to 1 relationship
            profile.user = user

            # chekc if picture is provided
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        
        else:
            print(user_form.errors,profile_form.errors)
    
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    # Make context dictionary, that links up with html file
    return render(request,'basic_app/registration.html',
                            {'user_form':user_form,
                            'profile_form':profile_form,
                            'registered':registered})

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Account Not Active")
        else:
            print("Someone tried to login and failed!")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("invalid login details supplied")

    else:
        return render(request,'basic_app/login.html',{})