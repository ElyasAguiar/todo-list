from django.contrib import admin

from .models import Task, Category

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ["title", "describe", "created", "datecompleted", "important", "user", "category"]
    readonly_fields = ["created"]


admin.site.register(Task)
admin.site.register(Category)