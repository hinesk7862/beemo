import numpy as np
import os
import imageio as iio

im = iio.imread('beemopic.png')
print(im)

# this turns off the cursor blink:
os.system ("TERM=linux setterm -foreground black -clear all >/dev/tty0")

screen_width = 1440
screen_height = 1440

# this is the frambuffer for analog video output - note that this is a 16 bit RGB
# other setups will likely have a different format and dimensions which you can check with
# fbset -fb /dev/fb0 
buf = np.memmap('/dev/fb0', dtype='uint16',mode='w+', shape=(screen_height,screen_width))

print(buf)
# fill with white

b = np.full((screen_height,screen_width), 0xaef5)

buf[:] = b
buf[100:200] = 0x31c6