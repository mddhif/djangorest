from django	import forms
from django.forms import ModelForm
from .models import Flights





class contactform(forms.Form):
	date = forms.DateField(widget=forms.DateInput(attrs={'class': 'any_custom_class_name'}))
	#image = forms.ImageField(label='select an image',)
	

#class pubform(ModelForm):
#	class Meta:
#		model = publisher
#		fields = ['name', 'address', 'city', 'state', 'country', 'website']