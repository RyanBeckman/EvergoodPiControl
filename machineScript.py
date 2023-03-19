import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)


class Machine:
  def __init__(self, gpio):
    self.GPIOpin = gpio

    #set to no fault
    self.fault = 0

    self.faultLightRed = self.GPIOpin[0]
    self.faultLightYellow = self.GPIOpin[1]
    self.faultLightGreen = self.GPIOpin[2]

    self.machineSwitch1 = self.GPIOpin[3]
    self.machineSwitch2 = self.GPIOpin[4]
    self.machineSwitch3 = self.GPIOpin[5]



    def machineGPIOconfiguration(self):
       #Displays the current GPIO pins of the machine
       print("Red light GPIO pin: ",self.faultLightRed)
       print("Yellow light GPIO pin: ",self.faultLightYellow)
       print("Green light GPIO pin: ",self.faultLightGreen)

       print("\n\nMachine Switch 1: ",self.machineSwitch1)
       print("Machine Switch 2: ",self.machineSwitch2)
       print("Machine Switch 3: ",self.machineSwitch3)

       print("Current Fault Status: ",self.fault)
    

    def setFault(self,status):
    #Set the fault status of the machine

       #Green Light Status
       if(status == 0):
          self.fault =0
       #Yellow Light Status
       if(status ==1):
          self.fault =1
       #Red Light Status
       if(status ==2):
          self.fault =2

    def getFault(self):
    #returns the fault status of the machine
       return(self.fault)

    def faultLight(self):

        #Sets the GPIO Pins as outputs
        GPIO.setup(self.faultLightRed, GPIO.OUT)
        GPIO.setup(self.faultLightYellow, GPIO.OUT)
        GPIO.setup(self.faultLightGreen, GPIO.OUT)

        #Green LED
        if(self.fault==0):
           GPIO.output(self.faultLightGreen, GPIO.HIGH)
           GPIO.output(self.faultLightRed, GPIO.LOW)
           GPIO.output(self.faultLightYellow, GPIO.LOW)
        #Yellow LED
        if(self.fault==1):
           GPIO.output(self.faultLightGreen, GPIO.LOW)
           GPIO.output(self.faultLightRed, GPIO.LOW)
           GPIO.output(self.faultLightYellow, GPIO.HIGH)
        #Red LED
        if(self.fault==2):
           GPIO.output(self.faultLightGreen, GPIO.LOW)
           GPIO.output(self.faultLightRed, GPIO.HIGH)
           GPIO.output(self.faultLightYellow, GPIO.LOW)

        GPIO.cleanup()

    def machineSwitch(self):
        GPIO.setup(self.machineSwitch1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.machineSwitch2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
        GPIO.setup(self.machineSwitch3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        if GPIO.input(self.machineSwitch1) == GPIO.HIGH:
            print("Button 1 was pushed!")
            #yellow
            setFault(1)
        if GPIO.input(self.machineSwitch2) == GPIO.HIGH:
            print("Button 2 was pushed!")
            #yellow
            setFault(1) 
        if GPIO.input(self.machineSwitch3) == GPIO.HIGH:
            print("Button 3 was pushed!")
            #yellow
            setFault(1)  

        GPIO.cleanup()

      


#PASS IN AN ARRAY OF GPIO PINS
#[0] = [redFaultLight pin]
#[1] = [yellowFaultLight pin]
#[2] = [greenFaultLight pin]
#[3] = [machineSwitch1 pin]
#[4] = [machineSwitch2 pin]
#[5] = [machineSwitch3 pin]

machine1 = Machine([1,2,3,4,5,6])
#Prints the current GPIO conficuration
machine1.machineGPIOconfiguration()

