#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
#from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
#from pybricks.media.ev3dev import SoundFile, ImageFile


# Create objects
ev3 = EV3Brick()

#Initialize a motor at part B
test_motor = Motor(Port.B)

# Write your program here.
#Play a sound
ev3.speaker.beep()

# Run the motor up to 500 degrees per second. To a target angle of 90 degrees.
test_motor.run_target(500, 9000)

# Play another beep sound
ev3.speaker.beep(frequency=1000, duration=500)