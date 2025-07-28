from django import forms
from .models import AccidentReport

class AccidentReportForm(forms.ModelForm):
    class Meta:
        model = AccidentReport
        fields = '__all__'
