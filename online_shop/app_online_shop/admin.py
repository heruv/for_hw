from django.contrib import admin

# Register your models here.
from .models import OnlineShop

class OnlineShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'prise', 'auction', 'created_time', 'update_time']
    list_filter = ['auction', 'created_time',]
    actions = ['make_auction_false', 'make_auction_true']
    
    fieldsets = (
        ('about', {
            'fields' : ('title', 'description')
        }),
        
        ('financhial', {
            'fields' : ('prise', 'auction'),
            'classes' : ['collapse']
        }),
    )
    
    @admin.action(description='delite auction')
    def make_auction_false(self, request, queryset):
        queryset.update(auction = False)
        
    @admin.action(description='approve auction')
    def make_auction_true(self, request, queryset):
        queryset.update(auction = True)
        
        
admin.site.register(OnlineShop, OnlineShopAdmin)