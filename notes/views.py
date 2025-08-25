from django.shortcuts import render
from django.http import HttpResponseNotFound, Http404

from .models import Notes
# Create your views here.

def notes_list(request):
    notes_all = Notes.objects.all()
    return render(request, 'notes/notes_list.html', {'notes': notes_all})

def note_detail(request, pk):
    try :
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        # raise Http404("Note not found") # use this one with the render method at the end 
        # or use andother page for 404 error and render it
        # or use the below method wiht return
        return HttpResponseNotFound("Note not found")
    return render(request, 'notes/note_detail.html', {'note': note})