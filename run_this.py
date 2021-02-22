import os
import tkinter as tk
from tkinter import filedialog

def download_video_with_audio(link, quality, target_directory):
    os.chdir(target_directory)
    os.system("youtube-dl -f \"bestvideo[height<={quality}]+bestaudio\" --write-srt --sub-lang en {link}".format(quality=quality, link=link))

if __name__ == "__main__":
    video_links = set()

    while True:
        link = input("Please paste the video link: ")
        if not link:
            break
        video_links.add(link) 
    
    video_qualities = {
                        1: 2160,
                        2: 1440,
                        3: 1080,
                        4: 720,
                        5: 480,
                        6: 360,
                        7: 240,
                        8: 144,
                        }
    for i in video_qualities:
        print(i, video_qualities[i])
    code = int(input("Please select the code for the desired video quality: "))
    video_quality = str(video_qualities[code])

    print("Note that the final output may have lower resolution depending on the availability.")

    print("Please select the save folder")
    target_directory = filedialog.askdirectory()

    for link in video_links:
        download_video_with_audio(link=link, quality=video_quality, target_directory=target_directory)
