from mhmovie.code import *

f = folder("Video audio mixer")
# folder has file of type mp4 and file of type mp3 and joins them automatically

f.save()  # save movie+music as output.mp4

# or
#f.save("the_final.mp4")  #save movie+music as the final.mp4 in the folder