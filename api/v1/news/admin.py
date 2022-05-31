from django.contrib import admin

# Register your models here.
admin.site.site_title = "Social Med"
admin.site.site_header = "Social Med"
admin.site.index_title = "Social Medga hush kelibsiz"


from . import models
#remove group
from django.contrib.auth.models import Group
admin.site.unregister(Group)

#import export
from import_export.admin import ImportExportActionModelAdmin

@admin.register(models.News)
class NewsAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at','is_active' ]
    list_filter = ['is_active',]
    list_display_links = ('id', 'title', 'created_at')
    date_hierarchy = 'created_at'
    ordering = ['-created_at']
