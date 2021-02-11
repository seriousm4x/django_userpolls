from django.contrib import admin
from django.core.exceptions import ObjectDoesNotExist

from .models import Topic, Emote


class TopicAdmin(admin.ModelAdmin):
    list_display = ["title", "user_created",
                    "total_votes", "created_at", "completed"]
    search_fields = ["title"]
    list_filter = ["user_created", "created_at", "completed"]


class EmoteAdmin(admin.ModelAdmin):
    list_display = ["code", "emote_id", "provider"]
    search_fields = ["code", "emote_id", "provider"]
    list_filter = ["code", "emote_id", "provider"]


admin.site.register(Topic, TopicAdmin)
admin.site.register(Emote, EmoteAdmin)
