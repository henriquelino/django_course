from django.contrib import admin
from django.utils.html import format_html
# Register your models here.
from .models import Role, Service, TeamMember, Feature


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ("role_name", "active", "modified")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "icon", "active", "modified")


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" style="width: 80px; height: 80px">'.format(obj.picture.url))

    image_tag.short_description = 'Image'

    list_display = ("name", "role", "active", "modified", "image_tag")


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ("name", "icon", "active", "modified")
