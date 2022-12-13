

import serial
import time
 
s = serial.Serial('/dev/ttyACM0', 9600) # change name, if needed
#s.open()
time.sleep(5) # the Arduino is reset after enabling the serial connectio, therefore we have to wait some seconds

while True:
    s.write(bytes("Move Up\n", 'utf-8'))
    time.sleep(0.05)








# s.write(b'test from rpi')
# try:
    # while True:
        # response = s.readline()
        # print(response)
# except KeyboardInterrupt:
    # s.close()



# def write_read(x):
    # s.write(bytes(x, 'utf-8'))
    # time.sleep(0.05)
    # data = s.readline()
    # return data
# while True:
    # num = input("Enter a number: ") # Taking input from user
    # value = write_read(num)
    # print(value) # printing the value
