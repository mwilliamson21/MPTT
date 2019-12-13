from MPTT.models import Folder
from django.shortcuts import render

def show_folder(request):
    return render(request, "index.html", {'folders': Folder.objects.all()})