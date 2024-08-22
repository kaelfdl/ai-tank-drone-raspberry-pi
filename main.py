import RPi.GPIO as GPIO
import time

def main():
    ena = 18

    in1 = 15
    in2 = 13
    in3 = 37
    in4 = 35

    enb = 16


    channels = [ena, in1, in2, in3, in4, enb]

    speed = 0
    freq = 100


    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(channels, GPIO.OUT)
    GPIO.output(channels[1:5], GPIO.LOW)
    print(channels[1:5])
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
            speed = 50
            print(direction)
            GPIO.output(in1, GPIO.LOW)
            GPIO.output(in2, GPIO.HIGH)
            GPIO.output(in3, GPIO.LOW)
            GPIO.output(in4, GPIO.HIGH)
            p0.ChangeDutyCycle(speed)
            p1.ChangeDutyCycle(speed)
            x = 'z'

        # stop
        elif x == 's':
            speed = 0
            direction = 'stop'
            print(direction)
            p0.ChangeDutyCycle(speed)
            p1.ChangeDutyCycle(speed)
            x = 'z'

        # exit
        elif x == 'e':
            GPIO.cleanup()
            break

        else:
            print('<<< Wrong data >>>')
            print('Please enter the defined data to continue...')

        time.sleep(1)

        # backward

        # left

        # right



if __name__ == "__main__":
    main()
