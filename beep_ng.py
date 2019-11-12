# coding: utf-8
import RPi.GPIO as GPIO
import time

def beep(Hz,pwm):
    pwm.start(TIME_DUTY)
    pwm.ChangeFrequency(Hz)
    time.sleep(TIME_DURATION)
    pwm.stop()
    time.sleep(0.025)

def sound_ng(pwm):
    beep(NOTE_C3, pwm)
    beep(NOTE_C3, pwm)
    time.sleep(1)

def sound_ok(pwm):
    beep(NOTE_C4, pwm)
    beep(NOTE_A3, pwm)
    time.sleep(1)

NUM_PIN = 21
TIME_DURATION = 0.3
TIME_DUTY = 40

NOTE_C3 = 262 # Do
NOTE_D3 = 294 # Re
NOTE_E3 = 330 # Mi
NOTE_F3 = 349 # Fa
NOTE_G3 = 392 # So
NOTE_A3 = 440 # La
NOTE_B3 = 494 # Si
NOTE_C4 = 523 # Do

GPIO.setmode(GPIO.BCM)
GPIO.setup(NUM_PIN, GPIO.OUT, initial = GPIO.LOW)

pwm = GPIO.PWM(NUM_PIN, 1)
sound_ng(pwm)
GPIO.cleanup()
