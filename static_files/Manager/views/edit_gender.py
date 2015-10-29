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
		users = m.Gender()
		users.gender = ""
	else:
		users = m.Gender.objects.get()

	
	form = UsersForm(initial={
		'gender':users.gender,
	})
	if request.method == 'POST':
		form = UsersForm(request.POST)
		if form.is_valid():
			users.gender=form.cleaned_data['gender']
			users.save()
			return HttpResponseRedirect('/Manager/catalogProductCategories/')
	
	tvars={
	'form':form,
	}
	
	return templater.render_to_response(request, 'edit_gender.html', tvars)
	
class UsersForm(forms.Form):
	gender = forms.CharField(required=False, label='name', widget=forms.TextInput(attrs={'class':'form-control'}))
	