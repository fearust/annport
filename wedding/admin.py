from django.contrib import admin
from wedding.models import Mc, Backdrops, Youtube, Gallery, Cast, Homepage


class YoutubeInline(admin.StackedInline):
    model = Youtube
    extra = 1


class GalleryInline(admin.StackedInline):
    model = Gallery
    extra = 1


@admin.register(Mc)
class McAdmin(admin.ModelAdmin):
    list_display = ['pk', 'fullname', 'mcdisplay', 'mcmain']
    list_display_links = ['pk', 'fullname']
    inlines = (YoutubeInline, GalleryInline)

    def fullname(self, post):
        return '{} {}'.format(post.name, post.title)
    fullname.short_description = '전체이름'


@admin.register(Backdrops)
class BackdropsAdmin(admin.ModelAdmin):
    list_display = ['pk', 'backdrop_name']
    list_display_links = ['pk', 'backdrop_name']


@admin.register(Cast)
class CastAdmin(admin.ModelAdmin):
    list_display = ['pk', 'bridecontact', 'groomcontact', 'create_date']
    list_display_links = ['pk', 'bridecontact', 'groomcontact', 'create_date']

    def bridecontact(self, post):
        return '{} ({})'.format(post.bride, post.bride_phone)
    bridecontact.short_description = '신부정보'

    def groomcontact(self, post):
        return '{} ({})'.format(post.groom, post.groom_phone)
    groomcontact.short_description = '신랑정보'


@admin.register(Homepage)
class HomepageAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'sub_title']
    list_display_links = ['pk', 'title']
