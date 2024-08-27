import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

class Motor():
    '''
    This class defines a motor object that
    controls two motors using an L298N H-bridge
    motor controller.
    '''

    # channels = [ena, in1, in2, in3, in4, enb]
    def __init__(self, channels, freq):
        self.channels = channels
        self.freq = freq

        GPIO.setup(channels, GPIO.OUT)
        self.pwm0 = GPIO.PWM(self.channels[0], self.freq)
        self.pwm1 = GPIO.PWM(self.channels[-1], self.freq)
        self.pwm0.start(0)
        self.pwm1.start(0)
        
    def move(self, speed=0.5, turn=0.0, t=0):
        '''
        Control the motors with the given parameters
        '''
        
        speed *= 100
        turn *= 100
        left_speed = speed - turn
        right_speed = speed + turn

        if left_speed > 100:
            left_speed = 100
        elif left_speed < -100:
            left_speed = -100

        if right_speed > 100:
            right_speed = 100
        elif right_speed < -100:
            right_speed = -100
        
        self.pwm0.ChangeDutyCycle(abs(left_speed))
        self.pwm1.ChangeDutyCycle(abs(right_speed))

        if left_speed > 0:
            GPIO.output(self.channels[1], GPIO.LOW)
            GPIO.output(self.channels[2], GPIO.HIGH)
        else:
            GPIO.output(self.channels[1], GPIO.HIGH)
            GPIO.output(self.channels[2], GPIO.LOW)

        if right_speed > 0:
            GPIO.output(self.channels[3], GPIO.LOW)
            GPIO.output(self.channels[4], GPIO.HIGH)
        else:
            GPIO.output(self.channels[3], GPIO.HIGH)
            GPIO.output(self.channels[4], GPIO.LOW)

        time.sleep(t)

    def stop(self, t=0):
        '''
        Stops both motors
        '''
        self.pwm0.ChangeDutyCycle(0)
        self.pwm1.ChangeDutyCycle(0)
        time.sleep(t)

    def cleanup(self):
        '''
        Resets the state of the GPIO pins.
        '''
        GPIO.cleanup()
