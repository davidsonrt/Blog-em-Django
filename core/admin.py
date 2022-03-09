from django.contrib import admin
from .models import Post, Comentari
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'subtitle', 'text']
@admin.register(Comentari)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'text', 'begin_date']