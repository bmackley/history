from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login
from django.conf import settings
import decimal, datetime
from homePage import models as m
from django.contrib.auth import logout
from . import templater


def process_request(request):
    if request.urlparams[0] == "logout":
        logout(request)
        return HttpResponseRedirect('/')
    createForm = CreateUserForm()
    if request.method == "POST":
        createForm = CreateUserForm(request.POST)
        if createForm.is_valid():
            newUser = m.User()
            print(createForm.cleaned_data['username'])
            newUser.username = createForm.cleaned_data['username']
            newUser.email = createForm.cleaned_data['email']
            newUser.password = createForm.cleaned_data['password']
            newUser.save()
            return HttpResponseRedirect('/homePage/tutorial')
    if request.urlparams[0] == "about":
        return templater.render_to_response(request, 'about.html')

    tvars = {
        'form' : createForm,
    }
    return templater.render_to_response(request, 'create_user.html', tvars)

class CreateUserForm(forms.Form):
    username = forms.CharField(required=True, label='Username', widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(required=False, label='Email', widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(required=False, widget=forms.PasswordInput(attrs={'class':'form-control'}))  
    retypepassword = forms.CharField(required=False, label='Re-Enter Password',  widget=forms.PasswordInput(attrs={'class':'form-control'}))
    

    def __init__(self, *args, **kwargs):
            self.request = kwargs.pop('request', None)
            super(CreateUserForm, self).__init__(*args, **kwargs)

    # def clean(self):
    #     if self.cleaned_data['username'] == "":
    #         raise forms.ValidationError("Please enter a username to sign up")
    #     if self.cleaned_data['password'] == "":
    #         raise forms.ValidationError("You must enter a password.")
    #     if self.cleaned_data['password'] != self.cleaned_data['retypepassword']:
    #         raise forms.ValidationError("The passwords do not match.")
    #     return self.cleaned_data
