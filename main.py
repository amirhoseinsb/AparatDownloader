from aparat_dl import AparatDownloader
from config import banner, quality_banner


class Handler:

    @staticmethod
    def run():
        link = input(banner)
        video = AparatDownloader(link)
        quality = int(input(quality_banner))
        qualities = {
            1: "video.quality_144()",
            2: "video.quality_240()",
            3: "video.quality_360()",
            4: "video.quality_480()",
            5: "video.quality_720()",
            6: "video.quality_1080()"
        }

        video.request_site()
        video.link_box_click()
        exec(qualities.get(quality))
        video.view_link()


if __name__ == '__main__':
    Handler.run()
