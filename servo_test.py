import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
servo = GPIO.PWM(11,50)
try:
    print('s')
    servo.start(2)
    while True:
        time.sleep(1)
        servo.ChangeDutyCycle(6)
        time.sleep(3)
        servo.ChangeDutyCycle(8.5)
        time.sleep(3)
except KeyboardInterrupt:
    servo.stop()
    GPIO.cleanup()
