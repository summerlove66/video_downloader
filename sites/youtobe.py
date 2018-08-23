from play_list import PalyListSite


class Youtube(PalyListSite):
    def get_all_videos(self):
        print(self.play_site_attr)
        all_videos = []
        for ele in self.get_play_list_tree().xpath("//div[@id='img-preload']/img/@src"):
            video_id = ele.split("/")[4]
            video_url = "https://www.youtube.com/watch?v=" + video_id
            all_videos.append(video_url)

        return all_videos
