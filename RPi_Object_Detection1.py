import cap as cap
import numpy as np
import serial
from time import sleep
import cv2
import sys
import subprocess
#from matplotlib import pyplot as plt


def list_ports():
    """
    Test the ports and returns a tuple with the available ports and the ones that are working.
    """
    non_working_ports = []
    dev_port = 0
    working_ports = []
    available_ports = []
    while len(non_working_ports) < 6: # if there are more than 5 non working ports stop the testing. 
        camera = cv2.VideoCapture(dev_port)
        if not camera.isOpened():
            non_working_ports.append(dev_port)
            print("Port %s is not working." %dev_port)
        else:
            is_reading, img = camera.read()
            w = camera.get(3)
            h = camera.get(4)
            if is_reading:
                print("Port %s is working and reads images (%s x %s)" %(dev_port,h,w))
                working_ports.append(dev_port)
            else:
                print("Port %s for camera ( %s x %s) is present but does not reads." %(dev_port,h,w))
                available_ports.append(dev_port)
        dev_port +=1
    return available_ports,working_ports,non_working_ports
    
# available_ports,workingports,non_working_ports = list_ports()
# print(available_ports," ",workingports," ",non_working_ports)





# cap = cv2.VideoCapture(0)

# # Check if the webcam is opened correctly
# if not cap.isOpened():
    # raise IOError("Cannot open webcam")

# while True:
    # ret, frame = cap.read()
    # frame = cv2.resize(frame, None, fx=2, fy=2, interpolation=cv2.INTER_AREA)
    # cv2.imshow('Input', frame)

    # c = cv2.waitKey(1)
    # if c == 27:
        # break

# cap.release()
# cv2.destroyAllWindows()






# def edge_detection_video():
    # cap = cv2.VideoCapture(0)
    # # VideoWriter for saving the video
    # fourcc = cv2.VideoWriter_fourcc(*'MP4V')
    # out = cv2.VideoWriter('output.mp4', fourcc, 30.0, (int(cap.get(3)), int(cap.get(4))), isColor=False)
    
    # while cap.isOpened():
        # (ret, frame) = cap.read()
        # if ret == True:
            # frame = cv2.GaussianBlur(frame, (3, 3), 0)
            # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # edge = cv2.Canny(frame, 50, 100)
            # out.write(edge)
            # cv2.imshow('Edge detection', edge)
        # else:
            # break

        # if cv2.waitKey(10) & 0xFF == ord('q'):
            # break

    # cap.release()
    # out.release()
    # cv2.destroyAllWindows()

# edge_detection_video()







# webcam = cv2.VideoCapture(0)
# #ser = serial.Serial ("/dev/ttyS0", 9600)

# while (True):

    # _, imageFrame = webcam.read()
    # hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)

    # # Set range for red color and
    # # define mask
    # red_lower = np.array([136, 87, 111], np.uint8)
    # red_upper = np.array([180, 255, 255], np.uint8)
    # red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)

    # kernal = np.ones((5, 5), "uint8")

    # # For red color
    # red_mask = cv2.dilate(red_mask, kernal)
    # res_red = cv2.bitwise_and(imageFrame, imageFrame, mask=red_mask)

    # contours, hierarchy = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # for pic, contour in enumerate(contours):
        # area = cv2.contourArea(contour)
        # if (area > 300):
            # x, y, w, h = cv2.boundingRect(contour)
            # imageFrame = cv2.rectangle(imageFrame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            # x2 = x + int(w/2)
            # y2 = y + int(h/2)
            # cv2.circle(imageFrame,(x2,y2),4,(0,255,0),-1)
            # text = "x: " + str(x2) + ", y: " + str(y2)
            # cv2.putText(imageFrame, text, (x2 - 10, y2 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            # # cv2.putText(imageFrame, "Red Colour" + str((x, y)), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255))
            # if (x > 350):
                # print("Move Right")
                # # ser.write("Move Right")
                # sleep(0.03)
            # if (x < 100):
                # print("Move Left")
                # # ser.write("Move Left")
                # sleep(0.03)


    # cv2.imshow("RPi Object Detection", imageFrame)
    # if cv2.waitKey(10) & 0xFF == ord('q'):
        # cap.release()
        # cv2.destroyAllWindows()
        # break
        
        
        


# while webcam.isOpened():
    # # to read frame by frame
    # # _, img_1 = webcam.read()
    # _, img_2 = webcam.read()

    # # find difference between two frames
    # diff = cv2.absdiff(img_1, img_2)

    # # to convert the frame to grayscale
    # diff_gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    # # apply some blur to smoothen the frame
    # diff_blur = cv2.GaussianBlur(diff_gray, (5, 5), 0)

    # # to get the binary image
    # _, thresh_bin = cv2.threshold(diff_blur, 20, 255, cv2.THRESH_BINARY)

    # # to find contours
    # contours, hierarchy = cv2.findContours(thresh_bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # # to draw the bounding box when the motion is detected
    # for contour in contours:
        # x, y, w, h = cv2.boundingRect(contour)
        # if cv2.contourArea(contour) > 300:
            # cv2.rectangle(img_1, (x, y), (x+w, y+h), (0, 255, 0), 2)
    # # cv2.drawContours(img_1, contours, -1, (0, 255, 0), 2)

    # # display the output
    # cv2.imshow("Detecting Motion...", img_1)
    # if cv2.waitKey(100) == 13:
        # exit()



# img = cv2.imread("/home/pi/Desktop/GreenBall.jpg",cv2.IMREAD_GRAYSCALE)
# img=255-img
# nz = cv2.findNonZero(img)
# a = nz[:,0,0].min()
# b = nz[:,0,0].max()
# c = nz[:,0,1].min()
# d = nz[:,0,1].max()
# print('a:{}, b:{}, c:{}, d:{}'.format(a,b,c,d))
    
# c0 = (a+b)/2
# c1 = (c+d)/2
# print('Ball centre: {},{}'.format(c0,c1))


# (h, w) = img.shape[:2] 
# print(h)
# print(w)
# img = cv2.circle(img, (w//2, h//2), 7, (255, 255, 255), -1)
# cv2.namedWindow('GreenBall', cv2.WINDOW_KEEPRATIO)
# cv2.imshow("GreenBall", img)
# cv2.resizeWindow('GreenBall', 200, 200)
# cv2.waitKey(0)









ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.reset_input_buffer()
send = 'Hello from pi'
while(True):
    ser.write("Hello from pi".encode())


(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
#print(cv2.__version__)
 
# if __name__ == '__main__' :
 
    # #Set up tracker.
    # #Instead of MIL, you can also use
    # tracker_types = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW', 'GOTURN', 'MOSSE', 'CSRT']
    # tracker_type = tracker_types[2]
 
    # if int(minor_ver) < 3:
        # tracker = cv2.Tracker_create(tracker_type)
    # else:
        # if tracker_type == 'BOOSTING':
            # tracker = cv2.TrackerBoosting_create()
        # if tracker_type == 'MIL':
            # tracker = cv2.TrackerMIL_create()
        # if tracker_type == 'KCF':
            # tracker = cv2.TrackerKCF.create()
        # if tracker_type == 'TLD':
            # tracker = cv2.TrackerTLD_create()
        # if tracker_type == 'MEDIANFLOW':
            # tracker = cv2.TrackerMedianFlow_create()
        # if tracker_type == 'GOTURN':
            # tracker = cv2.TrackerGOTURN_create()
        # if tracker_type == 'MOSSE':
            # tracker = cv2.TrackerMOSSE_create()
        # if tracker_type == "CSRT":
            # tracker = cv2.TrackerCSRT_create()
 
    # #Read video
    # video = cv2.VideoCapture(0)
 
    # #Exit if video not opened.
    # if not video.isOpened():
        # print("Could not open video")
        # sys.exit()
 
    # #Read first frame.
    # ok, frame = video.read()
    # if not ok:
        # print("Cannot read video file")
        # sys.exit()
     
    # #Define an initial bounding box
    # bbox = (287, 23, 86, 320)
 
    # #Uncomment the line below to select a different bounding box
    
    # #grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # bbox = cv2.selectROI(frame, False)
    # # print(bbox)
    # # grayframe=255-grayframe
    # # nz = cv2.findNonZero(grayframe)
    # # a = nz[:,0,0].min()
    # # b = nz[:,0,0].max()
    # # c = nz[:,0,1].min()
    # # d = nz[:,0,1].max()
    # # print('a:{}, b:{}, c:{}, d:{}'.format(a,b,c,d))
    
    # # c1 = (a+b)/2
    # # c0 = (c+d)/2
    # # print('Image Centre (height,width): {},{}'.format(c0,c1))
    
    # # (h, w) = grayframe.shape[:2] 
    # # print(h)
    # # print(w)

    # # dimension = grayframe.shape
    # # print("dimensions:",dimension)
    
    # # TLC_x = bbox[0]
    # # TLC_y = dimension[1] - bbox[1]
    # # LRC_x = bbox[0] + bbox[2]
    # # LRC_y = TLC_y - bbox[3]
    
    # # s0 = (TLC_y+LRC_y)/2
    # # s1 = (TLC_x+LRC_x)/2
    # # print('Square Centre (height,width): {},{}'.format(s0,s1))

 
    # #Initialize tracker with first frame and bounding box
    # ok = tracker.init(frame, bbox)
 
    # while True:
        # #Read a new frame
        # ok, frame = video.read()
        # if not ok:
            # break
         
        # #Start timer
        # timer = cv2.getTickCount()
 
        # #Update tracker
        # ok, bbox = tracker.update(frame)
 
        # #Calculate Frames per second (FPS)
        # fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
 
        # #Draw bounding box
        # if ok:
            # #Tracking success
            # p1 = (int(bbox[0]), int(bbox[1]))
            # p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
            # cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)
            
            # dim = frame.shape
            # #print('Image Dimension (height,width): {},{}:',format(dim))
            # print('Image Centre (height,width): {},{}'.format(dim[0]/2,dim[1]/2))

            # TLC_x = bbox[0]
            # TLC_y = dim[0] - bbox[1]
            # LRC_x = bbox[0] + bbox[2]
            # LRC_y = TLC_y - bbox[3]
            # c_x = dim[1]/2
            # c_y = dim[0]/2
            # sc_x = (TLC_x+LRC_x)/2
            # sc_y = (TLC_y+LRC_y)/2
            # print('Square Centre (height,width): {},{}'.format(sc_y,sc_x))
            # print('\n')
            
            # if (sc_x < c_x):
                # #print('Move Left')
                # ser.write(b'Move Left')
            # else:
                # #print('Move Right')
                # ser.write(b'Move Right')
            # if (sc_y < c_y):
                # #print('Move Down')
                # ser.write(b'Move Down')
            # else:
                # #print('Move Up')
                # ser.write(b'Move Up')
        # else :
            # #Tracking failure
            # cv2.putText(frame, "Tracking failure detected", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)
 
        # #Display tracker type on frame
        # cv2.putText(frame, tracker_type + " Tracker", (100,20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50),2);
     
        # #Display FPS on frame
        # cv2.putText(frame, "FPS : " + str(int(fps)), (100,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);
 
        # #Display result
        # cv2.imshow("Tracking", frame)
 
        # #Exit if ESC pressed
        # k = cv2.waitKey(1) & 0xff
        # if k == 27 : break

