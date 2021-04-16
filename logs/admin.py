from django import forms
from django.contrib import admin

from .models import LogEntity


class LogEntityAdminForm(forms.ModelForm):
    class Meta:
        widgets = {
            'uri': forms.Textarea,
            'details': forms.Textarea,
        }


@admin.register(LogEntity)
class LogEntityAdmin(admin.ModelAdmin):
    form = LogEntityAdminForm
    list_display = ('id', 'datetime', 'ip_address', 'method', 'response_code')
    list_display_links = ('id', 'datetime',)
    search_fields = ('ip_address', 'method', 'uri')
    list_filter = ('method', 'response_code')

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False