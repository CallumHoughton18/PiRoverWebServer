import RPi.GPIO as GPIO
from django.http import HttpResponse

def initGPIO(request,left,right,forward,backward):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(left, GPIO.OUT) 
    GPIO.setup(right, GPIO.OUT) 
    GPIO.setup(forward, GPIO.OUT) 
    GPIO.setup(backward, GPIO.OUT) 
    return HttpResponse('Initializing GPIO pins...')

def forward(request, forward, backward):
    GPIO.setmode(GPIO.BOARD)
    GPIO.output(forward,True)
    GPIO.output(backward,False)
    return HttpResponse('Driving Forwards...')


def backward(request, forward, backward):
    GPIO.setmode(GPIO.BOARD) 
    GPIO.output(forward,False)
    GPIO.output(backward,True)
    return HttpResponse('Driving Backwards...')


def right(request, left, right):
    GPIO.setmode(GPIO.BOARD)
    GPIO.output(left,False)
    GPIO.output(right,True)
    return HttpResponse('Turning Right...')

def left(request, left, right):
    GPIO.setmode(GPIO.BOARD)
    GPIO.output(left,True)
    GPIO.output(right,False)
    return HttpResponse('Turning Left...')

def stopForwardAndBackward(request,forward,backward):
    GPIO.setmode(GPIO.BOARD)
    GPIO.output(forward,False)
    GPIO.output(backward, False)
    return HttpResponse('Forward and Backward GPIOs reset')

def stopLeftAndRight(request,left,right):
    GPIO.setmode(GPIO.BOARD)
    GPIO.output(left,False)
    GPIO.output(right, False)
    return HttpResponse('Left and Right GPIOs reset')

def stopAll(request,forward,backward,left,right):
    GPIO.setmode(GPIO.BOARD)
    GPIO.output(forward,False)
    GPIO.output(backward, False)
    GPIO.output(left, False)
    GPIO.output(right, False)
    return HttpResponse('All GPIO reset')

