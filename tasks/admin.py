from django.contrib import admin
from .models import Task
from .models import Profile

admin.site.register(Profile)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'done', 'created')
    search_fields = ('title',)
    list_filter = ('done',)