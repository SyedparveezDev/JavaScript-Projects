from django.contrib import admin
from .models import IPO


@admin.register(IPO)
class IPOAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'status', 'open_date', 'close_date', 'issue_size', 'created_at')
    list_filter = ('status', 'open_date', 'close_date')
    search_fields = ('company_name', 'description')
    date_hierarchy = 'open_date'
    ordering = ('-created_at',)
    
    fieldsets = (
        ('Company Information', {
            'fields': ('company_name', 'company_logo', 'description')
        }),
        ('IPO Details', {
            'fields': ('issue_size', 'price_band', 'lot_size', 'status')
        }),
        ('Important Dates', {
            'fields': ('open_date', 'close_date', 'listing_date')
        }),
        ('Documents', {
            'fields': ('rhp_document', 'drhp_document'),
            'classes': ('collapse',)
        }),
    )
