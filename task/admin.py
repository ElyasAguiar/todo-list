from django.contrib import admin

from .models import Commitment, Category

# Register your models here.
class CommitmentAdmin(admin.ModelAdmin):
    list_display = ["title", "describe", "created", "datecompleted", "user", "category"]
    readonly_fields = ["created"]


admin.site.register(Commitment)
admin.site.register(Category)