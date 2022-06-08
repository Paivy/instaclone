from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


from django.forms import ModelForm
from .models import *

#Comment form
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields=('comment',   )

        labels={
            'comment':'',

        }

        widgets={
           'comment': forms.TextInput(attrs={'placeholder':' post a comment '}),
        }
