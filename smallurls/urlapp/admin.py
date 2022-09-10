from django.contrib import admin

from urlapp.models import Url, guest


class UrlsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'token', 'urls', 'alias', 'date')


class guestAdmin(admin.ModelAdmin):
    list_display = ('id', 'link', 'uuid')


admin.site.register(Url, UrlsAdmin)
admin.site.register(guest, guestAdmin)
