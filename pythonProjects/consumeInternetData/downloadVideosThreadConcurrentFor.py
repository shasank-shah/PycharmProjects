import pytube
from pytube import YouTube
import concurrent.futures
import time
import os
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
start = time.perf_counter()

def run(thread_no):
    saved_path = "temp"+str(thread_no)
    link = "https://www.youtube.com/watch?v=_uQrJ0TkZlc&t=13s"
    yt = pytube.YouTube(link)
    stream = yt.streams.first()
    os.remove(saved_path+"/Python Tutorial - Python for Beginners [Full Course].mp4")
    stream.download(saved_path)
    return f'Done Executing...{thread_no}'

with concurrent.futures.ThreadPoolExecutor() as executor:
    thr_no = [3, 2, 1]
    results = [executor.submit(run, thr) for thr in thr_no]

finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')