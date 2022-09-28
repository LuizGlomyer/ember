#!/usr/bin/env python

from time import sleep
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

GPIO.setmode(GPIO.BCM)

reader = SimpleMFRC522()

buzzer = 14
led_verde = 21
led_vermelho = 26

GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(led_verde, GPIO.OUT)
GPIO.setup(led_vermelho, GPIO.OUT)

buzz = GPIO.PWM(buzzer, 1000)

try:

    while True:
        id, text = reader.read()
        # check cleanup on IDE's exit
        #GPIO.output(led_vermelho, GPIO.HIGH)
        GPIO.output(led_verde, GPIO.HIGH)
        buzz.start(10)
        
        sleep(0.25)
        #GPIO.output(buzzer, GPIO.LOW)
        GPIO.output(led_verde, GPIO.LOW)
        buzz.stop()
        print("id do seu card:")
        print(id)
        print(text)
        sleep(1)
except KeyboardInterrupt:
        print("Keyboard interrupt. Exiting...")
except SystemExit:
    print("exiting")
except:
        print("Erro")
finally:  
        GPIO.cleanup()
    
