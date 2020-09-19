import os
from mhmovie.code import *

temp_folder = "temp_folder"
# prompt to ask for the video link
video_url = input("Paste the link of the video: ")

# video format to be downloaded according to youtube-dl
video_format = "399"  # FHD format
# video_format = "394"  # lowest quality format
audio_format = "140"

# make a temporary directory named 'temp_folder'
os.mkdir('.\\{}'.format(temp_folder))
# change working directory to 'cache'
os.chdir('.\\{}'.format(temp_folder))

# cmd command to download the video and audio of the specified formats.
os.system('cmd /c "youtube-dl -f {} {}"'.format(video_format, video_url))
os.system('cmd /c "youtube-dl -f {} {}"'.format(audio_format, video_url))

# change the format of the audio file from .m4a to .mp3
# delete the .m4a file after conversion
final_file_name = ""
for file in os.listdir():
    if '.mp4' in file:
        final_file_name = file

    if '.m4a' in file:
        os.system('cmd /c "ffmpeg -i \"{}\" audio.mp3"'.format(file))
        os.remove(file)

os.chdir('..')

# using mhmovie library, combining video with audio.
f = folder("{}".format(temp_folder))
f.save()

# renaming the output video file and moving it to the primary folder
os.rename('.\\{}\\output.mp4'.format(temp_folder), '.\\' + final_file_name)

# deleting all the files in the cache folder
for file in os.listdir('{}'.format(temp_folder)):
    os.remove(os.path.join(temp_folder, file))

# finally removing the cache folder
os.rmdir(temp_folder)
