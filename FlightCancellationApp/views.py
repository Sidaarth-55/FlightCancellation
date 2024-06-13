from django.shortcuts import render
from django.http import HttpResponse
from FlightCancellationApp.forms import PDFform
from FlightCancellationApp.models import PDF
from FlightCancellationApp.summarize import *
import os
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

def output(request):
    output=pdf_to_text("/Users/sid/Desktop/Flight Cancellation Project/media/free-full-refund-tnc.pdf")
    return render(request, 'FlightCancellationApp/results.html', {'outputs':output})