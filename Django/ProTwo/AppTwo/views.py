from django.shortcuts import render
# from AppTwo.models import User
from AppTwo.forms import NewUserForm

# Create your views here.
def index(request):
    return render(request, 'AppTwo/index.html')

# Signup page form linked with model
def user(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        # commit to database and take you back to home page
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR form invalid')

    return render(request,'AppTwo/users.html',{'form':form})