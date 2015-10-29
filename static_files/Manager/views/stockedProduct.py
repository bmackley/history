from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from Manager import models as m 
from . import templater

def process_request(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/Manager/login')
	
	if request.urlparams[0] == 'delete':
		stockedProduct = m.stockedProduct.objects.get(id=request.urlparams[1])
		stockedProduct.is_active = False
		stockedProduct.save()

	stockedProduct = m.stockedProduct.objects.all()

	
	tvars = {
		'stockedProduct' : stockedProduct,
	}
	return templater.render_to_response(request, 'stockedProduct.html', tvars)

