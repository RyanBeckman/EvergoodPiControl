import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM)


class StepperCtrl:
    """
    A class for controlling stepper motors
    """
    def __init__(self, ena, dir, pul):
        GPIO.setup(ena, GPIO.OUT)
        GPIO.setup(dir, GPIO.OUT)
        GPIO.setup(pul, GPIO.OUT)
        self.ena = ena
        self.dir = dir
        self.pul = pul

    def down(self, dur, delay):
        GPIO.output(self.ena, GPIO.HIGH)
        time.sleep(0.5) #ena time min is 0.2s
        GPIO.output(self.dir, GPIO.LOW)
        for i in range(dur):
            GPIO.output(self.pul, GPIO.HIGH)
            time.sleep(delay)
            GPIO.output(self.pul, GPIO.LOW)
            time.sleep(delay)

        GPIO.output(self.ena, GPIO.LOW)
        time.sleep(0.5)

    def up(self, dur, delay):
        GPIO.output(self.ena, GPIO.HIGH)
        time.sleep(0.5) #ena time min is 0.2s
        GPIO.output(self.dir, GPIO.HIGH)
        for i in range(dur):
            GPIO.output(self.pul, GPIO.HIGH)
            time.sleep(delay)
            GPIO.output(self.pul, GPIO.LOW)
            time.sleep(delay)

        GPIO.output(self.ena, GPIO.LOW)
        time.sleep(0.5)


class MachineSwitch:
    """
    A class for input switches (closed is high, open is low)
    """
    def __init__(self, pin):
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        self.pin = pin

    def getState(self):
        return int(GPIO.input(self.pin) == GPIO.HIGH)


class MachineIR:
    """
    A class for IR beams (broken is low, connected is high)
    """
    def __init__(self, pin):
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        self.pin = pin


    def getState(self):
        return int(GPIO.input(self.pin) != GPIO.HIGH)


class Machine:
    """
    A class for interfacing with the GPIO pins controlling the filling machine
    """
    def __init__(self, gpio):

        #set to no fault
        self.fault = 0

        self.faultLightRed = gpio["LIGHT"]["RED"]
        self.faultLightYellow = gpio["LIGHT"]["YELLOW"]
        self.faultLightGreen = gpio["LIGHT"]["GREEN"]

        self.n2sw = MachineSwitch(gpio["SWITCHES"]["N2_SW"])
        self.wine1sw = MachineSwitch(gpio["SWITCHES"]["WINE1_SW"])
        self.wine2sw = MachineSwitch(gpio["SWITCHES"]["WINE2_SW"])
        self.cappingsw = MachineSwitch(gpio["SWITCHES"]["CAPPING_SW"])

        self.irLeft = MachineIR(gpio["IR_BEAMS"]["LEFT"])
        self.irMid = MachineIR(gpio["IR_BEAMS"]["MID"])
        self.irRight = MachineIR(gpio["IR_BEAMS"]["RIGHT"])

        self.n2 = gpio["N2"]
        self.wine1 = gpio["WINE1"]
        self.wine2 = gpio["WINE2"]
        self.indexer = gpio["INDEXER"]

        self.n2Motor = StepperCtrl(gpio["N2_STEPPER"]["ENA"],
                                   gpio["N2_STEPPER"]["DIR"],
                                   gpio["N2_STEPPER"]["PUL"])

        self.wineMotor = StepperCtrl(gpio["WINE_STEPPER"]["ENA"],
                                     gpio["WINE_STEPPER"]["DIR"],
                                     gpio["WINE_STEPPER"]["PUL"])

        self.cappingMotor = StepperCtrl(gpio["CAPPING_STEPPER"]["ENA"],
                                        gpio["CAPPING_STEPPER"]["DIR"],
                                        gpio["CAPPING_STEPPER"]["PUL"])

        self.motorshutoff = gpio["MOTOR_PWR"]

        # Sets the GPIO Pins as outputs
        GPIO.setup(self.faultLightRed, GPIO.OUT)
        GPIO.setup(self.faultLightYellow, GPIO.OUT)
        GPIO.setup(self.faultLightGreen, GPIO.OUT)

        GPIO.setup(self.n2, GPIO.OUT)
        GPIO.setup(self.wine1, GPIO.OUT)
        GPIO.setup(self.wine2, GPIO.OUT)
        GPIO.setup(self.indexer, GPIO.OUT)
        GPIO.setup(self.motorshutoff, GPIO.OUT)

    def puffN2(self, delay):
        GPIO.output(self.n2, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(self.n2, GPIO.LOW)

    def openWine1(self):
        GPIO.output(self.wine1, GPIO.HIGH)

    def closeWine1(self):
        GPIO.output(self.wine1, GPIO.LOW)

    def openWine2(self):
        GPIO.output(self.wine2, GPIO.HIGH)

    def closeWine2(self):
        GPIO.output(self.wine2, GPIO.LOW)

    def moveIndexer(self, delay):
        GPIO.output(self.indexer, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(self.indexer, GPIO.LOW)

    def shutoff(self):
        GPIO.output(self.motorshutoff, GPIO.HIGH)
        self.closeWine1()
        self.closeWine2()

    def setFault(self, status):
        #Set the fault status of the machine
        self.fault = status
        self.faultLight()

    def getFault(self):
        #returns the fault status of the machine
        return(self.fault)

    def faultLight(self):
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

    def cleanUp(self):
        GPIO.cleanup()


