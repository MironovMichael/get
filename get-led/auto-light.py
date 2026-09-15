import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
led = 26
phtran = 6
GPIO.setup(led, GPIO.OUT)
GPIO.setup(phtran, GPIO.IN)
phtran = 6
state = 0
while True:
    if GPIO.input(phtran):
        GPIO.output(led, 1)
    else:
        GPIO.output(led, 0)