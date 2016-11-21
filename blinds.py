#!/bin/python

import RPi.GPIO as GPIO
import sys
from time import sleep

def openblinds(side):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    if side == 'right':
    	pins = [16,12,21,20]
    elif side == 'left':
    	pins = [26,19,13,6]

    path = side + '.txt'

    for pin in pins:
        print ("Setup pins")
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, False)

    counter = 0
    sequencecount = 8
    sequence = []
    sequence = list(range(0, sequencecount))

    file_object = open(path, 'r')

    oldposition = int((file_object.read()))
    print(file_object.read())
    file_object.close()

    move = 2070 - oldposition
    newposition = oldposition + move

    if newposition > 4140:
       move = 4140 - oldposition
       newposition = oldposition + move
    elif newposition < 0:
       move = 0 - oldposition
       newposition = oldposition + move

    file_object = open(path, 'w')
    file_object.write(str(newposition))
    file_object.close()

    file_object = open(path, 'r')

    print(file_object.read())
    file_object.close()

    if move > 0:
      sequence[7] = [1,0,0,1]
      sequence[6] = [1,0,0,0]
      sequence[5] = [1,1,0,0]
      sequence[4] = [0,1,0,0]
      sequence[3] = [0,1,1,0]
      sequence[2] = [0,0,1,0]
      sequence[1] = [0,0,1,1]
      sequence[0] = [0,0,0,1]

    elif move < 0:
      sequence[0] = [1,0,0,1]
      sequence[1] = [1,0,0,0]
      sequence[2] = [1,1,0,0]
      sequence[3] = [0,1,0,0]
      sequence[4] = [0,1,1,0]
      sequence[5] = [0,0,1,0]
      sequence[6] = [0,0,1,1]
      sequence[7] = [0,0,0,1]

    move = abs(move)

    #2070 steps

    try:
       for x in list(range(0,move)):
            for pin in list(range(0, 4)):
                xpin = pins[pin]
                if sequence[counter][pin] != 0:
                    print ("Stap: %i GPIO Actief: %i " % (counter, xpin))
                    GPIO.output(xpin, True)
                else:
                    GPIO.output(xpin, False)

            counter += 1

            if (counter==sequencecount): counter = 0
            if (counter<0): counter = sequencecount

            sleep(0.05)

       GPIO.cleanup()
       print(move)

    except KeyboardInterrupt:
        GPIO.cleanup()

def closeblinds(side):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    if side == 'right':
    	pins = [16,12,21,20]
    elif side == 'left':
    	pins = [26,19,13,6]

    path = side + '.txt'

    for pin in pins:
        print ("Setup pins")
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, False)

    counter = 0
    sequencecount = 8
    sequence = []
    sequence = list(range(0, sequencecount))

    file_object = open(path, 'r')

    oldposition = int((file_object.read()))
    print(file_object.read())
    file_object.close()

    move = 0 - oldposition
    newposition = oldposition + move

    if newposition > 4140:
       move = 4140 - oldposition
       newposition = oldposition + move
    elif newposition < 0:
       move = 0 - oldposition
       newposition = oldposition + move

    file_object = open(path, 'w')
    file_object.write(str(newposition))
    file_object.close()

    file_object = open(path, 'r')

    print(file_object.read())
    file_object.close()

    if move > 0:
      sequence[7] = [1,0,0,1]
      sequence[6] = [1,0,0,0]
      sequence[5] = [1,1,0,0]
      sequence[4] = [0,1,0,0]
      sequence[3] = [0,1,1,0]
      sequence[2] = [0,0,1,0]
      sequence[1] = [0,0,1,1]
      sequence[0] = [0,0,0,1]

    elif move < 0:
      sequence[0] = [1,0,0,1]
      sequence[1] = [1,0,0,0]
      sequence[2] = [1,1,0,0]
      sequence[3] = [0,1,0,0]
      sequence[4] = [0,1,1,0]
      sequence[5] = [0,0,1,0]
      sequence[6] = [0,0,1,1]
      sequence[7] = [0,0,0,1]

    move = abs(move)

    #2070 steps

    try:
       for x in list(range(0,move)):
            for pin in list(range(0, 4)):
                xpin = pins[pin]
                if sequence[counter][pin] != 0:
                    print ("Stap: %i GPIO Actief: %i " % (counter, xpin))
                    GPIO.output(xpin, True)
                else:
                    GPIO.output(xpin, False)

            counter += 1

            if (counter==sequencecount): counter = 0
            if (counter<0): counter = sequencecount

            sleep(0.05)

       GPIO.cleanup()
       print(move)

    except KeyboardInterrupt:
        GPIO.cleanup()

def moveblinds(side, degrees):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    if side == 'right':
    	pins = [16,12,21,20]
    elif side == 'left':
    	pins = [26,19,13,6]

    path = side + '.txt'

    for pin in pins:
        print ("Setup pins")
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, False)

    counter = 0
    sequencecount = 8
    sequence = []
    sequence = list(range(0, sequencecount))

    file_object = open(path, 'r')

    oldposition = int((file_object.read()))
    print(file_object.read())
    file_object.close()

    move = 23 * degrees
    newposition = oldposition + move

    if newposition > 4140:
       move = 4140 - oldposition
       newposition = oldposition + move
    elif newposition < 0:
       move = 0 - oldposition
       newposition = oldposition + move

    file_object = open(path, 'w')
    file_object.write(str(newposition))
    file_object.close()

    file_object = open(path, 'r')

    print(file_object.read())
    file_object.close()

    if move > 0:
      sequence[7] = [1,0,0,1]
      sequence[6] = [1,0,0,0]
      sequence[5] = [1,1,0,0]
      sequence[4] = [0,1,0,0]
      sequence[3] = [0,1,1,0]
      sequence[2] = [0,0,1,0]
      sequence[1] = [0,0,1,1]
      sequence[0] = [0,0,0,1]

    elif move < 0:
      sequence[0] = [1,0,0,1]
      sequence[1] = [1,0,0,0]
      sequence[2] = [1,1,0,0]
      sequence[3] = [0,1,0,0]
      sequence[4] = [0,1,1,0]
      sequence[5] = [0,0,1,0]
      sequence[6] = [0,0,1,1]
      sequence[7] = [0,0,0,1]

    move = abs(move)

    #2070 steps

    try:
       for x in list(range(0,move)):
            for pin in list(range(0, 4)):
                xpin = pins[pin]
                if sequence[counter][pin] != 0:
                    print ("Stap: %i GPIO Actief: %i " % (counter, xpin))
                    GPIO.output(xpin, True)
                else:
                    GPIO.output(xpin, False)

            counter += 1

            if (counter==sequencecount): counter = 0
            if (counter<0): counter = sequencecount

            sleep(0.05)

       GPIO.cleanup()
       print(move)

    except KeyboardInterrupt:
        GPIO.cleanup()
