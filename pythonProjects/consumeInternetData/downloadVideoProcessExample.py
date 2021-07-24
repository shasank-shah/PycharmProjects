import pytube
from pytube import YouTube
import concurrent.futures
import time
import os
import ssl
from multiprocessing import pool

ssl._create_default_https_context = ssl._create_unverified_context

link = ["https://www.youtube.com/watch?v=_uQrJ0TkZlc&t=13s", "https://www.youtube.com/watch?v=rfscVS0vtbw", "https://www.youtube.com/watch?v=gfDE2a7MKjA",
         "https://www.youtube.com/watch?v=ZSPZob_1TOk", "https://www.youtube.com/watch?v=KJgsSFOSQv0", "https://www.youtube.com/watch?v=8PopR3x-VMY",
         "https://www.youtube.com/watch?v=vl794HKeXug", "https://www.youtube.com/watch?v=eIrMbAQSU34", "https://www.youtube.com/watch?v=hBh_CC5y8-s"]

https://www.youtube.com/watch?v=vl794HKeXug
https://www.youtube.com/watch?v=7Pkkk52SfzI
def download_video(link):
    YouTube(link).streams.first().download()
    yt = YouTube(link)
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()

saved_path = "temp"

def clean_dir():
    arr_of_files = os.listdir(saved_path)
    for rm_file in arr_of_files:
        os.remove(saved_path + "/" + rm_file)

def download_video(link):
    yt = pytube.YouTube(link)
    stream = yt.streams.first()
    #os.remove(saved_path + "/Python Tutorial    - Python for Beginners [Full Course].mp4")
    #print(f'{link} was downloaded')
    stream.download(saved_path)

for i in range(1, 101):
    start = time.perf_counter()
    print("Execution {}".format(i))
    clean_dir()
    #print("The dir is cleaned")
    with concurrent.futures.ProcessPoolExecutor() as executor:
        #print("concurrent futures")
        executor.map(download_video, link)
    finish = time.perf_counter()
    print(f'Finished in {round(finish - start, 2)} second(s)')