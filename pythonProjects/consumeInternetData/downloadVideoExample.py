import pytube
from pytube import YouTube
import concurrent.futures
import time
import os
import ssl
import concurrent.futures

ssl._create_default_https_context = ssl._create_unverified_context
link = ["https://www.youtube.com/watch?v=_uQrJ0TkZlc&t=13s", "https://www.youtube.com/watch?v=rfscVS0vtbw", "https://www.youtube.com/watch?v=gfDE2a7MKjA"]
saved_path = "temp"

start = time.perf_counter()

def clean_dir():
    arr_of_files = os.listdir(saved_path)
    for rm_file in arr_of_files:
        os.remove(saved_path + "/" + rm_file)

def download_video(lnk):
    yt = pytube.YouTube(lnk)
    stream = yt.streams.first()
    #os.remove(saved_path + "/Python Tutorial - Python for Beginners [Full Course].mp4")
    print(f'{lnk} was downloaded')
    stream.download(saved_path)

clean_dir()
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_video, link)

finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')
