from tkinter import *
import serial
# from PIL import ImageTk,Image
from time import sleep



#-------------------------------Interface----------------------------------
serialString = ""
bmp = ""

serialPort = serial.Serial(port = "COM1", baudrate=115200,bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
try:
    serialPort.isOpen()
    print('serial is open')
except:
    print('error')
    exit()

#TODO: input is ascci 
#TODO: Com port

if (serialPort.isOpen()):
    try:
        while(1):
            #To find port = device manager -> Ports
            if(serialPort.in_waiting > 0):

                # Read data out of the buffer until a carraige return / new line is found
                serialString = serialPort.readline()
                bmp = serialString.decode("Ascii")

    except Exception:
        print('error')
else:
    print('Cannot open serial port')

# root = Tk()
# root.title("Spiff's Heartbeat")
# root.geometry("275x200+200+200")
# root.iconbitmap("Spifficon.ico")

# var = StringVar()
# var.set(bmp)


# image = Image.open('HeartImg.png')
# image = image.resize((200,200), Image.ANTIALIAS)
# tk_image = ImageTk.PhotoImage(image)


# label = Label(root, textvariable=var, image=tk_image, compound='center',font=(None,35), fg="White")
# label.pack()

# root.mainloop()




