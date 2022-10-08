from time import sleep
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522


class ReaderRFID():
    def __init__(self) -> None:
        GPIO.setmode(GPIO.BCM)

        self.buzzer = 14
        self.green_led = 21
        self.red_led = 26

        GPIO.setup(self.buzzer, GPIO.OUT)
        GPIO.setup(self.green_led, GPIO.OUT)
        GPIO.setup(self.red_led, GPIO.OUT)

        self.buzz = GPIO.PWM(self.buzzer, 1000)
        self.reader = SimpleMFRC522()

    def __del__(self):
        GPIO.cleanup()

    def blink(self, granted) -> None:
        if granted:
            pin = self.green_led
        else:
            pin = self.red_led

        GPIO.output(pin, GPIO.HIGH)
        self.buzz.start(100)
        sleep(0.25)  # time frame which the led will light up and the buzzer will beep

        GPIO.output(pin, GPIO.LOW)
        self.buzz.stop()
        sleep(1.5)  # a sleep time for preventing successive reads

    def read(self) -> int:
        while True:
            id, text = self.reader.read()
            print(f"Card id: {id}")
            self.blink(False)
            
            return id
