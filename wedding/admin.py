from django.contrib import admin
from wedding.models import Mc, Backdrops, Youtube, Gallery, Cast


class YoutubeInline(admin.StackedInline):
    model = Youtube
    extra = 1


class GalleryInline(admin.StackedInline):
    model = Gallery
    extra = 1


@admin.register(Mc)
class McAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'title']
    inlines = (YoutubeInline, GalleryInline)


@admin.register(Backdrops)
class BackdropsAdmin(admin.ModelAdmin):
    list_display = ['pk']


@admin.register(Cast)
class CastAdmin(admin.ModelAdmin):
    list_display = ['pk', 'bride', 'groom', 'create_date']