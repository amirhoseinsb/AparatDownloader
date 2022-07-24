from aparat_dl import AparatDownloader
from config import banner, quality_banner


class Handler:

    @staticmethod
    def run():
        link = input(banner)
        video = AparatDownloader(link)
        quality = int(input(quality_banner))
        qualities = {
            1: "144p",
            2: "240p",
            3: "360p",
            4: "480p",
            5: "720p",
            6: "1080p"
        }

        video.request_site()
        video.link_box_click()
        video.quality(qualities.get(quality))
        video.view_link()


if __name__ == '__main__':
    Handler.run()
