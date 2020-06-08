import _thread
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO_TRIGGER = 4
GPIO_ECHO = 17
GPIO_BUZZER = 21
GPIO_RED_LED = 20
GPIO_GREEN_LED = 16

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(GPIO_BUZZER, GPIO.OUT)
GPIO.setup(GPIO_RED_LED, GPIO.OUT)
GPIO.setup(GPIO_GREEN_LED, GPIO.OUT)

GPIO.output(GPIO_TRIGGER, False)
GPIO.output(GPIO_BUZZER, False)
GPIO.output(GPIO_RED_LED, False)
GPIO.output(GPIO_GREEN_LED, True)

keepRunning = True
distance = 0

def measureDistance():
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    start = time.time()
    stop = time.time()
    while GPIO.input(GPIO_ECHO) == 0:
        start = time.time()

    while GPIO.input(GPIO_ECHO) == 1:
        stop = time.time()

    elapsed = stop - start
    distance = elapsed * 17150
    return distance

def playSound(threadName, delay):
    keepRunning
    distance
    while keepRunning:
        if distance <= 30:
            GPIO.output(GPIO_BUZZER, True)
            time.sleep(0.01 * distance)
            GPIO.output(GPIO_GREEN_LED, False)
            GPIO.output(GPIO_RED_LED, True)
            
            GPIO.output(GPIO_BUZZER, False)
            time.sleep(0.05 * distance)
            GPIO.output(GPIO_RED_LED, False)
            GPIO.output(GPIO_GREEN_LED, True)

        time.sleep(delay)

try:
    distance = measureDistance()
    _thread.start_new_thread(playSound, ("BuzzerThread1", 0.01))
    while True:
        print (distance)
        time.sleep(0.1)
        distance = measureDistance()
except:
    keepRunning = False
    time.sleep(1)
    GPIO.cleanup()

