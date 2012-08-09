import .models

from django.contrib import admin


### actions

def setactive(modeladmin, request, queryset):
	queryset.update(active=True)
	setactive.short_description = "Set selected entries as active"

def setinactive(modeladmin, request, queryset):
	queryset.update(active=False)
	setinactive.short_description = "Set selected entries as NOT active"

## admin objects

class VirtualMailboxDomainAdmin(admin.ModelAdmin):
	list_display = ('domain', 'active', 'created', 'comment')
	list_filter = ('active', 'created' )
	search_fields = ['domain', 'comment']
	actions = [setactive, setinactive]

class VirtualMailboxMapsAdmin(admin.ModelAdmin):
	list_display = ('mailbox', 'domain', 'active', 'created', 'maildir',
		'comment')
	list_filter = ('active', 'created' )
	search_fields = ['mailbox', 'domain', 'maildir', 'comment']
	actions = [setactive, setinactive]

class VirtualAliasMapsAdmin(admin.ModelAdmin):
	list_display = ('alias', 'goto', 'active', 'created', 'comment')
	list_filter = ('active', 'created' )
	search_fields = ['alias', 'goto', 'comment']
	actions = [setactive, setinactive]

class Sasl2AuthAdmin(admin.ModelAdmin):
	list_display = ('username', 'active', 'created', 'comment')
	list_filter = ('active', 'created' )
	search_fields = ['username', 'comment']
	actions = [setactive, setinactive]

#register adminobjects

admin.site.register(models.VirtualMailboxDomain, VirtualMailboxDomainAdmin)
admin.site.register(models.VirtualAliasMaps, VirtualAliasMapsAdmin)
admin.site.register(models.VirtualMailboxMaps, VirtualMailboxMapsAdmin)
admin.site.register(models.Sasl2Auth, Sasl2AuthAdmin)



## todo
# setup.py
# readme
# push to pip
# deploy to arge-mx