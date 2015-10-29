from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from Manager import models as m 
from . import templater


def process_request(request):
	'''Shows the List of Stores'''
	if request.urlparams[0] == 'delete':
		user = m.User.objects.get(id=request.urlparams[1])   
		user.is_active = False
		user.save()


	if request.urlparams[0] == 'all':
		user = m.User.objects.all().order_by('username')
	else:
		user = m.User.objects.exclude(is_active=False).order_by('username')
	
	tvars = {
		'user' : user,
	}
	return templater.render_to_response(request, 'user.html', tvars)
