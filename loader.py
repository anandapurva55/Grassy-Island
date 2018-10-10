# media loader class

#load images

import os,sys,pygame

from pygame import *

def load_image(file,transparent = True):
    fullname = os.path.join('images',file)

    image = pygame.image.load(fullname)

    if transparent == True:
        image = image.convert()
        colorkey = image.get_at((0,0))

        image.set_colorkey(colorkey,RLEACCEL)   #RLEACCEL to provide better performance on non accelerated displays.


    else:
        image = image.convert_alpha()


    return image











