#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver


class AparatDownloader:
    def __init__(self, link):
        self.video_link = link
        self.driver_path = './chromedriver'
        self.options = webdriver.ChromeOptions()
        # self.options.add_argument('--headless')
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--ignore-ssl-errors')

    def request_site(self):
        self.driver = webdriver.Chrome(self.driver_path,
                                       chrome_options=self.options)
        self.driver.get(self.video_link)

    def link_box_click(self):
        self.box = self.driver.find_element_by_class_name(
            "sc-eldieg.gJpATt.button.download-button")
        self.box.click()

    def quality_144(self):
        self.quality144 = self.driver.find_element_by_id('144p')
        self.quality144.click()

    def quality_240(self):
        self.quality240 = self.driver.find_element_by_id('240p')
        self.quality240.click()

    def quality_360(self):
        self.quality360 = self.driver.find_element_by_id('360p')
        self.quality360.click()

    def quality_480(self):
        self.quality480 = self.driver.find_element_by_id('480p')
        self.quality480.click()

    def quality_720(self):
        self.quality720 = self.driver.find_element_by_id('720p')
        self.quality720.click()

    def quality_1080(self):
        self.quality1080 = self.driver.find_element_by_id('1080p')
        self.quality1080.click()

    def view_link(self):
        self.windows_name = self.driver.window_handles[1]
        self.driver.switch_to_window(self.windows_name)
        print(self.driver.current_url)
