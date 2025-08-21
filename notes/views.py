from django.shortcuts import render

from .models import Notes
# Create your views here.

def notes_list(request):
    notes_all = Notes.objects.all()
    return render(request, 'notes/notes_list.html', {'notes': notes_all})