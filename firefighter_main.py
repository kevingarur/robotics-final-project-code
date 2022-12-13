import cap as cap
import numpy as np
import serial
from time import sleep
import cv2
import sys
import subprocess

motorSel = 1

def servoControl(sel, cmd):
    arduino.write(cmd.encode())
    
    if (cmd == '0'):
        # while arduino.inWaiting()==0: pass
        # if  arduino.inWaiting()>0:
            # answer=arduino.readline()
            # print(answer)
            # arduino.flushInput() #remove data after reading
        motorSel+=1
        

if __name__ == '__main__':
    
    print('Running. Press CTRL-C to exit.')
    with serial.Serial("/dev/ttyACM0", 9600, timeout=1) as arduino:
        sleep(0.1) #wait for serial to open
        if arduino.isOpen():
            print("{} connected!".format(arduino.port))
            try:
                cap = cv2.VideoCapture(0)
                ret,frame=cap.read()
                x,y,w,h = cv2.selectROI(frame)
                track_window = (x, y, w, h)
                roi = frame[y:y+h, x:x+w]
                hsv_roi =  cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
                mask = cv2.inRange(hsv_roi, np.array((0., 60.,32.)), np.array((180.,255.,255.)))
                roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])
                cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)
                term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )
                while True:
                       ret, frame = cap.read()
                       if ret == True:
                            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                            dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)
                            ret, track_window = cv2.CamShift(dst, track_window, term_crit)
                            pts = cv2.boxPoints(ret)
                            pts=np.int0(pts)
                            # print(pts)
                            cv2.circle(frame, (pts[0][0],pts[0][1]), 3, (255,0,0), -1)
                            cv2.circle(frame, (pts[1][0],pts[1][1]), 3, (0,255,0), -1)
                            cv2.circle(frame, (pts[2][0],pts[2][1]), 3, (0,0,255), -1)
                            cv2.circle(frame, (pts[3][0],pts[3][1]), 3, (255,255,255), -1)
                            dim = frame.shape
                            c_x = dim[1]/2
                            c_y = dim[0]/2
                            sc_x = abs((pts[0][0] + pts[1][0] + pts[2][0] + pts[3][0]))/4
                            sc_y = abs((pts[0][1] + pts[1][1] + pts[2][1] + pts[3][1]))/4
                            
                            cv2.circle(frame, (int(sc_x),int(sc_y)),4,(0,255,0),-1)
                            text = "x: " + str(sc_x) + ", y: " + str(sc_y)
                            cv2.putText(frame, text, (int(sc_x) - 10, int(sc_y) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                            cmd = ""
                            # if (abs(c_x - sc_x) > abs(c_y - sc_y)):
                            if (motorSel == 1):
                                if (sc_x < c_x):
                                    cmd = "1"
                                    servoControl(motorSel,cmd)
                                    print('Move Left')
                                    # ser.write(bytes("1", 'utf-8'))
                                elif (sc_x > c_x):
                                    cmd = "2"
                                    servoControl(motorSel,cmd)
                                    print('Move Right')
                                    # ser.write(bytes("2", 'utf-8'))
                                    cmd = "2"
                                else:
                                    cmd = "0"
                                    servoControl(motorSel,cmd)
                                    print('Centered')
                                    
                            if (motorSel == 2):
                                if (sc_x < c_x):
                                    print('Move Left')
                                    # ser.write(bytes("1", 'utf-8'))
                                    cmd = "1"
                                else:
                                    print('Move Right')
                                    # ser.write(bytes("2", 'utf-8'))
                                    cmd = "2"

                            img2 = cv2.polylines(frame, [pts], True, 255,2)
                            cv2.imshow('img2',img2)
                                
                            k = cv2.waitKey(30) & 0xff
                            if k == 27:
                                break
                       else:
                           break


            except KeyboardInterrupt:
                print("KeyboardInterrupt has been caught.")

cv2.destroyAllWindows()
