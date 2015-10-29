from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
#import of BOs
from Manager import models as m
from . import templater
import decimal, datetime

def process_request(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/Manager/login')
	if request.urlparams[0] =='new':
		form = UsersForm(initial={
			'CatalogProductID': "",
			'serialNumber':"",
			'datePurchased':"",
			'cost':"",
			'Store Location':"",
			'isRental':"",
			'isAvailable':"",
			'isNew':"",
			'dateSold':"",
	})
	else:
		users = m.serializedProduct.objects.get(id=request.urlparams[0])
		form = UsersForm(initial={
			'CatalogProductID':users.catalogProductID,
			'serialNumber':users.serialNumber,
			'datePurchased':users.datePurchased,
			'cost':users.cost,
			'Store Location':users.storeLocation,
			'isRental':users.isRental,
			'isAvailable':users.isAvailable,
			'isNew':users.isNew,
			'dateSold':users.dateSold,
			
		})
	if request.method == 'POST':
		form = UsersForm(request.POST)
		if form.is_valid():
			if request.urlparams[0] == "new":
				users = m.serializedProduct()
			users.catalogProductID=form.cleaned_data['catalogProductID']
			users.serialNumber=form.cleaned_data[ 'serialNumber' ]
			users.datePurchased=form.cleaned_data[ 'datePurchased' ]
			users.cost=form.cleaned_data[ 'cost' ]
			users.storeLocation=form.cleaned_data['storeLocation']
			users.isRental = form.cleaned_data['isRental']
			users.isAvailable=form.cleaned_data['isAvailable']
			users.isNew=form.cleaned_data['isNew']
			users.dateSold=form.cleaned_data['dateSold']
			users.save()
			return HttpResponseRedirect('/Manager/serializedProduct/')
	
	tvars={
	'form':form,
	}
	
	return templater.render_to_response(request, 'edit_serializedProduct.html', tvars)
	
class UsersForm(forms.Form):
	catalogProductID = forms.ModelChoiceField(queryset=m.catalogProduct.objects.all())
	serialNumber = forms.CharField(required=False)
	datePurchased = forms.DateField(required=False)
	cost = forms.DecimalField(required=False)
	storeLocation = forms.CharField(required=False)
	isRental = forms.BooleanField(required=False)	
	isAvailable = forms.BooleanField(required=False)
	isNew = forms.BooleanField(required=False)
	dateSold = forms.DateField(required=False)
	
