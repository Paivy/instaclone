from django.shortcuts import render,redirect
from .models import *
import datetime as dt

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
