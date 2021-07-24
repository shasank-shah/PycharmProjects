import pytube
from pytube import YouTube
import sys
import ssl
import os
from threading import *
import time

ssl._create_default_https_context = ssl._create_unverified_context

class execution1:
    def run(Thread):
        saved_path = "temp1/"
        link = "https://www.youtube.com/watch?v=_uQrJ0TkZlc&t=13s"
        yt = pytube.YouTube(link)
        stream = yt.streams.first()
        for i in range(5):
            os.remove("temp/Python Tutorial - Python for Beginners [Full Course].mp4")
            print("Execution1: ", i)
            stream.download(saved_path)

class execution2:
    def run(Thread):
        saved_path = "temp2/"
        link = "https://www.youtube.com/watch?v=_uQrJ0TkZlc&t=13s"
        yt = pytube.YouTube(link)
        stream = yt.streams.first()
        for i in range(5):
            os.remove("temp/Python Tutorial - Python for Beginners [Full Course].mp4")
            print("Execution2: ", i)
            stream.download(saved_path)

t1 = execution1()
t2 = execution2()

def run_time():
    named_tuple = time.localtime() # get struct_time
    time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
    return time_string

def run():
    saved_path = "temp1/"
    link = "https://www.youtube.com/watch?v=_uQrJ0TkZlc&t=13s"
    yt = pytube.YouTube(link)
    stream = yt.streams.first()
    for i in range(25):
        print("The strat time: ", run_time())
        os.remove(saved_path+"/Python Tutorial - Python for Beginners [Full Course].mp4")
        print("Execution: ", i)
        stream.download(saved_path)
        print("The end time is: ", run_time())

run()
print("Program executed successfully")

#t1.sample()
'''
t2.start()

t1.join()
t2.join()

'''