from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
#import of BOs
from Manager import models as m
from . import templater
import decimal, datetime

def process_request(request):
	'''Edit a single store'''
	# if not request.user.is_authenticated():
	# 	return HttpResponseRedirect('/Manager/login')

	# if not request.user.is_superuser:
	# 	return HttpResponseRedirect('/Manager/user')
		
		
	#print to console
	if request.urlparams[0] =='new':
		users = m.User()
		users.username=""
		users.first_name = ""
		users.last_name = ""
		users.address=""
		users.city=""
		users.state=""
		users.zipcode=""
		users.country=""
		users.phone=""
		users.is_staff = False
		users.is_superuser = False
		users.is_active= True
	else:
		users = m.User.objects.get(id=request.urlparams[0])

	
	form = UsersForm(initial={
		'username':users.username,
		'first_name':users.first_name,
		'last_name':users.last_name,
		'email':users.email,
		'password':users.password,
		'address':users.address,
		'city':users.city,
		'state':users.state,
		'zipcode':users.zipcode,
		'phone':users.phone,
		'is_staff': users.is_staff,
		'is_superuser': users.is_superuser,
		
	})
	if request.method == 'POST':
		form = UsersForm(request.POST)
		if form.is_valid():
			users.username=form.cleaned_data[ 'username' ]
			users.first_name=form.cleaned_data[ 'first_name' ]
			users.last_name=form.cleaned_data[ 'last_name' ]
			users.email=form.cleaned_data[ 'email' ]
			users.set_password(form.cleaned_data['password'])
			users.address=form.cleaned_data['address']
			users.city=form.cleaned_data['city']
			users.state=form.cleaned_data['state']
			users.zipcode=form.cleaned_data['zipcode']
			users.phone=form.cleaned_data['phone']
			users.is_staff=form.cleaned_data['is_staff']
			users.is_superuser = form.cleaned_data['is_superuser']
			users.save()
			return HttpResponseRedirect('/Manager/user/')
	
	tvars={
	'form':form,
	}
	
	return templater.render_to_response(request, 'edit_user.html', tvars)
	
class UsersForm(forms.Form):
	username = forms.CharField(required=True, help_text='email address', label='Username', widget=forms.TextInput(attrs={'class':'form-control'}))
	first_name = forms.CharField(required=False, label='First Name', widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name = forms.CharField(required=False, label='Last Name', widget=forms.TextInput(attrs={'class':'form-control'}))
	email = forms.CharField(required=False, label='Email', widget=forms.TextInput(attrs={'class':'form-control'}))
	password = forms.CharField(required=False, widget=forms.PasswordInput(attrs={'class':'form-control'}))	
	address = forms.CharField(required=False, label='Address', widget=forms.TextInput(attrs={'class':'form-control'}))
	city = forms.CharField(required=False, label='City', widget=forms.TextInput(attrs={'class':'form-control'}))
	state = forms.CharField(required=False, label='State', widget=forms.TextInput(attrs={'class':'form-control'}))
	zipcode = forms.CharField(required=False, label='Zip Code', widget=forms.TextInput(attrs={'class':'form-control'}))
	phone = forms.CharField(required=False, label='Phone', widget=forms.TextInput(attrs={'class':'form-control'}))
	is_staff = forms.BooleanField(required=False)
	is_superuser= forms.BooleanField(required=False)
	
