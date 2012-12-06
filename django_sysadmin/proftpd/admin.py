from django_sysadmin.proftpd import models

from django.contrib import admin


### actions

def setactive(modeladmin, request, queryset):
    queryset.update(active=True)
    setactive.short_description = "Set selected entries as active"

def setinactive(modeladmin, request, queryset):
    queryset.update(active=False)
    setinactive.short_description = "Set selected entries as NOT active"

## admin objects

class FTPUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'homedir', 'uid', 'gid', 'active', 'created', 'comment')
    list_filter = ('active', 'created' )
    search_fields = ['usernme', 'comment']
    actions = [setactive, setinactive]



admin.site.register(models.FTPUser, FTPUserAdmin)