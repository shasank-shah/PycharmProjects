import pytube
from pytube import YouTube
import threading
import time
import os
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
start = time.perf_counter()

def run():
    saved_path = "temp1"
    link = "https://www.youtube.com/watch?v=_uQrJ0TkZlc&t=13s"
    yt = pytube.YouTube(link)
    stream = yt.streams.first()
    for i in range(1):
        #print("The strat time: ", run_time())
        os.remove(saved_path+"/Python Tutorial - Python for Beginners [Full Course].mp4")
        print("Execution1: ", i)
        stream.download(saved_path)
        #print("The end time is: ", run_time())

def run1():
    saved_path = "temp2"
    link = "https://www.youtube.com/watch?v=_uQrJ0TkZlc&t=13s"
    yt = pytube.YouTube(link)
    stream = yt.streams.first()
    for i in range(1):
        #print("The strat time: ", run_time())
        os.remove(saved_path+"/Python Tutorial - Python for Beginners [Full Course].mp4")
        print("Execution2: ", i)
        stream.download(saved_path)
        #print("The end time is: ", run_time())

def run2():
    saved_path = "temp3"
    link = "https://www.youtube.com/watch?v=_uQrJ0TkZlc&t=13s"
    yt = pytube.YouTube(link)
    stream = yt.streams.first()
    for i in range(1):
        #print("The strat time: ", run_time())
        os.remove(saved_path+"/Python Tutorial - Python for Beginners [Full Course].mp4")
        print("Execution3: ", i)
        stream.download(saved_path)
        #print("The end time is: ", run_time())

t1 = threading.Thread(target=run)
t2 = threading.Thread(target=run1)
t3 = threading.Thread(target=run2)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')