from django.contrib import admin
from . models import Car
from django.utils.html import format_html


# Register your models here.
class CarAdmin(admin.ModelAdmin):

    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.car_photo.url))

    thumbnail.short_description = 'Car_Image'


    list_display = ('id', 'thumbnail', 'car_title', 'city', 'condition', 'year', 'miles', 'price', 'miles', 'is_featured')
    list_display_links = ('id', 'thumbnail', 'car_title')
    search_fields = ('car_title', 'city', 'condition')
    list_filter = ('city', 'condition', 'year' )
    list_editable = ('is_featured',)

admin.site.register(Car, CarAdmin)
