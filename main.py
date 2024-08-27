# import RPi.GPIO as GPIO
import time

from KeypressModule import Keypress
from MotorModule import Motor

def main():
    ena = 11

    in1 = 15
    in2 = 16
    in3 = 18
    in4 = 22

    enb = 13


    channels = [ena, in1, in2, in3, in4, enb]

    speed = 0
    freq = 100
    turn = 1


    direction = 'forward'

    print('/n')
    print(f'The default speed and direction is {speed} | {direction} ')

    keypress = Keypress()

    motor = Motor(channels, freq)

    try:
        while True:
            if keypress.get_key():
                break
            print(keypress.keys)

            if keypress.keys[0]:
                motor.move(t=1)
            elif keypress.keys[1]:
                motor.move(turn=-turn, t=1)
            elif keypress.keys[2]:
                motor.move(turn=turn, t=1)
            elif keypress.keys[3]:
                motor.move(t=1)
            else:
                motor.stop()

            keypress.keys *= 0
    finally:
        keypress.cleanup()
    


if __name__ == "__main__":
    main()
