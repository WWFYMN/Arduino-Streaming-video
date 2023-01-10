import cv2
import numpy as np
import time
FILE="BA.mp4"
ADD="0b"
VID=[]
VIDAR=[]
def ArrayToCustomChars(ar):
    strs = ["" for x in range(0,16)] # Make an array of empty strings
    vars=[]
    
    for row in range(0,16):
        
        for col in range(0,16):
            strs[row]=strs[row]+str(int(ar[row][col])) #collect the data in one array of strings
    for i in range(0,8):
        vars.append([])
        #row 1
        if i == 0:
            a=[]
            for n in range(0,8):
                a.append(ADD+strs[n][:5])
            
            vars[i]=a
        if i == 1:
            a=[]
            for n in range(0,8):
                a.append(ADD+strs[n][5:10])
            
            vars[i]=a
        if i == 2:
            a=[]
            for n in range(0,8):
                a.append(ADD+strs[n][10:15])
            
            vars[i]=a
        if i == 3:
            a=[]
            for n in range(0,8):
                a.append(ADD+strs[n][15]+"0000")
            
            vars[i]=a
        #row 2
        if i == 4:
            a=[]
            for n in range(8,16):
                a.append(ADD+strs[n][:5])
            
            vars[i]=a
        if i == 5:
            a=[]
            for n in range(8,16):
                a.append(ADD+strs[n][5:10])
            
            vars[i]=a
        if i == 6:
            a=[]
            for n in range(8,16):
                a.append(ADD+strs[n][10:15])
            
            vars[i]=a
        if i == 7:
            a=[]
            for n in range(8,16):
                a.append(ADD+strs[n][15]+"0000")
            
            vars[i]=a
        #make the data into an array of 8 variables to be sent to an arduino


    return vars
cap=cv2.VideoCapture(FILE) #read video

def video_to_16():
    while(cap.isOpened()):
        cp, frame=cap.read() # read a frame from video
        try:
            
            frame = cv2.resize(frame,(16,16),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)# convert a frame into grayscale
        except:
            break

        
        

        frame = cv2.resize(frame,(16,16),fx=0,fy=0, interpolation = cv2.INTER_CUBIC) #convert a frame to 16X16 resolution
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # convert to grayscale again
        (thresh, frame) = cv2.threshold(frame, 127, 1, cv2.THRESH_BINARY) #convert into black and white

        VID.append(frame)
video_to_16()
def Pic_to16(frame): #this works simmilarly to the video function
    try:
        black=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    except:
        pass
        
        
    (thresh, BAWI) = cv2.threshold(black, 127, 1, cv2.THRESH_BINARY)
        
    frame = cv2.resize(frame,(16,16),fx=0,fy=0, interpolation = cv2.INTER_CUBIC) 
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    (thresh, frame) = cv2.threshold(frame, 127, 1, cv2.THRESH_BINARY)
    return frame

for i in range(0,len(VID)):
    VIDAR.append(ArrayToCustomChars(VID[i].tolist())) # run the function for every frame of a video


def toL2(L):
    
    #return ('[' +', '.join(map(str, L))+"]")
    return (', '.join(map(str, L)))
def toL(L):
    
    return ('[' +', '.join(map(toL2, L)) + ']')
    
a=('[' + ', '.join(map(toL, VIDAR)) + ']')# convert into a big file of a list
file = open("VID.py","w") #write it
file.write("VID="+a+";")
file.close()
print(len(a))



