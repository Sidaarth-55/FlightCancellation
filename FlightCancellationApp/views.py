from django.shortcuts import render
from django.http import HttpResponse
from FlightCancellationApp.forms import PDFform
from FlightCancellationApp.models import PDF
from FlightCancellationApp.QuestionAnswer import *
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
    LatestRecord=PDF.objects.last()
    question=LatestRecord.question
    base_dir='/Users/sid/Desktop/Flight Cancellation Project/media/'
    path=os.listdir(base_dir)
    text=file_to_text(base_dir+path[0])
    output=QA(question,text)
    os.remove(base_dir+path[0])
    form=PDFform(request.POST, request.FILES)
    context={'form': form,'outputs': output}
    return render(request, 'FlightCancellationApp/results.html', context)