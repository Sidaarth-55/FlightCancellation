from django.shortcuts import render
from django.http import HttpResponse
from FlightCancellationApp.forms import PDFform
# Create your views here.

def upload_form(request):
    if request.method == 'POST':
        form=PDFform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            context={'form': form}
            return render(request, 'FlightCancellationApp/index.html', context)
    context={'form': PDFform()}
    return render(request, 'FlightCancellationApp/index.html',context)
