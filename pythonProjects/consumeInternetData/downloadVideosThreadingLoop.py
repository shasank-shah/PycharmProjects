import pytube
from pytube import YouTube
import threading
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
    for i in range(1, 2):
        #print("The strat time: ", run_time())
        os.remove(saved_path+"/Python Tutorial - Python for Beginners [Full Course].mp4")
        print("Threading {} - Execution {}: ".format(thread_no, i))
        stream.download(saved_path)
        #print("The end time is: ", run_time())

threads = []
for i in range(1, 2):
    t = threading.Thread(target=run, args=[1])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')