import numpy as np
import os
import imageio as iio

im = iio.imread('beemopic.png')
r = im[1,1,1] 
g = im[1,1,2]
b = im[1,1,3]

print(r)
print(g)
print(b)

r5 = (r*31)//255
g6 = (g*63)//255
b5 = (b*31)//255

rgb565 = (r5 << 11) | (g6 <<5) | b5

print(hex(rgb565))
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