from mhmovie.code import *

m = movie("movie.mp4")#only mp4 movies
print(":".join(m.time()))# 00:03:06
mu = music("music.wav")# you can use mp3, wav, ogg or flv
mu.Aconvert()  # convert the music to mp3 from wav, ogg or flv
final = m + mu 
final.save("final.mp4") # save the movie with the music as final.mp4
final.clear() #delete music.wav if was converted

########################## automatic mode
f = folder("some_folder") 
# some_folder has file of type mp4 and file of type mp3 and joins them automatically
f.save()  # save movie+music as output.mp4
# or
f.save("the_final.mp4")  #save movie+music as the final.mp4 in the folder

############################ control audio of video
m = movie("movie.mp4")
m.mute()#mute music of movie to mute.mp4
mu = m.extract_music()
mu.vol(1.5)# up volume in 150% to vol.mp3
final = m+mu
final.save("movieUpVolume.mp4")
final.clear()
#delete movie.mp4 ,mute.mp4,vol.mp3