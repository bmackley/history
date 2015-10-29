from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from Manager import models as m 
from . import templater

def process_request(request):
	'''Shows the List of Stores'''
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/shop/login')
	
	if request.urlparams[0] == 'delete':
		catalogProductCategories = m.catalogProductCategories.objects.get(id=request.urlparams[1])
		catalogProductCategories.active = False 
		catalogProductCategories.save()

	catalogProductCategories = m.catalogProductCategories.objects.exclude(active=False)
	
	tvars = {
		'catalogProductCategories' : catalogProductCategories,
	}
	return templater.render_to_response(request, 'catalogProductCategories.html', tvars)