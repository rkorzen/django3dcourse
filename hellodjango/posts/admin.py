from django.contrib import admin
from .models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "is_published"] 
    readonly_fields = ["created", "modified"]
    # exclude = ["is_published"]