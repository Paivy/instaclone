from django.shortcuts import render,redirect
from .models import *
import datetime as dt
from .forms import *
from django.conf import settings



from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .forms import RegisterUserForm


# Create your views here.

def index(request):
    profile = Profile.objects.all()

    posts = Image.objects.all()
    form=CommentForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request,( "Comment has been saved"))

    return render(request, 'index.html',{'posts': posts, 'form': form,'profile': profile,})



def like(request,post_id ):
    user = request.user
    post=Image.objects.get(id=post_id)
    current_likes= post.likes
    liked=Likes.objects.filter(user=user,image=post).count()
    if not liked:
        liked =Likes.objects.create(user=user,image=post)
        current_likes=current_likes +1
    else:
        liked =Likes.objects.create(user=user,image=post).delete()
        current_likes=current_likes -1

    post.likes=current_likes
    post.save()
    return redirect('index')



def post_picture(request):
    form=UploadImageForm(request.POST,request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        messages.success(request,('picture posted'))
        
        return redirect('index')
    return render(request, 'post.html',{'form': form,})


def make_profile(request):
    form=ProfileForm(request.POST,request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        messages.success(request,('Profile created'))
        return redirect('index')

    return render(request, 'make_profile.html',{'form': form,})



def search_profile(request):
    if request.method == 'POST':
        searched=request.POST.get('searched')
        profile=Profile.objects.filter(name__contains=searched)
        return render(request, 'search.html',{'searched':searched,'profile':profile})
       

    else:
        return render(request, 'search.html',{})


def comment(request,image_id):
    comment=Comment.objects.all()
    post=Image.objects.get(id=image_id)
    if request.method == 'POST':
        form=CommentForm(request.POST )
        if form.is_valid():
            form=form.save(commit=False)
            form.post=post
            form.save()
            return redirect('index')
    else:
        form=CommentForm()
    return render(request, 'comments.html',{'comment':comment,'form':form,'post':post})





#Auth

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user= authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.success(request,('there ws an error loggig in, please try again...'))
            return redirect('login')

    else:
        return render (request,'authenticate/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request,('you are logged out'))
    return redirect('index')

def register_user(request):
    if request.method == 'POST':
        form =RegisterUserForm(request.POST)
        if form.is_valid():

            username=request.POST['username']
            email=request.POST['email']
            subject='welcome to InstaApp'
            message=f'Hi {username} welcome to InstaApp and have fun! '
            from_email=settings.EMAIL_HOST_USER
            recipients=[email]
            # send_mail(subject, message,from_email,recipients)

            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,('Regestration succesful'))
            return redirect('index')
    else:
        form =RegisterUserForm()


    return render(request,'authenticate/register.html',{'form':form,})