import RPi.GPIO as GPIO
import time

def dec2bin(v):
    return list(map(int, bin(v)[2::]))

GPIO.setmode(GPIO.BCM)
leds = [24, 22, 23, 27, 17, 25, 12, 16]
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)
button1 = 9
button2 = 10
num = 0
GPIO.setup(button1, GPIO.IN)
GPIO.setup(button2, GPIO.IN)
light_time = 0.2
while True:
    if GPIO.input(button1) and num<255:
        num+=1
    if GPIO.input(button2) and num>0:
        num-=1
    time.sleep(light_time)
    l1 = []
    l2 = []
    k = dec2bin(num)
    while len(k)<8:
        k = [0] + k
    for i in range(8):
        if k[i]:
            l1.append(leds[i])
        else:
            l2.append(leds[i])
    GPIO.output(l1, 1)
    GPIO.output(l2, 0)