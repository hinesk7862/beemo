import numpy as np
import os

# this turns off the cursor blink:
os.system ("TERM=linux setterm -foreground black -clear all >/dev/tty0")

screen_width = 2160
screen_height = 1080

# this is the frambuffer for analog video output - note that this is a 16 bit RGB
# other setups will likely have a different format and dimensions which you can check with
# fbset -fb /dev/fb0 
buf = np.memmap('/dev/fb0', dtype='uint16',mode='w+', shape=(screen_height,screen_width))

print(buf)
# fill with white

b = np.full((screen_height,screen_width), 0xaef5)

while True:
    buf[:] = b

