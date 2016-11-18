#!/bin/python

import RPi.GPIO as GPIO
import sys
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

StepPins = [26,19,13,6]

for pin in StepPins:
    print "Setup pins"
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin, False)

StepCounter = 0
StepCount = 8
Seq = []
Seq = range(0, StepCount)

input = sys.argv[1]

file_object = open('/usr/src/links.txt', 'r')
Steps = int((file_object.read()))
print(file_object.read())
file_object.close()

if input == 'open':
   StepsShift = 2070 - Steps
   ResultSteps = Steps + StepsShift
elif input == 'close':
   StepsShift = 0 - Steps
   ResultSteps = Steps + StepsShift
else:
   input = int(input)
   DegreeShift = input
   StepsShift = 23 * DegreeShift
   ResultSteps = Steps + StepsShift

if ResultSteps > 4140:
   StepsShift = 4140 - Steps
   ResultSteps = Steps + StepsShift 

if ResultSteps < 0:
   StepsShift = 0 - Steps
   ResultSteps = Steps + StepsShift

file_object = open('/usr/src/links.txt', 'w')
file_object.write(str(ResultSteps))
file_object.close()

file_object = open('/usr/src/links.txt', 'r')
print(file_object.read())
file_object.close()

if StepsShift > 0:
  Seq[7] = [1,0,0,1]
  Seq[6] = [1,0,0,0]
  Seq[5] = [1,1,0,0]
  Seq[4] = [0,1,0,0]
  Seq[3] = [0,1,1,0]
  Seq[2] = [0,0,1,0]
  Seq[1] = [0,0,1,1]
  Seq[0] = [0,0,0,1]

elif StepsShift < 0: 
  Seq[0] = [1,0,0,1]
  Seq[1] = [1,0,0,0]
  Seq[2] = [1,1,0,0]
  Seq[3] = [0,1,0,0]
  Seq[4] = [0,1,1,0]
  Seq[5] = [0,0,1,0]
  Seq[6] = [0,0,1,1]
  Seq[7] = [0,0,0,1]

StepsShift = abs(StepsShift)

#2070 steps

try:
   for x in range (0,StepsShift):
        for pin in range(0, 4):
            xpin = StepPins[pin]
            if Seq[StepCounter][pin] != 0:
                print "Stap: %i GPIO Actief: %i" %(StepCounter,xpin)
                GPIO.output(xpin, True)
            else:
                GPIO.output(xpin, False)

        StepCounter += 1

        if (StepCounter==StepCount): StepCounter = 0
        if (StepCounter<0): StepCounter = StepCount

        sleep(0.05)

   GPIO.cleanup()
   print(StepsShift)

except KeyboardInterrupt:
    GPIO.cleanup()
