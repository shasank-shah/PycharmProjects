import pytube
from pytube import YouTube
import ssl
import sys

ssl._create_default_https_context = ssl._create_unverified_context
link = ["https://www.youtube.com/watch?v=KJgsSFOSQv0&t=12s"]
saved_path = "temp/"
yt = pytube.YouTube(link[0])
stream = yt.streams.first()
print(f'{link} was downloaded')
stream.download(saved_path)