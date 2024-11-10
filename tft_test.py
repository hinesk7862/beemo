import spidev
import RPi.GPIO as GPIO
import time

TFT_CS = 3
TFT_RESET = 0
TFT_RS = 0

GPIO.setmode(GPIO.BCM)

GPIO.setup(TFT_CS, GPIO.OUT)
GPIO.setup(TFT_RESET, GPIO.OUT)
GPIO.setup(TFT_RS, GPIO.OUT)

GPIO.output(TFT_CS, GPIO.LOW)
GPIO.output(TFT_RESET, GPIO.HIGH)

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 32000000

def send_command(cmd):
    GPIO.output(TFT_RS, GPIO.HIGH)
    spi.xfer([cmd])

def send_data(data):
    GPIO.output(TFT_RS, GPIO.LOW)
    if isinstance(data, list):
        spi.xfer(data)
    else:
        spi.xfer([data])

def display_image(buffer):
    send_command(0x2C)
    send_data(buffer)

def init_display():
    send_command(0x01)
    send_command(0x11)
    send_command(0x29)

def fill_screen_white():
    send_command(0x2A)
    send_data([0x00, 0x00, 0x00, 0xEF])
    send_command(0x2B)
    send_data([0x00, 0x00, 0x01, 0x3F])

    send_command(0x2C)

    white_pixel = [0xFF, 0xFF]
    buffer = white_pixel * (240*320)

    for i in range(0, len(buffer), 4096):
        send_data(buffer[i:i+4096])

try:
    GPIO.output(TFT_RESET, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(TFT_RESET, GPIO.HIGH)
    time.sleep(0.1)

    init_display()
    fill_screen_white()

finally:
    spi.close()
    GPIO.cleanup()
