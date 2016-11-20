import RPi.GPIO as GPIO
import sys
from time import sleep

def setup(side):
    if side == 'right':
        pins = [16,12,21,20]
    elif side == 'left':
        pins = [26,19,13,6]

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    for pin in pins:
        print ("Setup pins")
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, False)

    path = side + '.txt'
    file_object = open(path, 'r')
    position = int((file_object.read()))
    file_object.close()

def open(side):
    setup(side)

    move = 2070 - position
    endposition = position + move

    if endposition > 4140:
        move = 4140 - position
        endposition = position + move
    elif endposition > 0:
        move = 0 - position
        endposition = position + move

    file_object = open(path, 'w')
    file_object.write(str(endposition))
    file_object.close()

    sequencecount = 8
    sequence = list(range(0, sequencecount))
    counter = 0

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

    #move = abs(move)

    try:
       for x in list(range(0,move)):
            for pin in list(range(0, 4)):
                gpioport = pins[pin]
                if sequence[counter][pin] != 0:
                    print ("Stap: %i GPIO Actief: %i " % (counter, gpioport))
                    GPIO.output(gpioport, True)
                else:
                    GPIO.output(gpioport, False)

            counter += 1

            if (counter == sequencecount):
                counter = 0
            if (counter < 0):
                counter = sequencecount

            sleep(0.05)

       GPIO.cleanup()
       print(move)

    except KeyboardInterrupt:
        GPIO.cleanup()

def close(side):
    setup(side)

    move = 0 - position
    endposition = position + move

    if endposition > 4140:
        move = 4140 - position
        endposition = position + move
    elif endposition > 0:
        move = 0 - position
        endposition = position + move

    file_object = open(path, 'w')
    file_object.write(str(endposition))
    file_object.close()

    sequencecount = 8
    sequence = list(range(0, sequencecount))
    counter = 0

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

    #move = abs(move)

    try:
       for x in list(range(0,move)):
            for pin in list(range(0, 4)):
                gpioport = pins[pin]
                if sequence[counter][pin] != 0:
                    print ("Stap: %i GPIO Actief: %i " % (counter, gpioport))
                    GPIO.output(gpioport, True)
                else:
                    GPIO.output(gpioport, False)

            counter += 1

            if (counter == sequencecount):
                counter = 0
            if (counter < 0):
                counter = sequencecount

            sleep(0.05)

       GPIO.cleanup()
       print(move)

    except KeyboardInterrupt:
        GPIO.cleanup()
