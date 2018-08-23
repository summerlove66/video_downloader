import requests
import lxml.html
import random
import importlib

play_list_item = {'youtube': "youtube"}

headers = {

    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}


def site_func(url, attr):
    for key in play_list_item.keys():

        if key in url:
            module = play_list_item.get(key)
            site = importlib.import_module(module)
            Obj = getattr(site, module.capitalize())
            # Obj= globals().get(play_list_item.get(key))
            print("obj", Obj)
            if Obj:
                return Obj(url, attr).get_attr_videos()


class PalyListSite:
    def __init__(self, play_list_url, play_site_attr):
        self.play_site_attr = play_site_attr
        self.play_list_url = play_list_url
        self.all_videos = self.get_all_videos()

    def get_play_list_tree(self):
        res = requests.get(self.play_list_url, headers=headers)
        html = res.text
        return lxml.html.fromstring(html)

    def get_all_videos(self):
        pass

    def get_attr_videos(self):

        if self.play_site_attr == "all":
            return self.all_videos
        if self.play_site_attr.startswith("range"):
            play_list_strs = self.play_site_attr.split(":")
            print(play_list_strs)

            return self.all_videos[int(play_list_strs[1]): int(play_list_strs[2])]
        if self.play_site_attr.startswith("random"):
            random_num = self.play_site_attr.split(":")[1]
            return random.sample(self.all_videos, int(random_num))
        return []
