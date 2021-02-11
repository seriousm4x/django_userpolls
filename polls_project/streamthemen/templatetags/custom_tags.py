from django import template
from streamthemen.models import Emote


register = template.Library()


@register.filter(name="split")
def split(value, arg):
    return value.split(arg)


@register.filter(name="match_emote")
def match_emote(value):
    find_emote = Emote.objects.filter(code=value)
    if find_emote:
        return find_emote.get()
    return None
