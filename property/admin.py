from django.contrib import admin

from .models import Flat, Complaint

class RealtorAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner')
    readonly_fields = ('created_at',)
    list_display = ('address', 'price', 'new_building', 'construction_year',
        'owner_pure_phone', 'owners_phonenumber')
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    raw_id_fields = ('liked_by',)


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('author', 'flat',)


admin.site.register(Flat, RealtorAdmin)
admin.site.register(Complaint, ComplaintAdmin)
