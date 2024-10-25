import RPi.GPIO as GPIO
import pygame

# motor setup
 
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
 
m1a = 17
m1b = 27
m1 = 22

m2a = 23
m2b = 24
m2 = 25

GPIO.setup(m1a,GPIO.OUT)
GPIO.setup(m1b,GPIO.OUT)
GPIO.setup(m1,GPIO.OUT)
 
GPIO.setup(m2a,GPIO.OUT)
GPIO.setup(m2b,GPIO.OUT)
GPIO.setup(m2,GPIO.OUT)

#joystick setup

pygame.init()
joystick_count = pygame.joystick.get_count()

for i in range(joystick_count):
    joystick = pygame.joystick.Joystick(i)
    joystick.init()

#joystick input values converted to electrical output

while True:
    pygame.event.pump()
    right = joystick.get_axis(1)
    left = joystick.get_axis(4)
    
    print(right)
    print(left)

    #forward
    if right > 0.2 and left > 0.2:
        while right > 0.2 and left > 0.2:
            GPIO.output(m1a, GPIO.HIGH)
            GPIO.output(m1b, GPIO.LOW)
            GPIO.output(m1, GPIO.HIGH)

            GPIO.output(m2a, GPIO.HIGH)
            GPIO.output(m2b, GPIO.LOW)
            GPIO.output(m2, GPIO.HIGH)

            pygame.event.pump()

            right = joystick.get_axis(1)
            left = joystick.get_axis(4)
    
        GPIO.output(m1, GPIO.LOW)
        GPIO.output(m2, GPIO.LOW)
    
    pygame.event.pump()
    print(right)
    print(left)

    #backward
    if right < -0.2 and left < -0.2:
        while right < -0.2 and left < -0.2:
            GPIO.output(m1a, GPIO.LOW)
            GPIO.output(m1b, GPIO.HIGH)
            GPIO.output(m1, GPIO.HIGH)

            GPIO.output(m2a, GPIO.LOW)
            GPIO.output(m2b, GPIO.HIGH)
            GPIO.output(m2, GPIO.HIGH)

            pygame.event.pump()

            right = joystick.get_axis(1)
            left = joystick.get_axis(4)

        GPIO.output(m1, GPIO.LOW)
        GPIO.output(m2, GPIO.LOW)
    
    pygame.event.pump()
    print(right)
    print(left)

    #clockwise about origin
    if left > 0.2 and right < -0.2:
        while left > 0.2 and right < -0.2:

            GPIO.output(m1a, GPIO.LOW)
            GPIO.output(m1b, GPIO.HIGH)
            GPIO.output(m1, GPIO.HIGH)

            GPIO.output(m2a, GPIO.HIGH)
            GPIO.output(m2b, GPIO.LOW)
            GPIO.output(m2, GPIO.HIGH)

            pygame.event.pump()

            right = joystick.get_axis(1)
            left = joystick.get_axis(4)

        GPIO.output(m1, GPIO.LOW)
        GPIO.output(m2, GPIO.LOW)

    pygame.event.pump()
    print(right)
    print(left)

    #counterclockwise about origin

    if left < -0.2 and right > 0.2:
        while left < -0.2 and right > 0.2:

            GPIO.output(m1a, GPIO.HIGH)
            GPIO.output(m1b, GPIO.LOW)
            GPIO.output(m1, GPIO.HIGH)

            GPIO.output(m2a, GPIO.LOW)
            GPIO.output(m2b, GPIO.HIGH)
            GPIO.output(m2, GPIO.HIGH)

            pygame.event.pump()

            right = joystick.get_axis(1)
            left = joystick.get_axis(4)


        GPIO.output(m1, GPIO.LOW)
        GPIO.output(m2, GPIO.LOW)

    pygame.event.pump()
    print(right)
    print(left)


    #turn right forward
    right = joystick.get_axis(4)
    left = joystick.get_axis(1)

    if left < -0.2 and -0.2 < right < 0.2:
        while left < -0.2 and -0.2 < right < 0.2:

            GPIO.output(m1a, GPIO.LOW)
            GPIO.output(m1b, GPIO.HIGH)
            GPIO.output(m1, GPIO.HIGH)

            pygame.event.pump()

            right = joystick.get_axis(4)
            left = joystick.get_axis(1)

        GPIO.output(m1, GPIO.LOW)
        GPIO.output(m2, GPIO.LOW)

    pygame.event.pump()
    print(right)
    print(left)

    #turn left forward

    if right < -0.2 and -0.2 < left < 0.2:
        while right < -0.2 and -0.2 < left < 0.2:
        
            GPIO.output(m2a, GPIO.LOW)
            GPIO.output(m2b, GPIO.HIGH)
            GPIO.output(m2, GPIO.HIGH)

            pygame.event.pump()

            right = joystick.get_axis(4)
            left = joystick.get_axis(1)

        GPIO.output(m1, GPIO.LOW)
        GPIO.output(m2, GPIO.LOW)

    pygame.event.pump()
    print(right)
    print(left)

    #turn right backward
    
    if left > 0.2 and right == 0.0:
        while left > 0.2 and right == 0.0:

            GPIO.output(m1a, GPIO.HIGH)
            GPIO.output(m1b, GPIO.LOW)
            GPIO.output(m1, GPIO.HIGH)
            
            pygame.event.pump()

            right = joystick.get_axis(4)
            left = joystick.get_axis(1)

        GPIO.output(m1, GPIO.LOW)
        GPIO.output(m2, GPIO.LOW)

    pygame.event.pump()
    print(right)
    print(left)

    #turn left backward

    if right > 0.2 and left == 0.0:
        while right > 0.2 and left == 0.0:

            GPIO.output(m2a, GPIO.HIGH)
            GPIO.output(m2b, GPIO.LOW)
            GPIO.output(m2, GPIO.HIGH)

            pygame.event.pump()

            right = joystick.get_axis(4)
            left = joystick.get_axis(1)

        GPIO.output(m1, GPIO.LOW)
        GPIO.output(m2, GPIO.LOW)
    
    pygame.event.pump()
    print(right)
    print(left)
    
    if joystick.get_button(0):
        print("Quitting the program")
        GPIO.cleanup()
        break
