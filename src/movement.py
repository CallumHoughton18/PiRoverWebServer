import curses
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT) #left
GPIO.setup(13, GPIO.OUT) #right
GPIO.setup(16, GPIO.OUT)#reverse
GPIO.setup(18, GPIO.OUT) #forward

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

try:
    while True:
        char = screen.getch()
        if char == ord('q'):
            GPIO.output(18,False)
            GPIO.output(16,False)
            GPIO.output(11,False)
            GPIO.output(13,False)
            break
        elif char == curses.KEY_UP:
            GPIO.output(18,True)
            GPIO.output(16,False)
        elif char == curses.KEY_DOWN:
            GPIO.output(18,False)
            GPIO.output(16,True)
        elif char == curses.KEY_RIGHT:
            GPIO.output(18,False)
            GPIO.output(16,False)
            GPIO.output(11,False)
            GPIO.output(13,True)
        elif char == curses.KEY_LEFT:
            GPIO.output(18,False)
            GPIO.output(16,False)
            GPIO.output(11,True)
            GPIO.output(13,False)

finally:
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()
