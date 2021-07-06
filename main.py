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

sleep(1)

video_url = input("Please, past the video's url here: ")

youtube = pytube.YouTube(video_url)

print(f"Downloading video: | {youtube.title}")
