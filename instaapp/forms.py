from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


from django.forms import ModelForm
from .models import *
from .forms import *
from django.conf import settings

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


# auth
class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username','first_name', 'last_name','email','password1','password2')

    def __init__(self, *args,**kwargs):
        super(RegisterUserForm, self).__init__(*args,**kwargs)

        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['class']='form-control'