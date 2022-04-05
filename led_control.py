import RPi.GPIO as GPIO
from sys import argv

blue_led_pin = 23
white_led_pin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(blue_led_pin, GPIO.OUT)
GPIO.setup(white_led_pin, GPIO.OUT)

if int(argv[1]) == 1:
	GPIO.output(white_led_pin, GPIO.HIGH)

if int(argv[1]) == 0:
        GPIO.output(white_led_pin, GPIO.LOW)
