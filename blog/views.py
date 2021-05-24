import datetime
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import UploadFileForm, NameForm, ContactForm
from django.http import HttpResponse, HttpResponseRedirect


def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'blog/upload.html', {'form': form})


def get_name(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = NameForm()
    return render(request, 'blog/forms.html', {'form': form})


def current_datetime(request):
    now = datetime.datetime.now()
    html = f"""<html><head><title>{datetime.datetime.today()}</title>
            </head><body><h1>Вреия сейчас : {now}</h1></body></html>"""
    return HttpResponse(html)
# Create your views here.
