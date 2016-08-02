import RPi.GPIO as GPIO


class Pin:
    """ """
    def __init__(self, type, param, mode=GPIO.OUT):
        """
        param:contains pin types characteristics
        type:pin type
        """
        self.param = param
        self.type = type
        self.mode = mode

    def setup(self):
        GPIO.setup(self.param, self.mode)

    def __str__(self):
        return "Pin(%s, %s)" % (self.type, self.param)

class RaspberryPi:
    """ """
    def __init__(self, *pins):
        self.pins = pins
        GPIO.setmode(GPIO.BOARD)
        self.pins[0].setup()
    def __str__(self):
        rv = ""
        for pin in self.pins:
            rv += str(pin) + ", "
        return rv
    
    def __del__(self):
        GPIO.cleanup()

rp = RaspberryPi(Pin("gpio", 4),
                 Pin("gpio", 7),
                 Pin("gpio", 11),
                 Pin("gpio", 13))
print (rp)


