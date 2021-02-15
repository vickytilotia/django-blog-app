from django.contrib import admin
from . import models
# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    # select what to display about a blog in admin section
    list_display = ('title','slug','publish','author','status')

admin.site.register(models.Post, AuthorAdmin)
