from django import forms
from FlightCancellationApp.models import PDF

class PDFform(forms.ModelForm):
    class Meta:
        model=PDF
        fields=('name','file')