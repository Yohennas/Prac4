#!/usr/bin/python
import RPi.GPIO as GPIO
import Adafruit_MCP3008
import time
from os import system, name
GPIO.setmode(GPIO.BCM)
StartTimer = time.time()

# pin definition
SPICLK = 11
SPIMISO = 9
SPIMOSI = 10
SPICS = 8
switch_1 = 
switch_2 =
switch_3 =
switch_4 =

# pin setup
GPIO.setup(SPIMOSI, GPIO.OUT)
GPIO.setup(SPIMISO, GPIO.IN)
GPIO.setup(SPICLK, GPIO.OUT)
GPIO.setup(SPICS, GPIO.OUT)
GPIO.setup(switch_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(switch_2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(switch_4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
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
    
def Display(channel):
    print(' {0:>4}  {1:>4}  {2:>4}  {3:>4}  {4:>4}  {5:>4}  {6:>4}  {7:>4} '.format(*range(8))) #headings
    for i in range(5):
        print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*past_values[i])) #values
    print(past_values)
    
    
    

GPIO.add_event_detect(switch_1, GPIO.FALLING, callback=FreqChng,
bouncetime=200)    
    
GPIO.add_event_detect(switch_2, GPIO.FALLING, callback=Reset,
bouncetime=200)


GPIO.add_event_detect(switch_4, GPIO.FALLING, callback=Display,
bouncetime=200)   


# global variable
values = [0]*8
past_values = [[0]*8]*5
j=0

freq = 0.5
print(' {0:>4}  {1:>4}  {2:>4}  {3:>4}  {4:>4}  {5:>4}  {6:>4}  {7:>4} '.format(*range(8))) #headings
print('_' * 57)

while True:

    
    if (j==5):
        j=0
        
    for i in range(8):
        
        values[i] = mcp.read_adc(i)
        past_values[j][i]
        
        # delay for a half second
        time.sleep(freq)
    print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*values)) #values
        
    EndTimer = time.time()
    Timer = EndTimer-StartTimer
    Time = time.time()
    print(Time)
    print (Timer)
    print (values)   
    j+=1