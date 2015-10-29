from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
#import of BOs
from Manager import models as m
from . import templater
import decimal, datetime

def process_request(request):
	if request.urlparams[0] =='new':
		form = UsersForm(initial={
			'CatalogProductID': "",
			'amount':"",
			'cost':"",
			#'store':"",
	})
	else:
		users = m.stockedProduct.objects.get(id=request.urlparams[0])
		form = UsersForm(initial={
			'CatalogProductID':users.catalogProductID,
			'amount':users.amount,
			'cost':users.cost,
			#'store':users.store,			
		})
	if request.method == 'POST':
		form = UsersForm(request.POST)
		if form.is_valid():
			if request.urlparams[0] == "new":
				users = m.stockedProduct()
			users.catalogProductID=form.cleaned_data['catalogProductID']
			users.amount=form.cleaned_data[ 'amount' ]
			users.cost=form.cleaned_data[ 'cost' ]
			users.store=form.cleaned_data['store']
			users.save()
			return HttpResponseRedirect('/Manager/stockedProduct/')
	
	tvars={
	'form':form,
	}
	
	return templater.render_to_response(request, 'edit_stockedProduct.html', tvars)
	
class UsersForm(forms.Form):
	catalogProductID = forms.ModelChoiceField(queryset=m.catalogProduct.objects.all())
	amount = forms.DecimalField()
	cost = forms.DecimalField()
	store = forms.ModelChoiceField(queryset=m.stores.objects.exclude(active=False))
	
	
