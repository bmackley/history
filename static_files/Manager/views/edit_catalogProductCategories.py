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
		# return HttpResponseRedirect('/account/login')
	# if not request.user.is_staff and not request.user.is_superuser:
		# return HttpResponseRedirect('/account/youcantgothere')
		
		
	#print to console
	if request.urlparams[0] =='new':
		users = m.catalogProductCategories()
		users.active = True
		users.name=''
		users.url=""
		users.queryURL=''
		users.imagePath=""
		users.description = ""
	else:
		users = m.catalogProductCategories.objects.get(id=request.urlparams[0])

	
	form = UsersForm(initial={
		'name':users.name,
		'url':users.url,
		'queryURL':users.queryURL,
		'imagePath':users.imagePath,
		'description':users.description,
	})
	if request.method == 'POST':
		form = UsersForm(request.POST)
		if form.is_valid():
			users.name=form.cleaned_data['name']
			users.url=form.cleaned_data[ 'url' ]
			users.queryURL=form.cleaned_data[ 'queryURL' ]
			users.imagePath=form.cleaned_data[ 'imagePath' ]
			users.description=form.cleaned_data[ 'description' ]
			users.save()
			return HttpResponseRedirect('/Manager/catalogProductCategories/')
	
	tvars={
	'form':form,
	}
	
	return templater.render_to_response(request, 'edit_catalogProductCategories.html', tvars)
	
class UsersForm(forms.Form):
	name = forms.CharField(required=False, label='name', widget=forms.TextInput(attrs={'class':'form-control'}))
	url = forms.CharField(required=False, label='url', widget=forms.TextInput(attrs={'class':'form-control'}))
	queryURL = forms.CharField(required=False, label='Query url', widget=forms.TextInput(attrs={'class':'form-control'}))
	imagePath = forms.CharField(required=False, label='imagePath', widget=forms.TextInput(attrs={'class':'form-control'}))
	description = forms.CharField(required=False, label='description', widget=forms.TextInput(attrs={'class':'form-control'}))
	