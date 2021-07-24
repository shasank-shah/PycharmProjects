import random
from pytube import YouTube
import time
#import pygame
count = 0

while 1:
    characters = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_'
    result = ''
    count = count + 1

    try:
        for i in range(0, 11):
            result += random.choice(characters)
        youtubeurl= "https://www.youtube.com/watch?v=" + result
        #print count,"...", (youtubeurl)
        print(youtubeurl)
    except Exception as e:
        print(e)