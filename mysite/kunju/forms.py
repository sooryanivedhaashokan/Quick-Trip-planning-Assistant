"""
In Django framework, forms.py is used as an interface to request the data from the user and process the data and
to post the information back on web page

We used get and post http methods in views.py to request and render the data using forms.

Testing Forms:
If we are able to see the web page properly by running the server, then
check if the following fields are working fine when you enter data
Example:
Location: New York
From Date: 2019-08-10
To Date: 2019-08-14

Output:
If we could see the results in web page for the entered data, then forms.py is working fine.
ie. Data is received by the server using the get methods in views.py
Result is published in the server after processing using the post methods in views.py
"""

from django import forms
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker
from django.forms import ValidationError
import datetime


class HomeForm(forms.Form):

    Location = forms.CharField()
    From_Date = forms.DateField(widget=DatePicker())
    To_Date = forms.DateField(widget=DatePicker())
    def check_dates(self):
        f = self.cleaned_data['From_Date']
        t = self.cleaned_data['To_Date']
        if f > t:
            raise forms.ValidationError("From date cannot be greater than to date")
        else:
            return True


