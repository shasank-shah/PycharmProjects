import pytube
from pytube import YouTube
import concurrent.futures
import time
import os
import ssl
from multiprocessing import pool
ssl._create_default_https_context = ssl._create_unverified_context
from time import sleep

class download_video:
    def __init__(self, path, link):
        self.path = path
        self.link = link
        #self.time_capture = time_capture

    def print_time(self):
        print(time.perf_counter())

    def clean_dir(self):
        files_list = os.listdir(self.path)
        for file in files_list:
            os.remove(self.path + file)

    def video_download(self):
        yt = pytube.YouTube(self.link)
        stream = yt.streams.first()
        stream.download(self.path)

try:
    for i in range(1, 101):
        print(i)
        vd = download_video('/Users/shasankshah/Shasank/PycharmProjects/consumeInternetData/temp/', 'https://www.youtube.com/watch?v=rfscVS0vtbw')
        vd.print_time()
        vd.clean_dir()
        vd.video_download()
        vd.print_time()
except Exception as e:
    print(e)