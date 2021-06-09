from django.contrib import admin

from .models import Comment

# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Comment, CommentAdmin)
