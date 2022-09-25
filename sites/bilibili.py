import requests
from play_list import PalyListSite,headers

class Bilibili(PalyListSite):
    def get_all_videos(self):
        res = requests.get(self.play_list_url, headers=headers)
        js = res.json()
        # print(js)
        all_videos = []
        for ele in js["data"]["archives"]:
            video_url = "https://www.bilibili.com/video/" + ele["bvid"]
            all_videos.append(video_url)
        return all_videos