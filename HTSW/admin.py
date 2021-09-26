from django.contrib import admin
from .models import Routes


class RouteAdmin(admin.ModelAdmin):
    list_display = ('id', 'r_name', 'r_count_stowaways', 'r_region')
    list_display_links = ('id', 'r_name', 'r_count_stowaways', 'r_region')
    search_fields = ('r_name',)


admin.site.register(Routes, RouteAdmin)
