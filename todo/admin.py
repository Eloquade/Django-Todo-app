from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'priority', 'created_at']
    search_fields = ['id', 'title', 'description', 'priority', 'created_at']
    ordering = ('id', 'title', 'description', 'priority', 'created_at')


admin.site.register(Todo, TodoAdmin)
