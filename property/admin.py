from django.contrib import admin

from .models import Flat, Complaint, Owner


class FlatOwnersAdmin(admin.TabularInline):
    model = Flat.flat_owners.through
    raw_id_fields =('owner',)


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address')
    readonly_fields = ('created_at',)
    list_display = ('address', 'price', 'new_building', 'construction_year')
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    raw_id_fields = ('liked_by',)
    inlines = [FlatOwnersAdmin]


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('author', 'flat',)


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'pure_phone')
    raw_id_fields = ('owned_flats',)


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)