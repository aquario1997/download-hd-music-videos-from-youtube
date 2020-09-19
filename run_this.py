#step 1: execute the program in a folder where the final video should be
#step 2: download the video of specified format in a newly created folder 'cache'.
#step 3: download the audio for the same video in the newly created folder 'cache'.
#step 4: now the program should go to cache folder to work in it.
#step 5: now it should combine the video and audio together.
#step 6: the program should ask the user for the name of the file.
#step 7: the program should change the name of the output file to the given name.
#step 8: move the generated output video to the original folder.
#step 9: delete the newly created folder




import os
from mhmovie.code import *

#promt to ask for the video link
video_url = input("Paste the link of the video: ")

#video format to be downloaded according to youtube-dl
video_format = "399"
audio_format = "140"

#make a temporary directory named 'cache'
os.mkdir('.\\cache')
#change working directory to 'cache'
os.chdir('.\\cache')

#cmd command to download the video and audio of the specified formats.
os.system('cmd /c "youtube-dl -f {} {}"'.format(video_format, video_url))
os.system('cmd /c "youtube-dl -f {} {}"'.format(audio_format, video_url))

#change the format of the audio file from .m4a to .mp3
#delete the .m4a file after conversion
for file in os.listdir():
    if '.m4a' in file:
        os.system('cmd /c "ffmpeg -i \"{}\" audio.mp3"'.format(file))
        os.remove(file)

os.chdir('..')

#using mhmovie library, combining video with audio.
f = folder("cache")
f.save()

#renaming the output video file and moving it to the primary folder
new_name = input('Please enter a new name for the newly generated video file: ')
os.rename('.\\cache\\output.mp4', '.\\' + new_name + '.mp4')

#deleting all the files in the cache folder
for file in os.listdir('cache'):
    os.remove(os.path.join('cache', file))

#finally removing the cache folder
os.rmdir('cache')
