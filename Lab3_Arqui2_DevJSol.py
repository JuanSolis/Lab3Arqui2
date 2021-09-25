import RPI.GPIO as GPIO
import time

contador=0
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(8,GPIO.IN)
GPIO.setup(1,GPIO.OUT) #a
GPIO.setup(2,GPIO.OUT) #b
GPIO.setup(3,GPIO.OUT) #c
GPIO.setup(4,GPIO.OUT) #d
GPIO.setup(5,GPIO.OUT) #e
GPIO.setup(6,GPIO.OUT) #f
GPIO.setup(7,GPIO.OUT) #g

def mostrar(num):
    if num==0:
        GPIO.output(1,True)
        GPIO.output(2,True)
        GPIO.output(3,True)
        GPIO.output(4,True)
        GPIO.output(5,True)
        GPIO.output(6,True)
        GPIO.output(7,False)
    elif num==1:
        GPIO.output(1,False)
        GPIO.output(2,True)
        GPIO.output(3,True)
        GPIO.output(4,False)
        GPIO.output(5,False)
        GPIO.output(6,False)
        GPIO.output(7,False)
    elif num==2:
        GPIO.output(1,True)
        GPIO.output(2,True)
        GPIO.output(3,False)
        GPIO.output(4,True)
        GPIO.output(5,True)
        GPIO.output(6,False)
        GPIO.output(7,True)
    elif num==3:
        GPIO.output(1,True)
        GPIO.output(2,True)
        GPIO.output(3,True)
        GPIO.output(4,True)
        GPIO.output(5,False)
        GPIO.output(6,False)
        GPIO.output(7,True)
    elif num==4:
        GPIO.output(1,False)
        GPIO.output(2,True)
        GPIO.output(3,True)
        GPIO.output(4,False)
        GPIO.output(5,False)
        GPIO.output(6,True)
        GPIO.output(7,True)
    elif num==5:
        GPIO.output(1,True)
        GPIO.output(2,False)
        GPIO.output(3,True)
        GPIO.output(4,True)
        GPIO.output(5,False)
        GPIO.output(6,True)
        GPIO.output(7,True)
    elif num==6:
        GPIO.output(1,True)
        GPIO.output(2,False)
        GPIO.output(3,True)
        GPIO.output(4,True)
        GPIO.output(5,True)
        GPIO.output(6,True)
        GPIO.output(7,True)
    elif num==7:
        GPIO.output(1,True)
        GPIO.output(2,True)
        GPIO.output(3,True)
        GPIO.output(4,False)
        GPIO.output(5,False)
        GPIO.output(6,False)
        GPIO.output(7,False)
    elif num==8:
        GPIO.output(1,True)
        GPIO.output(2,True)
        GPIO.output(3,True)
        GPIO.output(4,True)
        GPIO.output(5,True)
        GPIO.output(6,True)
        GPIO.output(7,True)
    elif num==9:
        GPIO.output(1,True)
        GPIO.output(2,True)
        GPIO.output(3,True)
        GPIO.output(4,True)
        GPIO.output(5,False)
        GPIO.output(6,True)
        GPIO.output(7,True)
        
mostrar(0)
while True:        
    if cont<10:
        if GPIO.input(8):
            cont=cont+1
            mostrar(cont)
    else:
        cont = 0
GPIO.cleanup()