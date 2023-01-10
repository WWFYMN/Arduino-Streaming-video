import serial
import time
import VID
TIME=0.033
SKIP=0
arduino = serial.Serial('/dev/ttyUSB0', baudrate=921600, timeout=3) #make a serial connection


print("Started")
lido = arduino.readline()
time.sleep(2)#wait for the arduino to restart
print("Start Video for syncing")
time.sleep(0.1)
for i in range(len(VID.VID)): #loop through every element of the vid list and sen it to arduino
    arduino.write(VID.VID[i+SKIP][0:63])
    
    
    #print(VID.VID[i+SKIP])
    time.sleep(TIME)
    