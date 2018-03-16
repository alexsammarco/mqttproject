#code derived from rasberrypiprojects.com
import os 
import sys
import time                                                                                                                         
from gpiozero import LightSensor, Buzzer #import LDR and Buzzer from GPIO pin zero
from time import sleep
from time import strftime
import datetime #Imports the date and time in to file
import paho.mqtt.publish as publish

ldr = LightSensor(4)
buzzer = Buzzer(17)
timestamp = datetime.datetime.now().strftime("%Y%m%d %H:%M:%S")
while True: #continuously checks the light level on LDR
    time.sleep(2) 
    if ldr is not None:
        f=open("lslog.csv", "a") #Creates log file for analytics
        if ldr.value < 0.8: #if LDR value falls below 0.5 buzzer will
            buzzer.beep(4) #how long the buzzer beeps for
            f.write(timestamp+","), #inserts time stamp in to analytics
            f.write("1"+","),       #Insertsmqttproject a one in to the analytics to show buzzer had sounded
            f.write(str(ldr)+"\n"),
            
            publish.single("mqtt-events", ldr.value, hostname="test.mosquitto.org")
        else:
            buzzer.off()
            f.write(timestamp +","),
            f.write("0"+","),     #Inserts 0 to show buzzer has not sounded at specified time
            f.write(str(ldr)+"\n"),
            

        f.close()
        time.sleep(2) 
    else:
        print('Failed to get reading.') 
        


GPIO.cleanup()
