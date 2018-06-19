import RPi.GPIO as GPIO
import time


class Servomotor:
    """Precise controlled motor
    Start pwm with Duty Cycle is 2% --> Pulse with = 2%*20ms = 0.4ms
    Servo cannot turn on and off fast enough. Longer width, Higher Perceived V.
    Create PWM on pin 11, motor frequency is 50Hz --> period = 20ms
    1.0ms = CCW = 5.0 dc
    1.5ms = --  = 7.5 dc
    2.0ms = CW  = 2/20 = 10% duty cycle
    Motors map duration to direction / position (degrees). This uses direction.
    """
    def __init__(self):
        self.pin = 11
        self.freq = 50
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin, self.freq)
        self.position = {
            'left': 6,
            'right': 9,
        }
        self.pwm.start(2)

    def ServoUp(self):
        dc = self.position['left']
        print('start: ' + str(dc))
        self.pwm.ChangeDutyCycle(dc)
        time.sleep(1)

    def ServoDown(self):
        dc = self.position['right']
        print('start: ' + str(dc))
        self.pwm.ChangeDutyCycle(dc)
        time.sleep(1)

    def close(self):
        self.pwm.stop()
        GPIO.cleanup()


