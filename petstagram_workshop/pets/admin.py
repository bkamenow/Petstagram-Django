from django.contrib import admin

from petstagram_workshop.pets.models import Pet


# Register your models here.


class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


admin.site.register(Pet, PetAdmin)
