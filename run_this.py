import os
from mhmovie.code import *

temp_folder = "to be deleted"
# promt to ask for the video link
video_url = input("Paste the link of the video: ")

# video format to be downloaded according to youtube-dl
video_format = "399"  # FHD format
video_format = "394"  # lowest quality format
audio_format = "140"

# make a temporary directory named 'cache'
os.mkdir('.\\{}'.format(temp_folder))
# change working directory to 'cache'
os.chdir('.\\{}'.format(temp_folder))

# cmd command to download the video and audio of the specified formats.
os.system('cmd /c "youtube-dl -f {} {}"'.format(video_format, video_url))
os.system('cmd /c "youtube-dl -f {} {}"'.format(audio_format, video_url))

# change the format of the audio file from .m4a to .mp3
# delete the .m4a file after conversion
for file in os.listdir():
    if '.m4a' in file:
        os.system('cmd /c "ffmpeg -i \"{}\" audio.mp3"'.format(file))
        os.remove(file)

os.chdir('..')

# using mhmovie library, combining video with audio.
f = folder("{}".format(temp_folder))
f.save()

# renaming the output video file and moving it to the primary folder
new_name = input('Please enter a new name for the newly generated video file: ')
os.rename('.\\{}\\output.mp4'.format(temp_folder), '.\\' + new_name + '.mp4')

# deleting all the files in the cache folder
for file in os.listdir('{}'.format(temp_folder)):
    os.remove(os.path.join(temp_folder, file))

# finally removing the cache folder
os.rmdir(temp_folder)
