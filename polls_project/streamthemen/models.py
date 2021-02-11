from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


def time_now():
    return timezone.now()


class Topic(models.Model):
    def __str__(self):
        return str(self.total_votes())

    def total_votes(self):
        return len(self.users_upvoted.all()) - len(self.users_downvoted.all())

    title = models.TextField(max_length=250, null=False, blank=False)
    user_created = models.ForeignKey(
        User, verbose_name="user", on_delete=models.CASCADE, null=True, blank=True)
    users_upvoted = models.ManyToManyField(
        User, related_name="upvotes", blank=True)
    users_downvoted = models.ManyToManyField(
        User, related_name="downvotes", blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=time_now)


class Emote(models.Model):
    emote_id = models.SlugField(null=False, blank=False)
    code = models.SlugField(null=False, blank=False)
    provider = models.SlugField(null=False, blank=False)
