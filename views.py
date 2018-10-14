from django.shortcuts import render

# Create your views here.

from django.db.models import Q
from django.shortcuts import render_to_response

from django.http import HttpResponseRedirect, HttpResponse
from .models import Flights

from .forms import contactform



def search (request):
	yquery = request.GET.get('yq', '')
	mquery = request.GET.get('mq', '')
	flight = request.GET.get('flight', '')

	printed = yquery
	#if flight:
	#	qset = (Q(year__icontains=flight.year) & Q(month__icontains=flight.month))

			

		#results = Flights.objects.filter(qset).distinct()

	#else:
	#	results = []

	return render_to_response("search.html" , {
		 "r": flight, "q":flight, "printed":printed,



		}) 


def datesearch(request):
	if request.method == 'POST':
		form = contactform(request.POST)
		if form.is_valid():
			flightdate = form.cleaned_data['date']
			flights = Flights.objects.filter(year=flightdate.year)
			if flights:
				return HttpResponse('flight exists')
			else:
				return HttpResponse('does not exist')

			
	else:
		form = contactform()
	return render(request, 'myform.html', {'form':form})