from django.contrib import admin
# Register your models here.
from import_export.admin import ImportExportActionModelAdmin

from . import models


@admin.register(models.Maps)
class MapsAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ["id", "name", "created_at", "is_active"]
    list_filter = [
        "is_active",
    ]
    list_display_links = ("id", "name", "created_at")
    date_hierarchy = "created_at"
    ordering = ["-created_at"]


# Maps category
@admin.register(models.CategoryofMaps)
class CategoryofMapsAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ["id", "name"]
    list_display_links = ("id", "name")
