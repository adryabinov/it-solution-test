from django.contrib import admin
from messages_api.models import MessageFromSpace
# Register your models here.


@admin.action(description='Mark selected messages unread')
def make_unread(modeladmin, request, queryset):
    queryset.update(is_read=False)


class MessageFromSpaceAdmin(admin.ModelAdmin):
    actions = [make_unread]


admin.site.register(MessageFromSpace, MessageFromSpaceAdmin)
