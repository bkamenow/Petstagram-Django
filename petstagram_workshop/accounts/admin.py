from django.contrib import admin

from petstagram_workshop.accounts.models import PetstagramUser


class PetstagramUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', )


admin.site.register(PetstagramUser, PetstagramUserAdmin)
