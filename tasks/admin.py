from django.contrib import admin
from .models import Task
# Register your models here.
@admin.register(Task)

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title','complete','created')
    list_filter = ('complete',)
    search_fields = ('title','description')

    