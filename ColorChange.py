# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 11:56:50 2018

@author: matth
"""

from PIL import Image
import numpy as np
import randomcolor
import random
import ctypes
import os
import subprocess

SCRIPT = """/usr/bin/osascript<<END
tell application "Finder"
set desktop picture to POSIX file "%s"
end tell
END"""

def removeColor(img):
    '''
    expects image
    returns an image with everything but white removed
    '''
    img = Image.open(img)
    img = img.convert('RGB')
    pxList = list(img.getdata())
    color = tuple(chooseColor()[0])
    for i in range(len(pxList)):
        if(pxList[i][0]<240 and pxList[i][1]<240 and pxList[i][2]<240):
            pxList[i] = color

    img = Image.new('RGB',(1920,1080))
    img.putdata(pxList)
    return img
def chooseColor():
    '''
    Uses Kevin Wuhoo's python port of David Merfield's random color picker
    Modified randomcolor to return list of ints instead of string
    '''
    chooser = randomcolor.RandomColor()
    lum = ['random']
    color = chooser.generate(hue = 'random', luminosity = random.choice(lum),format_ = 'rgb')
    print(color)
    return color

im = removeColor('suckFacev2.png')
im.save('wall.png')
im.show()

#if windows
if(os.name == 'nt'):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:/Users/matth/.spyder-py3/suckFace/wall.png" , 0)
    
#if mac
elif(os.name == 'mac'):
    #need to put in file path where it is specified in script
   SCRIPT = """/usr/bin/osascript<<END
   tell application "Finder"
   set desktop picture to POSIX file "FILEPATH_TO_WALL.PNG"
   end tell
   END"""
   subprocess.Popen(SCRIPT%filename, shell=True)
   

    