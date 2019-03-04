from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
import RPi.GPIO as GPIO
import time
from django.db.models import Count

#Setting metode penomeran menjadi standar Broadcom 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)

# Create your views here.

def index(request):
    return render_to_response('index.html', {'status':"LOCKED"})

def turnOn(request):
    GPIO.output(17, GPIO.LOW)
#    p.stop()
#    GPIO.cleanup()
    return render_to_response('index.html', {'status':"LOCKED"})


def turnOff(request):
    status = 'unlocked'
    GPIO.output(17, GPIO.HIGH)
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