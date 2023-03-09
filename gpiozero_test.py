from gpiozero import Motor
import pygame

# motor setup
rightWheels = Motor(17, 27)
leftWheels = Motor(23, 24)


# joystick setup
pygame.init()
joystick_count = pygame.joystick.get_count()

for i in range(joystick_count):
    joystick = pygame.joystick.Joystick(i)
    joystick.init()


# functions

def setRightSpeed(speed):
    if speed>0:
        rightWheels.forward(speed)
    if speed<0:
        rightWheels.forward(abs(speed))

def setLeftSpeed(speed):
    if speed>0:
        leftWheels.forward(speed)
    if speed<0:
        leftWheels.forward(abs(speed))


# joystick input values converted to electrical output

while True:
    pygame.event.pump()

    # quit
    if joystick.get_button(0):
        rightWheels.forward(0)
        leftWheels.forward(0)
        print("quit program")
        break

    # speed values
    rightJoyY = joystick.get_axis(4)
    leftJoyY = joystick.get_axis(1)
    
    print("rightJoyY:" + rightJoyY)
    print("leftJoyY:" + leftJoyY)

    setRightSpeed(rightJoyY)
    setLeftSpeed(leftJoyY)



print("program was quit")
