#!/usr/bin/python
import RPi.GPIO as GPIO
import Adafruit_MCP3008
import time
from os import system, name
GPIO.setmode(GPIO.BCM)
StartTimer = time.time()
boolean stop=false

# pin definition
SPICLK = 11
SPIMISO = 9
SPIMOSI = 10
SPICS = 8
switch_1 = 16
switch_2 = 20
switch_3 = 21
switch_4 = 19

# pin setup
GPIO.setup(SPIMOSI, GPIO.OUT)
GPIO.setup(SPIMISO, GPIO.IN)
GPIO.setup(SPICLK, GPIO.OUT)
GPIO.setup(SPICS, GPIO.OUT)
GPIO.setup(switch_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(switch_2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(switch_4, GPIO.IN, pull_up_down=GPIO.PUD.UP)
GPIO.setup(switch_3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

mcp = Adafruit_MCP3008.MCP3008(clk=SPICLK, cs=SPICS, mosi=SPIMOSI,
miso=SPIMISO)

def FreqChng(channel):    
    if (freq==2):
        freq=0.5
    else:
        freq*=2

def Reset(channel):
    EndTimer = 0
    _ = system('clear')

def Stop(channel):
	if stop=false:
		stop=true
	else if stop=true:
		stop=false
	    
GPIO.add_event_detect(switch_1, GPIO.FALLING, callback=FreqChng,
bouncetime=200)    
    
GPIO.add_event_detect(switch_2, GPIO.FALLING, callback=Reset,
bouncetime=200)

GPIO.add_event_detect(switch_3, GPIO.RISING, callback=Stop, bouncetime=200)

# global variable
values = [0]*8

freq = 0.5

while (stop=false):    
    for i in range(8):
        
        values[i] = mcp.read_adc(i)
	
    EndTimer = time.time()
    Timer = EndTimer-StartTimer
    Time = time.time()
    print(Time ' ' Timer ' ' values)
    time.sleep(freq)	   
    
        
        


