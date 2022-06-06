import admin_thumbnails
from django.contrib import admin
# import export
from import_export.admin import ImportExportActionModelAdmin

# Register your models here.
from . import models


@admin.register(models.Service)
class ServiceAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ["id", "name", "service_type", "created_at", "is_active"]
    list_filter = ["is_active", "is_free"]
    list_display_links = ("id", "name", "created_at")
    date_hierarchy = "created_at"
    ordering = ["-created_at"]


@admin.register(models.ServiceCategory)
@admin_thumbnails.thumbnail("icon")
class ServiceCategoryAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ["id", "name", "icon_thumbnail"]
