from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import CreateUserForm,ProfileForm
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user

# Create your views here.

@unauthenticated_user

def resister_user(request):
    form =CreateUserForm()

    if request.method=="POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,'your account has been created')
            return redirect('login')
        else:
            messages.info(request,'invalid Credentials')

            return redirect('register')


    context= {"form":form}





    return render(request,'register.html',context)


@unauthenticated_user
def login_user(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username ,password=password)
        if user is not None:
            login(request,user)
            messages.info(request,f'{username}, you are login ')

            return redirect('profile')

        else:
            messages.info(request,f'invalid username or password ')

            return redirect('login')



    return render(request,'login.html')



def logout_user(request):

    logout(request)
    messages.info(request,f'you logged out successfully ')
    return redirect('home')




@unauthenticated_user
def home(request):

    return render(request,'home.html')

@login_required(login_url='login')
def profile(request):

    return render(request,'profile.html')

@login_required(login_url='login')
def Edit_profile(request):
    name=request.user.profile
    form = ProfileForm(instance=name)
    if request.method == 'POST':
        form=ProfileForm(request.POST,request.FILES,instance=name)
        if form.is_valid():
            form.save()
            username= request.user.username
            messages.info(request,f'{username}, your profile has been updated')
            return redirect('profile')

    context={'form':form}


    return render(request,'Edit_profile.html',context)