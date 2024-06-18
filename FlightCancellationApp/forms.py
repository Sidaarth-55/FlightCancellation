from django import forms
from FlightCancellationApp.models import PDF

class PDFform(forms.ModelForm):
    class Meta:
        model=PDF
        fields=('name','file','question')

    def __init__(self, *args, **kwargs):
        super(PDFform, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'nameclass'})
        self.fields['name'].widget.attrs['placeholder'] = 'Enter your name'
        self.fields['question'].widget.attrs.update({'class': 'questionclass'})
        self.fields['question'].widget.attrs['placeholder'] = 'Enter your question'
        self.fields['file'].widget=forms.FileInput()
        self.fields['file'].widget.attrs={'class':'fileuploadclass'}