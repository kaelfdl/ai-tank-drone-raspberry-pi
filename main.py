import RPi.GPIO as GPIO
import time

ena = 18

in1 = 15
in2 = 13
in3 = 31
in4 = 29

enb = 16


channels = [ena, in1, in2, in3, in4, enb]

speed = 25
freq = 1000


def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(channels, GPIO.OUT)
    GPIO.output(channels[1:5], GPIO.LOW)
    p0 = GPIO.PWM(ena, freq)
    p1 = GPIO.PWM(enb, freq)

    p0.start(speed)
    p1.start(speed)

    direction = 'forward'

    print('/n')
    print(f'The default speed and direction is {speed} | {direction} ')
    
    while True:

        x = input("Prompt: ")

        # forward
        if x == 'w':
            print(direction)
            GPIO.output(in1, GPIO.HIGH)
            GPIO.output(in2, GPIO.LOW)
            GPIO.output(in3, GPIO.HIGH)
            GPIO.output(in4, GPIO.LOW)
            x = 'z'

        # stop
        elif x == 's':
            direction = 'stop'
            print(direction)
            GPIO.output(channels[1:5], GPIO.LOW)
            x = 'z'

        # exit
        elif x == 'e':
            GPIO.cleanup()
            break

        else:
            print('<<< Wrong data >>>')
            print('Please enter the defined data to continue...')

        time.sleep(0.1)
        GPIO.output(channels[1:5], GPIO.LOW)

        # backward

        # left

        # right



if __name__ == "__main__":
    main()
