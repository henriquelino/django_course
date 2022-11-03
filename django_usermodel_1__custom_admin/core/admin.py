from django.contrib import admin
from django.http import HttpRequest
from .models import Post
from django.contrib.auth import get_user_model


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author_full_name')

    # ---------- FIELDS ----------
    def author_full_name(self, instance: Post):
        return instance.author.get_full_name()

    author_full_name.short_description = 'Autor'

    # ----------  ----------
    def get_exclude(self, request: HttpRequest, obj=None):
        """Exclude fields based on filters"""
        user = get_user_model().objects.filter(username=request.user).first()
        print(user, request.user)
        if user.is_superuser:
            return []
        return ['author']

    def get_queryset(self, request: HttpRequest):
        """Modify the admin view based on logged user"""
        qs = super().get_queryset(request)
        return qs.filter(author=request.user)

    def save_model(self, request: HttpRequest, obj: Post, form, change) -> None:
        obj.author = request.user  # fix the author to the logged user
        return super().save_model(request, obj, form, change)