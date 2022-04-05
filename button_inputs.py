import RPi.GPIO as GPIO
import time

pin_a = 10
pin_b = 9
pin_c = 11

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_a, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pin_b, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pin_c, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        print(f"Pin A: {GPIO.input(pin_a)}, Pin B: {GPIO.input(pin_b)}, Pin C: {GPIO.input(pin_c)}")
        time.sleep(0.5)

except KeyboardInterrupt:
    GPIO.cleanup()