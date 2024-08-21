import RPi.GPIO as GPIO
import time

ena = 18
enb = 16

input = [15, 13, 31, 29]

GPIO.setmode(GPIO.BOARD)
GPIO.setup(ena, GPIO.OUT)
GPIO.setup(enb, GPIO.OUT)

for i in input:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.LOW)


