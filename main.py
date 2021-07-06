import os

import pytube

from time import sleep


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


clearConsole()

print("\n\n\t\t\t\t******** WELCOME TO THE PYTUBE ********\n")

sleep(1)

print("\t\t\t\t\t (👍≖‿‿≖)👍 👍(≖‿‿≖👍)\n\n")

sleep(3)

clearConsole()

sleep(0.5)

print("\n\n\t（っ＾▿＾）  ☜(ˆ▿ˆc)\n")
video_url = input(f"Please, past the video's url here: ")

print("\n")

youtube = pytube.YouTube(video_url)

sleep(1)

print(f"\nDownloading video: {youtube.title}\n\n")

sleep(3)


video = youtube.streams.first()

video.download()

print("\n\n\t\t\t\t*** DOWNLOAD COMPLETED ***\n\n\t\t\t\t(っ◔◡◔)っ ❤ \t ❤(ˆ‿ˆԅ)\n\n\n")
