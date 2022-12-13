from tkinter import *
#Thinter in python 2
import RPi.GPIO as io
import time
import subprocess


io.setmode(io.BOARD)
io.setup(11,io.OUT)
p1=io.PWM(11,50)
p1.start(90)
time.sleep(2)
io.setup(13,io.OUT)
p2=io.PWM(13,50)
p2.start(90)
time.sleep(2)


def test_1():
    global dc
    deg1 = 120.0
    deg2 = 60.0
    
    # Center Servos
    # deg_p1 = 160.0
    # deg_p2 = 120.0
    
    # dc = 0.056*deg_p1 + 2.5
    # p1.ChangeDutyCycle(dc)
    # dc = 0.056*deg_p2 + 2.5
    # p2.ChangeDutyCycle(dc)

    for y in range(2):
        dc = 0.056*deg1 + 2.5
        p2.ChangeDutyCycle(dc)
        print(deg1, dc)
        time.sleep(1)
        
        dc = 0.056*deg2 + 2.5
        p2.ChangeDutyCycle(dc)
        print(deg2, dc)
        time.sleep(1)

    for x in range(2):
        dc = 0.056*deg1 + 2.5
        p1.ChangeDutyCycle(dc)
        print(deg1, dc)
        time.sleep(1)
        
        dc = 0.056*deg2 + 2.5
        p1.ChangeDutyCycle(dc)
        print(deg2, dc)
        time.sleep(1)
        
        
        
    subprocess.call("speaker-test -t sine -f 440 -c 2 -s 1",shell = True)

test_1()






# root = Tk()
# Label(root, text="Angle").grid(row=0)
# e1 = Entry(root)
# e1.grid(row=0, column=1)

# def cal():
    # global dc
    # deg1 =e1.get()
    # deg = abs(float(deg1))
    # dc = 0.056*deg + 2.5
    # p.ChangeDutyCycle(dc)
    # print(deg, dc)
   
# b1= Button(root, text = "Enter",bg="pink", command =cal)
# b1.grid(row=2, column=1)
# b3 = Button(root, text='Quit', bg= "cyan", command=root.quit)
# b3.grid(row=2, column=3)
# root.mainloop()
