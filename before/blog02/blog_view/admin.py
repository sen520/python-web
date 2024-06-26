from django.contrib import admin

# Register your models here.
from blog_view.models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']


admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
