from django.shortcuts import render
from django.http import HttpResponse

from .models import MediaUpload


def home(request):
    uploads = MediaUpload.objects.all().order_by('-id') if MediaUpload.objects.count() < 2 else MediaUpload.objects.all().order_by('-id')[:2]
    context = {
        "uploads": uploads
    }
    return render(request, "index.html", context)
