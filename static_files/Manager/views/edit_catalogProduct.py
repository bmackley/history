from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
#import of BOs
from Manager import models as m
from . import templater
import decimal, datetime

def process_request(request):
	'''Edit a Catalog Product'''
	
		
		
	#print to console
	if request.urlparams[0] =='new':
		form = UsersForm(initial={
		'CatalogProductID': "",
		'brand':"",
		'category':"",
		'price' :"",
		'rentalPrice':"",
		'replacementPrice':"",
		'description':"",
		'imagePath': "",
		})
		
	else:
		users = m.catalogProduct.objects.get(id=request.urlparams[0])
	
		form = UsersForm(initial={
			'CatalogProductID':users.catalogProductID,
			'brand':users.brand,
			'category':users.category,
			'price' :users.price,
			'rentalPrice':users.rentalPrice,
			'replacementPrice':users.replacementPrice,
			'description':users.description,
			'imagePath':users.imagePath,
	})
	if request.method == 'POST':
		form = UsersForm(request.POST)
		if form.is_valid():
			if request.urlparams[0] == "new":
				users = m.catalogProduct()
			users.catalogProductID=form.cleaned_data['catalogProductID']
			users.lcatalogProductID=users.catalogProductID.lower()
			users.brand=form.cleaned_data[ 'brand' ]
			users.lbrand=users.brand.lower()
			users.category=form.cleaned_data[ 'category' ]
			users.price=form.cleaned_data[ 'price' ]
			users.rentalPrice=form.cleaned_data['rentalPrice']
			users.replacementPrice = form.cleaned_data['replacementPrice']
			users.description = form.cleaned_data['description']
			users.ldescription = users.description.lower()
			users.imagePath = form.cleaned_data['imagePath']
			users.save()
			return HttpResponseRedirect('/Manager/catalogProduct/')
	
	tvars={
	'form':form,
	}
	
	return templater.render_to_response(request, 'edit_catalogProduct.html', tvars)
	
class UsersForm(forms.Form):
	catalogProductID = forms.CharField(required=False, label='catalogProductID', widget=forms.TextInput(attrs={'class':'form-control'}))
	brand = forms.CharField(required=False, label='brand', widget=forms.TextInput(attrs={'class':'form-control'}))
	category = forms.ModelChoiceField(queryset=m.catalogProductCategories.objects.all())
	price = forms.DecimalField(required=False, label='Price', widget=forms.TextInput(attrs={'class':'form-control'}))
	rentalPrice = forms.DecimalField(required=False, label='Rental Price', widget=forms.TextInput(attrs={'class':'form-control'}))
	replacementPrice = forms.DecimalField(required=False, label='Replacement Rate', widget=forms.TextInput(attrs={'class':'form-control'}))	
	description = forms.CharField(required=False, label='Description', widget=forms.TextInput(attrs={'class':'form-control'}))
	imagePath = forms.CharField(required=True, label='Image Path', widget=forms.TextInput(attrs={'class':'form-control'}))
