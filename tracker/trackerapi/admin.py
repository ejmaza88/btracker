from django.contrib import admin
from rest_framework.authtoken.admin import TokenAdmin

from trackerauth.admin import ArchivedModelAdmin
from trackerapi.models import Baby

# DRF stuff
TokenAdmin.raw_id_fields = ["user"]


@admin.register(Baby)
class BabyAdmin(ArchivedModelAdmin):
    readonly_fields = ('id',)
    list_display = ("name", "dob", "time_of_birth", "due_day", "id")
    search_fields = ('name', 'id',)
