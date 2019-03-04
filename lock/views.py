from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
import RPi.GPIO as GPIO
import time
from django.db.models import Count

servoPIN = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization

# Create your views here.

def index(request):
    return render_to_response('index.html', {'status':"LOCKED"})

def turnOn(request):
    p.ChangeDutyCycle(5)
    time.sleep(0.5)
#    p.stop()
#    GPIO.cleanup()
    return render_to_response('index.html', {'status':"LOCKED"})


def turnOff(request):
    status = 'unlocked'
    p.ChangeDutyCycle(12.5)
    time.sleep(0.5)
#    p.stop()
#    GPIO.cleanup()
    return render_to_response('index.html', {'status':"UNLOCKED"})

#def turnOn(request):
#    return render_to_response('locked.html')
#
#def turnOff(request):
#    return render_to_response('unlocked.html')

def foo(request):
    return render_to_response('index.html')