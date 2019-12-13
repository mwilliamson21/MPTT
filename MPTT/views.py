from MPTT.models import Folder

def show_folder(request):
    return render(request, "index.html", {'folders': Folder.objects.all()})