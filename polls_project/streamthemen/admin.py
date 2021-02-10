from django.contrib import admin
from django.core.exceptions import ObjectDoesNotExist

from .models import Topic


class TopicAdmin(admin.ModelAdmin):
    list_display = ["title", "user_created",
                    "total_votes", "created_at", "completed"]
    search_fields = ["title"]
    list_filter = ["user_created", "created_at", "completed"]


admin.site.register(Topic, TopicAdmin)
