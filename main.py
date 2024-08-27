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

    speed = 0.25
    freq = 100
    turn = 1
    level = 0

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

            motor_turn = 0
            # w forward 
            if keypress.keys[0]:
                if level < 4:
                    level += 1
                else:
                    level = 4
            # a left
            elif keypress.keys[1]:
                motor_turn = turn
            # s reverse
            elif keypress.keys[2]:
                if level > -4:
                    level -= 1
                else:
                    level = -4
            # d right
            elif keypress.keys[3]:
                motor_turn = -turn
            else:
                motor.stop()

            motor.move(speed=speed*level, turn=motor_turn)

            keypress.keys *= 0
    finally:
        keypress.cleanup()
    


if __name__ == "__main__":
    main()
