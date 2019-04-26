"""
In Django framework, views.py is used to write the actual code, ie. from views.py all the functions were called and
the values will be returned to the web application

Here, there is no need for individual test function to test views.py, why because,
1. Here, I am using this view.py of Django to call all our other sub functions.
2. Also, I have test functions to test all the functions called in views individually.If those test functions fails,
   then obviously the values we are retuning to views.py would not be proper values
3. Ultimately, my web page will not have any return values to display for the request given
"""


from django.views.generic import TemplateView
from kunju.forms import HomeForm
from django.shortcuts import render
from django.contrib import messages
from . import geolocate, weather, air, flight
from datetime import date
from datetime import datetime


class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request):
        form = HomeForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            Location = form.cleaned_data['Location']
            f = form.cleaned_data['From_Date']
            t = form.cleaned_data['To_Date']
            if f > t:
                s = "From date cannot be greater than to date"
                args = {'form': form, 'text': s}
                return render(request, self.template_name, args)
            lati = geolocate.lati(Location)
            longi = geolocate.longi(Location)
            summary = weather.getsummary(lati, longi, f, t)
            s = ''
            airports = air.getnearestairports(lati, longi)
            min_fares = []
            for key, value in airports.items():
                print(key + "=>" + value)
                flights = flight.getcheapestflights('JFK',value,f)
                min_fares.append(flights)
            min_fares1 = []
            for key, value in airports.items():
                print(key + "=>" + value)
                flights = flight.getcheapestflights(value,'JFK',t)
                min_fares1.append(flights)
            for item in range(len(min_fares)):
                if min_fares[item] is not None:
                    print(min_fares[item].arrival_time)
            args = {'form': form, 'list': summary, 'list1': airports, 'obj': min_fares, 'objr':min_fares1 }
            return render(request, self.template_name, args)
        else:
            return render(request, self.template_name, {'form':form})
