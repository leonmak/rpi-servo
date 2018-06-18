import RPi.GPIO as GPIO
import time


class Servomotor:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11, GPIO.OUT)
        # start pwm with Duty Cycle is 2% --> Pulse with = 2%*20ms = 0.4ms
        # Create PWM on pin 11 with frequency 50Hz --> period 20ms
        self.servo = GPIO.PWM(11, 50)
        self.servo.start(2.5)
        self.servo.ChangeDutyCycle(2.5)
        self.cur_X = 0  # initial value of servo motor

    def ServoUp(self):
        self.cur_X += 2.5
        if self.cur_X > 12:
            self.cur_X = 12.5
        self.servo.ChangeDutyCycle(self.cur_X)
        time.sleep(1)

    def ServoDown(self):
        self.cur_X -= 2.5
        if self.cur_X < 2.5:
            self.cur_X = 2.5
            self.servo.ChangeDutyCycle(self.cur_X)
        time.sleep(1)

    def close(self):
        self.servo.stop()


