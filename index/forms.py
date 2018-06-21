from django import forms
from models import *

class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Education
        # fields = ['appointment_date', 'name', 'type_of_appointment']

    appointment_date = forms.DateField(
        widget=forms.DateInput(format='%m/%d/%Y'),
        input_formats=('%m/%d/%Y', )
        )