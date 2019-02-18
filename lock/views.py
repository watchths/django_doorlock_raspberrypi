from django.shortcuts import render
import RPi.GPIO as GPIO
import time

servoPIN = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization

# Create your views here.

def turnOn(request) {
    p.ChangeDutyCycle(5)
    time.sleep(0.5)
    return HttpResponse('')
}

def turnOff(request) {
    p.ChangeDutyCycle(12.5)
    time.sleep(0.5)
    Return HttpResponse('')
}