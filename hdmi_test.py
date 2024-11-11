import numpy as np
import os

# this turns off the cursor blink:
os.system ("TERM=linux setterm -foreground black -clear all >/dev/tty0")

# this is the frambuffer for analog video output - note that this is a 16 bit RGB
# other setups will likely have a different format and dimensions which you can check with
# fbset -fb /dev/fb0 
buf = np.memmap('/dev/fb0', dtype='uint16',mode='w+', shape=(576,720))

# fill with white
buf[:] = 0xffff

for x in range(720):
    # create random noise (16 bit RGB)
    b = np.random.randint(0x10000,size=(576,720),dtype="uint16")
    # make vertical line at x black
    b[:,x]=0
    # push to screen
    buf[:] = b

# turn on the cursor again:    
os.system("TERM=linux setterm -foreground white -clear all >/dev/tty0")