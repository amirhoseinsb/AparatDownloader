#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class AparatDownloader:
    def __init__(self, link):
        self.video_link = link
        self.driver_path = './chromedriver'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--ignore-ssl-errors')
        self.driver = webdriver.Chrome(
            self.driver_path,
            chrome_options=self.options
        )

    def request_site(self):
        self.driver.get(self.video_link)

    def link_box_click(self):
        box = self.driver.find_element_by_class_name(
            "sc-eldieg.gJpATt.button.download-button"
        )
        box.click()

    def quality(self, quality):
        try:
            video_with_quality = self.driver.find_element_by_id(quality)
        except NoSuchElementException:
            print(f"Sorry, this quality is not available.")
        else:
            video_with_quality.click()

    def view_link(self):
        windows_name = self.driver.window_handles[1]
        self.driver.switch_to.window(windows_name)
        print(self.driver.current_url)
        self.driver.close()
