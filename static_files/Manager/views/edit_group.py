from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from Manager import models as m
from . import templater


def process_request(request):
		#Shows all group in the DB
		# get BO
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/Manager/login')
					
	if request.urlparams[0] == 'new':
		return HttpResponseRedirect('/member/create_group/') 
	group = m.Group.objects.get(id=request.urlparams[0]) #this isn't working right
	
	if request.user != group.administrator:
		return HttpResponseRedirect('/')

	form = GroupForm(initial={
		'groupName': group.groupName,
		'city': group.city,
		'state': group.state,
		'zipcode': group.zipcode,
		'phone': group.phone,
	})
	

	if request.method == 'POST':
		form = GroupForm(request.POST)
		if form.is_valid():
			group.groupName = form.cleaned_data['groupName']
			group.lgroupName = group.groupName.lower()
			group.city = form.cleaned_data['city']
			group.state = form.cleaned_data['state']
			group.zipcode = form.cleaned_data['zipcode']
			group.phone = form.cleaned_data['phone']
			group.save()
			return HttpResponseRedirect('/Manager/groups/' + str(group.id )) 
	# return the template html
	tvars ={
	'form': form,
	}
	return templater.render_to_response(request, 'edit_group.html', tvars)


	
class GroupForm(forms.Form):
	groupName = forms.CharField(required=False, label="Group Name", widget=forms.TextInput(attrs={'class':'form-control'}))
	city = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
	state = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
	zipcode = forms.CharField(required=False, max_length=6, widget=forms.TextInput(attrs={'class':'form-control'}))
	phone = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
	#active = forms.BooleanField(required=False)





