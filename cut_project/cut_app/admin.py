from django.contrib import admin
from cut_app.models import Links

# Register your models here.
#admin.site.register(Links)
@admin.register(Links)
class Admin_links(admin.ModelAdmin):
    list_display = ('original_url', 'short_url', 'created_at', 'updated_at')
    list_filter = ('original_url', 'short_url', 'created_at', 'updated_at')