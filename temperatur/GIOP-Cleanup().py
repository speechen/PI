# laueft nicht!!!!
""" https://schmidt-feldberg.de/raspberry-pi-shell-script-zum-steuern-der-gpios/ """
""" am not so fluent in programming for the Rpi, which I only do in my very few spare time, so I would like some confirmation.

If I put GPIO.cleanup() this cleansups and puts to input all used GPIOs , right?

I ask this very simple question because in the docs of a sensor (ultrasonic) I have there is this code for us to use:"""

def reading(sensor):
    import time
    import RPI.GPIO as GPIO
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    TRIG=11
    ECHO= 13
    if sensor == 0:
        GPIO.setup(TRIG,GPIO.OUT)
        GPIO.setup(ECHO,GPIO.IN)
        time.sleep(0.3)
        GPIO.output(TRIG,True)
        time.sleep(0.00001)
        GPIO.output(TRIG,False)
        while GPIO.input(ECHO) ==0:
            signaloff=time.time()
        while GPIO.input(ECHO) ==1:
            signalon=time.time()
        timepassed=signalon-signaloff
        distance=timepassed*170000
        return distance
        GPIO.cleanup()
    else:
#        print"Incorrect usonic() function variable"

#print reading(0)

# Oben gehoert noch zum Programm


"""First, I find the implementation of this function not that good. With the imports and the setmode inside the function.
But what it bothers me most is that the function includes cleanup

I am planning to use other GPIOs for other sensors as well, But does using the above function once means that it is
going to interfere with my own other sensors? I guess it will and that the implementation of this function is wrong.

Any thoughts on this?

4

Yes, the cleanup() function sets to be inputs all the GPIO used by a RPi.GPIO script.
It doesn't effect other RPi.GPIO scripts running at the same time."""