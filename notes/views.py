from django.shortcuts import render
from django.http import HttpResponseNotFound, Http404
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Notes
# Create your views here.

class NotesListView(LoginRequiredMixin , ListView): # class based view using ListView for using a model
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'
    login_url = '/admin'
    
    def get_queryset(self): # this is the method to override the default queryset to filter the notes based on the logged in user: see ccbv website for more details: https://ccbv.co.uk/projects/Django/5.2/django.views.generic.list/ListView/#get_queryset
        return self.request.user.notes.all() # to show only the notes of the logged in user (we can access the user from the request object in this method)

# def notes_list(request):
#     notes_all = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes': notes_all})


class NoteDetailView(DetailView): # class based view using DetailView for using a model and a url with argument like pk (other things like exceptions are taken care of by default)
    model = Notes
    context_object_name = 'note'
    template_name = 'notes/note_detail.html'
    # pk_url_kwarg = 'pk' # default is pk so this line is optional

# def note_detail(request, pk):
#     try :
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         # raise Http404("Note not found") # use this one with the render method at the end 
#         # or use andother page for 404 error and render it
#         # or use the below method wiht return
#         return HttpResponseNotFound("Note not found")
#     return render(request, 'notes/note_detail.html', {'note': note})

class PopularNotesListView(ListView): # class based view using ListView for using a model with queryset to list the notes with likes greater than or equal to a certain number
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'
    queryset = Notes.objects.filter(likes__gte=0) # the default is Notes.objects.all() 
                                                  # gte is greater than or equal to, lte is less than or equal to, lt is less than, gt is greater than, exact is equal to, iexact is case insensitive equal to, contains is contains, icontains is case insensitive contains, startswith is starts with, istartswith is case insensitive starts with, endswith is ends with, iendswith is case insensitive ends with