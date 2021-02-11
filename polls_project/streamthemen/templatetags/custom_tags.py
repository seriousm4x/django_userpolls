from django import template
from streamthemen.models import Emote


register = template.Library()


@register.filter(name="split")
def split(value, arg):
    return value.split(arg)


@register.filter(name="match_emote")
def match_emote(value):
    word_list = value.split(" ")
    final_html = ""

    for word in word_list:
        find_emote = Emote.objects.filter(code=word)
        if find_emote:
            find_emote = find_emote.get()
            if find_emote.provider == "twitch":
                html = """
                <span class="mx-2 is-align-items-center">
                    <img src="https://static-cdn.jtvnw.net/emoticons/v1/{}/1.0">
                </span>
                """.format(find_emote.emote_id)
                final_html += html
            elif find_emote.provider == "bttv":
                html = """
                <span class="mx-2 is-align-items-center">
                    <img src="https://cdn.betterttv.net/emote/{}/1x">
                </span>
                """.format(find_emote.emote_id)
                final_html += html
            elif find_emote.provider == "ffz":
                html = """
                <span class="mx-2 is-align-items-center">
                    <img src="https://cdn.frankerfacez.com/emote/{}/1">
                </span>
                """.format(find_emote.emote_id)
                final_html += html
        else:
            final_html += f"{word} "
    return final_html


+=
