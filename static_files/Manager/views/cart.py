from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from Manager import models as m 
from django.db.models import Q
from . import templater

def process_request(request):
	'''Makes the cart'''
	cart = request.session.get('cart', {})
	Objects = {}

	if request.urlparams[0]=="remove":
		if request.urlparams[1] in cart:
			if cart[reuest.urlparams[1]] > 1:
				cart[reuest.urlparams[1]] -=1
			else:
				del cart[request.urlparams[1]]
			request.session['cart'] = cart
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

	for key in cart:
		object = m.catalogProduct.objects.get(id=key)
		Objects[object] = cart[key]

	tvars = {
		'Objects': Objects,
	}
	return templater.render_to_response(request, 'cart.html', tvars)