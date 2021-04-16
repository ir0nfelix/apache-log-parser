from django.contrib import admin


class SuperuserDeleteAddPermissionAdminMixin:
    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False


class SuperuserChangePermissionAdminMixin:
    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False


class TrainServicesBaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'evs', 'train_number',)
    list_display_links = ('id', )
    search_fields = ('id', 'evs', 'train_number')
    list_filter = ('evs',)
