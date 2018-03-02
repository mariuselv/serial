#!/usr/bin/python3
 
# adapted from https://github.com/recantha/EduKit3-RC-Keyboard/blob/master/rc_keyboard.py
 
import sys, termios, tty, os, time, serial

ser = serial.Serial('/dev/cu.usbserial-A702NVWD', 57600)
 
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
 
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch
 
button_delay = 0.2

print("Running Python-Arduino serial if.\nHit q to exit.")

while True and ser.is_open:
  #char = getch()

  #if (char == "q"):
  #  print("Exit!")
  #  ser.close()
  #  exit(0)
  
  print("Data:" + ser.readline())
  #ser.write(b'5')


print("done")


