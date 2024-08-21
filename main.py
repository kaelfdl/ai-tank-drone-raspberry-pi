import RPi.GPIO as GPIO
import time

ena = 18

in1 = 15
in2 = 13
in3 = 31
in4 = 29

enb = 16


input = [in1, in2, in3, in4]

def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ena, GPIO.OUT)
    GPIO.setup(enb, GPIO.OUT)

    for i in input:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, GPIO.LOW)

if __name__ == "__main__":
    main()
