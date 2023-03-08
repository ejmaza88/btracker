from django.contrib import admin
from trackerauth.models import User
from django.contrib.auth.admin import UserAdmin


class ArchivedModelAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        # Force admin to display all objects including archived
        qs = self.model.all_objs.get_queryset()
        ordering = self.get_ordering(request)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs

    def get_list_display(self, request):
        return list(self.list_display) + ['archived']


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('App User', {'fields': ('is_app_admin',)}),
    )
