from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from Manager import models as m
from . import templater


def process_request(request):
		#Shows all stores in the DB
		# get BO
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/Manager/login')
	if not request.user.is_superuser:
		return HttpResponseRedirect('/Manageraccount/stores')
			
	if request.urlparams[0] == 'new':
		stores = m.stores()
		stores.locationName = 'New Store'
		stores.active = True
		stores.save()
		return HttpResponseRedirect('/Manager/edit_stores/' + str(stores.id )) 
	
	stores = m.stores.objects.get(id=request.urlparams[0]) #this isn't working right

	# run the form

	form = StoreForm(initial={
		'Location': stores.locationName,
		'Street': stores.street,
		'city': stores.city,
		'state': stores.state,
		'zipcode': stores.zipcode,
		'phone': stores.phone,
	})
	

	if request.method == 'POST':
		form = StoreForm(request.POST)
		if form.is_valid():
			stores.locationName = form.cleaned_data['locationName']
			stores.street = form.cleaned_data['street']
			stores.city = form.cleaned_data['city']
			stores.state = form.cleaned_data['state']
			stores.zipcode = form.cleaned_data['zipcode']
			stores.phone = form.cleaned_data['phone']
			stores.save()
			return HttpResponseRedirect('/Manager/stores/') 
	# return the template html
	tvars ={
	'form': form,
	}
	return templater.render_to_response(request, 'edit_stores.html', tvars)


	
class StoreForm(forms.Form):
	locationName = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
	street = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
	city = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
	state = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
	zipcode = forms.CharField(required=False, max_length=6, widget=forms.TextInput(attrs={'class':'form-control'}))
	phone = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
	#active = forms.BooleanField(required=False)





