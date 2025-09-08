# This is a script I wrote A LONG TIME AGO to beat (or cheat) on my 
# friends on "Lumber Jack" -- A simple web game
# It probabely won't work, but I decided keep it for historical
# reasons :-]

from pykeyboard import PyKeyboard
import gtk.gdk
import time

def getScreenshot():
    w = gtk.gdk.get_default_root_window()
    #sz = w.get_size()
    sz = tuple([460, 468])
    pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,sz[0],sz[1])
    pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])
    return pb.get_pixels_array()

def isTargetColor(targetPixel):
    #green
    #return tuple(targetPixel) == tuple([126, 173, 79])
    # brown
    return tuple(targetPixel) == tuple([161, 116, 56])

def appLoop():
    k = PyKeyboard()
    # 0: right, 1: left
    current = 1
    while 1 == 1:
        w = gtk.gdk.get_default_root_window()
        pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,460,468)
        pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,460,468)
        pixels = pb.get_pixels_array()
        #pixels = getScreenshot()
        
        if isTargetColor(pixels[248, 367]):
            # right
            current = 0
        elif isTargetColor(pixels[248, 313]):
            # left
            current = 1

        if current == 0:
            k.tap_key(k.left_key, n=2, interval=0.055)
        else:
            k.tap_key(k.right_key, n=2, interval=0.055)

        time.sleep(0.00001)

appLoop()
