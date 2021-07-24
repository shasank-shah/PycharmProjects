import pytube
from pytube import YouTube
import concurrent.futures
import time
import os
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
link = ["https://www.youtube.com/watch?v=_uQrJ0TkZlc&t=13s", "https://www.youtube.com/watch?v=rfscVS0vtbw", "https://www.youtube.com/watch?v=gfDE2a7MKjA",
         "https://www.youtube.com/watch?v=ZSPZob_1TOk", "https://www.youtube.com/watch?v=KJgsSFOSQv0", "https://www.youtube.com/watch?v=8PopR3x-VMY",
         "https://www.youtube.com/watch?v=vl794HKeXug", "https://www.youtube.com/watch?v=eIrMbAQSU34", "https://www.youtube.com/watch?v=hBh_CC5y8-s"]
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
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_video, link)
    finish = time.perf_counter()
    print(f'Finished in {round(finish - start, 2)} second(s)')

'''
start = time.perf_counter()

def run(thread_no):
    saved_path = "temp"+str(thread_no)
    link = "https://www.youtube.com/watch?v=_uQrJ0TkZlc&t=13s"
    yt = pytube.YouTube(link)
    stream = yt.streams.first()
    os.remove(saved_path+"/Python Tutorial - Python for Beginners [Full Course].mp4")
    stream.download(saved_path)
    return 'executed {}'.format(thread_no)

with concurrent.futures.ThreadPoolExecutor() as executor:
    f1 = executor.submit(run, 1)
    f2 = executor.submit(run, 2)
    f3 = executor.submit(run, 3)
    print(f1.result())
    print(f2.result())
    print(f3.result())

finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')

'''