from django.contrib import admin
from .models import BoardModel
# Register your models here.

@admin.register(BoardModel)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'title', 'description')
# admin.site.register(BoardModel)
