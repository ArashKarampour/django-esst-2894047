from django.urls import path

from . import views

urlpatterns = [
    path('notes', views.NotesListView.as_view()), # using class based view
    # path('notes', views.notes_list),
    # path('notes/<int:pk>', views.note_detail),
    path('notes/<int:pk>', views.NoteDetailView.as_view()), # using class based view
    path('popularnotes', views.PopularNotesListView.as_view())
]