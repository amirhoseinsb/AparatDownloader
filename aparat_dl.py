#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class Aparat_Downloader:
    def __init__(self):
        self.video_link = input('''
                                
   / \   _ __   __ _ _ __ __ _| |_ 
  / _ \ | '_ \ / _` | '__/ _` | __|
 / ___ \| |_) | (_| | | | (_| | |_ 
/_/   \_\ .__/ \__,_|_|  \__,_|\__|
        |_|                        
 ____                      _                 _           
|  _ \  _____      ___ __ | | ___   __ _  __| | ___ _ __ 
| | | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|
| |_| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   
|____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|   
                                                         
Created By : amirhoseinsohrabi

---------------------------------------------------

Please Enter The Video Link : ''')

        self.driver_path = './chromedriver' 
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--ignore-ssl-errors')

    def request_site(self):
        self.driver = webdriver.Chrome(self.driver_path,chrome_options=self.options)
        self.driver.get(self.video_link)
        
    def link_box_click(self):
        self.box = self.driver.find_element_by_class_name("sc-eldieg.gJpATt.button.download-button")
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
        
video = Aparat_Downloader()
quality = int(input('''
                     
1 = 144p
2 = 240p
3 = 360p
4 = 480p
5 = 720p
6 = 1080p

Enter The Quality of Video : '''))

if quality == 1:   
    video.request_site()
    video.link_box_click()
    video.quality_144()
    video.view_link()
    
elif quality == 2:    
    video.request_site()
    video.link_box_click()
    video.quality_240()
    video.view_link()

elif quality == 3:    
    video.request_site()
    video.link_box_click()
    video.quality_360()
    video.view_link()

elif quality == 4:    
    video.request_site()
    video.link_box_click()
    video.quality_480()
    video.view_link()

elif quality == 5:    
    video.request_site()
    video.link_box_click()
    video.quality_720()
    video.view_link()

elif quality == 6:    
    video.request_site()
    video.link_box_click()
    video.quality_1080()    
    video.view_link()
