import numpy as np
import os

# this turns off the cursor blink:
os.system ("TERM=linux setterm -foreground black -clear all >/dev/tty0")

# this is the frambuffer for analog video output - note that this is a 16 bit RGB
# other setups will likely have a different format and dimensions which you can check with
# fbset -fb /dev/fb0 
buf = np.memmap('/dev/fb0', dtype='uint16',mode='w+', shape=(1000,720))

# fill with an off green
buf[:] = 0xbf17

# turn on the cursor again:    
os.system("TERM=linux setterm -foreground white -clear all >/dev/tty0")