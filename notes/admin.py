from django.contrib import admin

from . import models
# Register your models here.
class NotesAdmin(admin.ModelAdmin):
    list_display = ('title', 'created') # Display these fields in the admin list view
    # pass

admin.site.register(models.Notes, NotesAdmin)