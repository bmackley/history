edit_question.py
======================
from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from stores import models as m
from . import templater


def process_request(request):
'''Shows all stores in the DB'''
# get BO
q = m.stores.objects.get(id=request.urlparams[0])

# run the form
form = StoreForm(initial={
'Location': m.locationName,
'Street': m.street,
'city': m.city,
'state': m.state,
'zipcode': m.zipcode,
'phone': m.phone,

})
if request.method == 'POST':
	form = StoreForm(request.POST)
		if form.is_valid():
			q.question_text = form.cleaned_data['question_text']
			q.pub_date = form.cleaned_data['pub_date']
			q.save()
			m.locationName = orm.cleaned_data['locationName'],
			m.street = orm.cleaned_data['street'],
			m.city = orm.cleaned_data['city'],
			m.state =orm.cleaned_data['state'],
			m.zipcode = orm.cleaned_data['zipcode'],
			m.phone = orm.cleaned_data['LocationName'],

# return the template html
template_vars = {
'form': form,
}
return templater.render_to_response(request, 'edit_question.html', template_vars)



'''
class QuestionForm(forms.Form):
	question_text=forms.CharField()
	pub_date=forms.DateTimeField()
	length=forms.IntegerField()




This is what we did in class 1/29
	form=QuestionForm(initial={
		'question_text': question.question_text,
		'pub_date': question.pub_date,
		'length': question.length,
		})

		if request.method =="POST":
			form = QuestionForm(request.POST)
			if form.is.valid() #validates data and then typecasts data for us.  This step also prevents SQL injection
				question.question_text = form.cleaned_data['question_text']
				question.pub_date = form.cleaned_data['pub_date']
				question.question.length = form.cleaned_data['length']
				question.save()


