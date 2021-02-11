from django.core.management.base import BaseCommand
import requests
from streamthemen.models import Emote


class Command(BaseCommand):
    def __init__(self):
        self.twitch_api_url = "https://api.twitchemotes.com/api/v4/channels/108776574"
        self.bttv_api_url = "https://api.betterttv.net/2/channels/wubbl0rz"
        self.ffz_api_url = "https://api.frankerfacez.com/v1/room/wubbl0rz"

    def handle(self, **options):
        Emote.objects.all().delete()
        print("fetching twitch emotes")
        self.fetch_twitch()
        print("fetching bttv emotes")
        self.fetch_bttv()
        print("fetching ffz emotes")
        self.fetch_ffz()

    def fetch_twitch(self):
        req = requests.get(self.twitch_api_url)
        if not req.status_code == 200:
            print("failed to fetch twitch emotes")
            return
        emotes = req.json()["emotes"]
        for i in emotes:
            Emote.objects.create(
                emote_id=i["id"], code=i["code"], provider="twitch")

    def fetch_bttv(self):
        req = requests.get(self.bttv_api_url)
        if not req.status_code == 200:
            print("failed to fetch bttv emotes")
            return
        emotes = req.json()["emotes"]
        for i in emotes:
            Emote.objects.create(
                emote_id=i["id"], code=i["code"], provider="bttv")

    def fetch_ffz(self):
        req = requests.get(self.ffz_api_url)
        if not req.status_code == 200:
            print("failed to fetch bttv emotes")
            return
        req_json = req.json()
        emotes = req_json["sets"][str(req_json["room"]["set"])]["emoticons"]
        for i in emotes:
            Emote.objects.create(
                emote_id=i["id"], code=i["name"], provider="ffz")
