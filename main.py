import micropython
micropython.alloc_emergency_exception_buf(100)
import pyb
import time
from pyb import UART
from pyb import Timer
from pyb import I2C
from machine import Pin

#u2 = UART(2, baudrate=115200, read_buf_len=8192)
#u3 = UART(3, baudrate=115200, read_buf_len=2048)
u6 = UART(6, baudrate=9600, read_buf_len=4096)
#u4 = UART(4, baudrate=115200, read_buf_len=8192) 

i2c = I2C(2, I2C.MASTER)
left_down = Pin('X12', Pin.IN, Pin.PULL_UP) 
left_enter = Pin('Y12', Pin.IN, Pin.PULL_UP)
camera = Pin('X11', Pin.IN, Pin.PULL_UP)
sw=1

def Fan():
    button1 = i2c.mem_read(2, 0x26, 0)
    button2 = i2c.mem_read(2, 0x27, 0)
    if (button1 == b'\xdf\xff' and button2 == b'\xff\xff'): 
        return 0
    else:
        return 1
    while True:
        first=state()


def RC():
    button1 = i2c.mem_read(2, 0x26, 0)
    button2 = i2c.mem_read(2, 0x27, 0)
    if (button1 == b'\x7f\xff' and button2 == b'\xff\xff'): 
        return 0
    else:
        return 1

def FNSCREEN():
    button1 = i2c.mem_read(2, 0x26, 0)
    button2 = i2c.mem_read(2, 0x27, 0)
    if (button2 == b'\xfe\xff' and button1 == b'\xff\xff'):
        return 0
    else:
        return 1

def ESTOP():
    button1 = i2c.mem_read(2, 0x26, 0)
    button2 = i2c.mem_read(2, 0x27, 0)
    if (button1 == b'\xef\xff' and button2 == b'\xff\xff'):
        return 0
    else:
        return 1
        
#########################right side################################     
    
def CAMERA():
    button1 = i2c.mem_read(2, 0x26, 0)
    button2 = i2c.mem_read(2, 0x27, 0)
    if (camera.value() == 0 and button2 == b'\xff\xff' and button1 == b'\xff\xff'):
        return 0
    else:
        return 1

def GPS():
    button1 = i2c.mem_read(2, 0x26, 0)
    button2 = i2c.mem_read(2, 0x27, 0)
    if (button2 == b'\xff\xfd' and button1 == b'\xff\xff'):
        return 0
    else:
        return 1

def SPEED():
    button1 = i2c.mem_read(2, 0x26, 0)
    button2 = i2c.mem_read(2, 0x27, 0)
    if (button2 == b'\xff\xfe' and button1 == b'\xff\xff'): 
        return 0
    else:
        return 1

def r_UP():
    button1 = i2c.mem_read(2, 0x26, 0)
    button2 = i2c.mem_read(2, 0x27, 0)
    if (button2 == b'\xef\xff' and button1 == b'\xff\xff'): 
        return 0
    else:
        return 1

def r_DOWN():
    button1 = i2c.mem_read(2, 0x26, 0)
    button2 = i2c.mem_read(2, 0x27, 0)
    if (button2 == b'\xf7\xff' and button1 == b'\xff\xff'):
        return 0
    else:
        return 1

def r_LEFT():
    button1 = i2c.mem_read(2, 0x26, 0)
    button2 = i2c.mem_read(2, 0x27, 0)
    if (button2 == b'\xfd\xff' and button1 == b'\xff\xff'):
        return 0
    else:
        return 1

def r_RIGHT():
    button1 = i2c.mem_read(2, 0x26, 0)
    button2 = i2c.mem_read(2, 0x27, 0)
    if (button2 == b'\xfb\xff' and button1 == b'\xff\xff'): 
        return 0
    else:
        return 1

def r_ENTER():
    button1 = i2c.mem_read(2, 0x26, 0)
    button2 = i2c.mem_read(2, 0x27, 0)
    if (button2 == b'\xbf\xff' and button1 == b'\xff\xff'):  
        return 0
    else:
        return 1

def r_STOP():
    button1 = i2c.mem_read(2, 0x26, 0)
    button2 = i2c.mem_read(2, 0x27, 0)
    if (button2 == b'\xdf\xff' and button1 == b'\xff\xff'): 
        return 0
    else:
        return 1
        
#########################left button##############

def SCAN():
    button1 = i2c.mem_read(2, 0x26, 0)
    button2 = i2c.mem_read(2, 0x27, 0)
    if (button1 == b'\xff\xf7' and button2 == b'\xff\xff'): 
        return 0
    else:
        return 1

def ADJUST():
    button1 = i2c.mem_read(2, 0x26, 0)
    button2 = i2c.mem_read(2, 0x27, 0)
    if (button1 == b'\xff\xef' and button2 == b'\xff\xff'): 
        return 0
    else:
        return 1

def l_STOP():
    button1 = i2c.mem_read(2, 0x26, 0)
    button2 = i2c.mem_read(2, 0x27, 0)
    if (button1 == b'\xff\xdf' and button2 == b'\xff\xff'): 
        return 0
    else:
        return 1

def l_UP():
    button1 = i2c.mem_read(2, 0x26, 0)
    button2 = i2c.mem_read(2, 0x27, 0)
    if (button1 == b'\xff\x7f' and button2 == b'\xff\xff'):
        return 0
    else:
        return 1

def l_DOWN():
    button1 = i2c.mem_read(2, 0x26, 0)
    button2 = i2c.mem_read(2, 0x27, 0)
    if (left_down.value() == 0 and button1 == b'\xff\xff' and button2 == b'\xff\xff' and camera.value() != 0): 
        return 0
    else:
        return 1

def l_LEFT():
    button1 = i2c.mem_read(2, 0x26, 0)
    button2 = i2c.mem_read(2, 0x27, 0)
    if (button1 == b'\xff\xfb' and button2 == b'\xff\xff'):
        return 0
    else:
        return 1

def l_RIGHT():
    button1 = i2c.mem_read(2, 0x26, 0)
    button2 = i2c.mem_read(2, 0x27, 0)
    if (button1 == b'\xff\xbf' and button2 == b'\xff\xff'):
        return 0
    else:
        return 1

def l_ENTER():
    button1 = i2c.mem_read(2, 0x26, 0)
    button2 = i2c.mem_read(2, 0x27, 0)
    if (left_enter.value() == 0 and button1 == b'\xff\xff' and button2 == b'\xff\xff'): 
        return 0
    else:
        return 1
###################buttom##############

def F1():
    button1 = i2c.mem_read(2, 0x26, 0)
    button2 = i2c.mem_read(2, 0x27, 0)
    if (button2 == b'\xff\xfb' and button1 == b'\xff\xff' and left_enter.value() != 0):
        return 0
    else:
        return 1

def F2():
    button1 = i2c.mem_read(2, 0x26, 0)
    button2 = i2c.mem_read(2, 0x27, 0)
    if (button2 == b'\xff\xf7' and button1 == b'\xff\xff'): 
        return 0
    else:
        return 1

def F3():
    button1 = i2c.mem_read(2, 0x26, 0)
    button2 = i2c.mem_read(2, 0x27, 0)
    if (button2 == b'\xff\xdf' and button1 == b'\xff\xff'):
        return 0
    else:
        return 1

def F4():
    button1 = i2c.mem_read(2, 0x26, 0)
    button2 = i2c.mem_read(2, 0x27, 0)
    if (button2 == b'\xff\xef' and button1 == b'\xff\xff'):
        return 0
    else:
        return 1

def F5():
    button1 = i2c.mem_read(2, 0x26, 0)
    button2 = i2c.mem_read(2, 0x27, 0)
    if (button2 == b'\xff\xbf' and button1 == b'\xff\xff'):
        return 0
    else:
        return 1

def F6():
    button1 = i2c.mem_read(2, 0x26, 0)
    button2 = i2c.mem_read(2, 0x27, 0)
    if (button2 == b'\xff\x7f' and button1 == b'\xff\xff'):
        return 0
    else:
        return 1

def F7():
    button1 = i2c.mem_read(2, 0x26, 0)
    button2 = i2c.mem_read(2, 0x27, 0)
    if (button1 == b'\xff\xfe' and button2 == b'\xff\xff'):
        return 0
    else:
        return 1

def SPACE():
    button1 = i2c.mem_read(2, 0x26, 0)
    button2 = i2c.mem_read(2, 0x27, 0)
    if (button1 == b'\xbf\xff' and button2 == b'\xff\xff'):
        return 0
    else:
        return 1

###################side button##############

def A():
    button1 = i2c.mem_read(2, 0x26, 0)
    button2 = i2c.mem_read(2, 0x27, 0)
    if (button1 == b'\xfb\xff' and button2 == b'\xff\xff'):
        return 0
    else:
        return 1

def B():
    button1 = i2c.mem_read(2, 0x26, 0)
    button2 = i2c.mem_read(2, 0x27, 0)
    if (button1 == b'\xfe\xff' and button2 == b'\xff\xff'):
        return 0
    else:
        return 1

def C():
    button1 = i2c.mem_read(2, 0x26, 0)
    button2 = i2c.mem_read(2, 0x27, 0)
    if (button1 == b'\xfd\xff' and button2 == b'\xff\xff'): 
        return 0
    else:
        return 1

def SHUTDOWN():
    button1 = i2c.mem_read(2, 0x26, 0)
    button2 = i2c.mem_read(2, 0x27, 0)
    if (button1 == b'\xf7\xff' and button2 == b'\xff\xff'):
        return 0
    else:
        return 1

while True:
    print("system print")

    if sw and not Fan():
        u6.writechar(21)
        print('Button Fan Pressed')
        sw=0
        sw=1
        pyb.delay(100)
        if not Fan():
            pyb.delay(100)
            if not Fan():
                pyb.delay(100)
                if not Fan():
                    pyb.delay(100)
                    if not Fan():
                        pyb.delay(100)
                        if not Fan():
                            pyb.delay(100)
                            if not Fan():
                                pyb.delay(200)
                                if not Fan():
                                    pyb.delay(300)
                                    while not Fan():
                                        u6.writechar(21)
                                        print('Button Fan Pressed')
                                        pyb.delay(100)

    if sw and not RC():#################################
        u6.writechar(22)
        print('Button RC Pressed')        
        sw=0
        sw=1
        pyb.delay(100)
        if not RC():
            pyb.delay(100)
            if not RC():
                pyb.delay(100)
                if not RC():
                    pyb.delay(100)
                    if not RC():
                        pyb.delay(100)
                        if not RC():
                            pyb.delay(100)
                            if not RC():
                                pyb.delay(200)
                                if not RC():
                                    pyb.delay(300)
                                    while not RC():
                                        u6.writechar(22)
                                        print('Button RC Pressed')
                                        pyb.delay(100)

    if sw and not FNSCREEN():
        u6.writechar(23)
        print('Button FNSCREEN Pressed')
        sw=0
        sw=1
        pyb.delay(100)
        if not FNSCREEN():
            pyb.delay(100)
            if not FNSCREEN():
                pyb.delay(100)
                if not FNSCREEN():
                    pyb.delay(100)
                    if not FNSCREEN():
                        pyb.delay(100)
                        if not FNSCREEN():
                            pyb.delay(100)
                            if not FNSCREEN():
                                pyb.delay(200)
                                if not FNSCREEN():
                                    pyb.delay(300)
                                    while not FNSCREEN():
                                        u6.writechar(23)
                                        print('Button FNSCREEN Pressed')
                                        pyb.delay(100)


    if sw and not ESTOP():
        u6.writechar(24)
        print('Button ESTOP Pressed')
        sw=0
        sw=1
        pyb.delay(100)
        if not ESTOP():
            pyb.delay(100)
            if not ESTOP():
                pyb.delay(100)
                if not ESTOP():
                    pyb.delay(100)
                    if not ESTOP():
                        pyb.delay(100)
                        if not ESTOP():
                            pyb.delay(100)
                            if not ESTOP():
                                pyb.delay(200)
                                if not ESTOP():
                                    pyb.delay(300)
                                    while not ESTOP():
                                        u6.writechar(24)
                                        print('Button ESTOP Pressed')
                                        pyb.delay(100)

    if sw and not camera.value():
        u6.writechar(11)
        print('Button CAMERA Pressed')
        sw=0
        sw=1
        pyb.delay(100)
        if not CAMERA():
            pyb.delay(100)
            if not CAMERA():
                pyb.delay(100)
                if not CAMERA():
                    pyb.delay(100)
                    if not CAMERA():
                        pyb.delay(100)
                        if not CAMERA():
                            pyb.delay(100)
                            if not CAMERA():
                                pyb.delay(200)
                                if not CAMERA():
                                    pyb.delay(300)
                                    while not CAMERA():
                                        u6.writechar(11)
                                        print('Button CAMERA Pressed')
                                        pyb.delay(100)


    if sw and not GPS():
        u6.writechar(12)
        print('Button GPS Pressed')
        sw=0
        sw=1
        pyb.delay(100)
        if not GPS():
            pyb.delay(100)
            if not GPS():
                pyb.delay(100)
                if not GPS():
                    pyb.delay(100)
                    if not GPS():
                        pyb.delay(100)
                        if not GPS():
                            pyb.delay(100)
                            if not GPS():
                                pyb.delay(200)
                                if not GPS():
                                    pyb.delay(300)
                                    while not GPS():
                                        u6.writechar(12)
                                        print('Button GPS Pressed')
                                        pyb.delay(100)

    if sw and not SPEED():
        u6.writechar(13)
        print('Button SPEED Pressed')
        sw=0
        sw=1
        pyb.delay(100)
        if not SPEED():
            pyb.delay(100)
            if not SPEED():
                pyb.delay(100)
                if not SPEED():
                    pyb.delay(100)
                    if not SPEED():
                        pyb.delay(100)
                        if not SPEED():
                            pyb.delay(100)
                            if not SPEED():
                                pyb.delay(200)
                                if not SPEED():
                                    pyb.delay(300)
                                    while not SPEED():
                                        u6.writechar(13)
                                        print('Button SPEED Pressed')
                                        pyb.delay(100)

    if sw and not r_UP():
        u6.writechar(14)
        print('Button right UP Pressed')
        sw=0
        sw=1
        pyb.delay(100)
        if not r_UP():
            pyb.delay(100)
            if not r_UP():
                pyb.delay(100)
                if not r_UP():
                    pyb.delay(100)
                    if not r_UP():
                        pyb.delay(100)
                        if not r_UP():
                            pyb.delay(100)
                            if not r_UP():
                                pyb.delay(200)
                                if not r_UP():
                                    pyb.delay(200)
                                    while not r_UP():
                                        u6.writechar(14)
                                        print('Button right UP Pressed')
                                        pyb.delay(100)

    if sw and not r_DOWN():
        u6.writechar(15)
        print('Button right DOWN Pressed')
        sw=0
        sw=1
        pyb.delay(100)
        if not r_DOWN():
            pyb.delay(100)
            if not r_DOWN():
                pyb.delay(100)
                if not r_DOWN():
                    pyb.delay(100)
                    if not r_DOWN():
                        pyb.delay(100)
                        if not r_DOWN():
                            pyb.delay(100)
                            if not r_DOWN():
                                pyb.delay(200)
                                if not r_DOWN():
                                    pyb.delay(300)
                                    while not r_DOWN():
                                        u6.writechar(15)
                                        print('Button right DOWN Pressed')
                                        pyb.delay(100)

    if sw and not r_LEFT():
        u6.writechar(16)
        print('Button right LEFT Pressed')
        sw=0
        sw=1
        pyb.delay(50)
        if not r_LEFT():
            pyb.delay(50)
            if not r_LEFT():
                pyb.delay(50)
                if not r_LEFT():
                    pyb.delay(900)
                    if not r_LEFT():
                        pyb.delay(50)
                        if not r_LEFT():
                            pyb.delay(50)
                            if not r_LEFT():
                                pyb.delay(900)
                                if not r_LEFT():
                                    pyb.delay(900)
                                    while not r_LEFT():
                                        u6.writechar(16)
                                        print('Button right LEFT Pressed')
                                        pyb.delay(100)

    if sw and not r_RIGHT():
        u6.writechar(17)
        print('Button right RIGHT Pressed')
        sw=0
        sw=1
        pyb.delay(100)
        if not r_RIGHT():
            pyb.delay(100)
            if not r_RIGHT():
                pyb.delay(100)
                if not r_RIGHT():
                    pyb.delay(100)
                    if not r_RIGHT():
                        pyb.delay(100)
                        if not r_RIGHT():
                            pyb.delay(100)
                            if not r_RIGHT():
                                pyb.delay(200)
                                if not r_RIGHT():
                                    pyb.delay(300)
                                    while not r_RIGHT():
                                        u6.writechar(17)
                                        print('Button right RIGHT Pressed')
                                        pyb.delay(100)

    if sw and not r_ENTER():
        u6.writechar(18)
        print('Button right ENTER Pressed')
        sw=0
        sw=1
        pyb.delay(100)
        if not r_ENTER():
            pyb.delay(100)
            if not r_ENTER():
                pyb.delay(100)
                if not r_ENTER():
                    pyb.delay(100)
                    if not r_ENTER():
                        pyb.delay(100)
                        if not r_ENTER():
                            pyb.delay(100)
                            if not r_ENTER():
                                pyb.delay(200)
                                if not r_ENTER():
                                    pyb.delay(300)
                                    while not r_ENTER():
                                        u6.writechar(18)
                                        print('Button right ENTER Pressed')
                                        pyb.delay(100)

    if sw and not r_STOP():
        u6.writechar(19)
        print('Button right STOP Pressed')
        sw=0
        sw=1
        pyb.delay(100)
        if not r_STOP():
            pyb.delay(100)
            if not r_STOP():
                pyb.delay(100)
                if not r_STOP():
                    pyb.delay(100)
                    if not r_STOP():
                        pyb.delay(100)
                        if not r_STOP():
                            pyb.delay(100)
                            if not r_STOP():
                                pyb.delay(200)
                                if not r_STOP():
                                    pyb.delay(300)
                                    while not r_STOP():
                                        u6.writechar(19)
                                        print('Button right STOP Pressed')
                                        pyb.delay(100)

    if sw and not SCAN():
        u6.writechar(1)
        print('Button SCAN Pressed')
        sw=0
        sw=1
        pyb.delay(100)
        if not SCAN():
            pyb.delay(100)
            if not SCAN():
                pyb.delay(100)
                if not SCAN():
                    pyb.delay(100)
                    if not SCAN():
                        pyb.delay(100)
                        if not SCAN():
                            pyb.delay(100)
                            if not SCAN():
                                pyb.delay(200)
                                if not SCAN():
                                    pyb.delay(300)
                                    while not SCAN():
                                        u6.writechar(1)
                                        print('Button SCAN Pressed')
                                        pyb.delay(100)


    if sw and not ADJUST():
        u6.writechar(2)
        print('Button ADJUST Pressed')
        sw=0
        sw=1
        pyb.delay(100)
        if not ADJUST():
            pyb.delay(100)
            if not ADJUST():
                pyb.delay(100)
                if not ADJUST():
                    pyb.delay(100)
                    if not ADJUST():
                        pyb.delay(100)
                        if not ADJUST():
                            pyb.delay(100)
                            if not ADJUST():
                                pyb.delay(200)
                                if not ADJUST():
                                    pyb.delay(300)
                                    while not ADJUST():
                                        u6.writechar(2)
                                        print('Button ADJUST Pressed')
                                        pyb.delay(100)


    if sw and not l_STOP():
        u6.writechar(3) 
        print('Button left STOP Pressed')
        sw=0
        sw=1
        pyb.delay(100)
        if not l_STOP():
            pyb.delay(100)
            if not l_STOP():
                pyb.delay(100)   
                if not l_STOP():
                    pyb.delay(100)
                    if not l_STOP():
                        pyb.delay(100)
                        if not l_STOP():
                            pyb.delay(100)   
                            if not l_STOP():
                                pyb.delay(200)
                                if not l_STOP():
                                    pyb.delay(300)
                                    while not l_STOP():
                                        u6.writechar(3) 
                                        print('Button left STOP Pressed')
                                        pyb.delay(100)

    if sw and not l_UP():
        u6.writechar(4) 
        print('Button left UP Pressed')
        sw=0
        sw=1
        pyb.delay(100)
        if not l_UP():
            pyb.delay(100)
            if not l_UP():
                pyb.delay(100)   
                if not l_UP():
                    pyb.delay(100)
                    if not l_UP():
                        pyb.delay(100)
                        if not l_UP():
                            pyb.delay(100)   
                            if not l_UP():
                                pyb.delay(200)
                                if not l_UP():
                                    pyb.delay(300)
                                    while not l_UP():
                                        u6.writechar(4) 
                                        print('Button left UP Pressed')
                                        pyb.delay(100)

    if sw and not l_DOWN():
        u6.writechar(5) 
        print('Button left DOWN Pressed')
        sw=0
        sw=1
        pyb.delay(100)
        if not l_DOWN():
            pyb.delay(100)
            if not l_DOWN():
                pyb.delay(100)   
                if not l_DOWN():
                    pyb.delay(100)
                    if not l_DOWN():
                        pyb.delay(100)
                        if not l_DOWN():
                            pyb.delay(100)   
                            if not l_DOWN():
                                pyb.delay(200)
                                if not l_DOWN():
                                    pyb.delay(300)
                                    while not l_DOWN():
                                        u6.writechar(5) 
                                        print('Button left DOWN Pressed')
                                        pyb.delay(100)

    if sw and not l_LEFT():
        u6.writechar(6)
        print('Button left LEFT Pressed')
        sw=0
        sw=1
        pyb.delay(100)
        if not l_LEFT():
            pyb.delay(100)
            if not l_LEFT():
                pyb.delay(100)   
                if not l_LEFT():
                    pyb.delay(100)
                    if not l_LEFT():
                        pyb.delay(100)
                        if not l_LEFT():
                            pyb.delay(100)   
                            if not l_LEFT():
                                pyb.delay(200)
                                if not l_LEFT():
                                    pyb.delay(300)
                                    while not l_LEFT():
                                        u6.writechar(6)
                                        print('Button left LEFT Pressed')
                                        pyb.delay(100)

    if sw and not l_RIGHT():
        u6.writechar(7)
        print('Button left RIGHT Pressed')
        sw=0
        sw=1
        pyb.delay(100)
        if not l_RIGHT():
            pyb.delay(100)
            if not l_RIGHT():
                pyb.delay(100)   
                if not l_RIGHT():
                    pyb.delay(100)
                    if not l_RIGHT():
                        pyb.delay(100)
                        if not l_RIGHT():
                            pyb.delay(100)   
                            if not l_RIGHT():
                                pyb.delay(200)
                                if not l_RIGHT():
                                    pyb.delay(300)
                                    while not l_RIGHT():
                                        u6.writechar(7)
                                        print('Button left RIGHT Pressed')
                                        pyb.delay(100)

    if sw and not l_ENTER():
        u6.writechar(8) 
        print('Button left ENTER Pressed')
        sw=0
        sw=1
        pyb.delay(100)
        if not l_ENTER():
            pyb.delay(100)
            if not l_ENTER():
                pyb.delay(100)   
                if not l_ENTER():
                    pyb.delay(100)
                    if not l_ENTER():
                        pyb.delay(100)
                        if not l_ENTER():
                            pyb.delay(100)   
                            if not l_ENTER():
                                pyb.delay(200)
                                if not l_ENTER():
                                    pyb.delay(300)
                                    while not l_ENTER():
                                        u6.writechar(8) 
                                        print('Button left ENTER Pressed')
                                        pyb.delay(100)

    if sw and not F1():
        u6.writechar(31)
        print('Button F1 Pressed')
        sw=0
        sw=1
        pyb.delay(100)
        if not F1():
            pyb.delay(100)
            if not F1():
                pyb.delay(100)
                if not F1():
                    pyb.delay(100)
                    if not F1():
                        pyb.delay(100)
                        if not F1():
                            pyb.delay(100)
                            if not F1():
                                pyb.delay(100)
                                if not F1():
                                    pyb.delay(100)
                                    while not F1():
                                        u6.writechar(31)
                                        print('Button F1 Pressed')
                                        pyb.delay(100)

    if sw and not F2():
        u6.writechar(32)
        print('Button F2 Pressed')
        sw=0
        sw=1
        pyb.delay(100)
        if not F2():
            pyb.delay(100)
            if not F2():
                pyb.delay(100)
                if not F2():
                    pyb.delay(100)
                    if not F2():
                        pyb.delay(100)
                        if not F2():
                            pyb.delay(100)
                            if not F2():
                                pyb.delay(100)
                                if not F2():
                                    pyb.delay(100)
                                    while not F2():
                                        u6.writechar(32)
                                        print('Button F2 Pressed')
                                        pyb.delay(100)

    if sw and not F3():
        u6.writechar(33)
        print('Button F3 Pressed')
        sw=0
        sw=1
        pyb.delay(100)
        if not F3():
            pyb.delay(100)
            if not F3():
                pyb.delay(100)
                if not F3():
                    pyb.delay(100)
                    if not F3():
                        pyb.delay(100)
                        if not F3():
                            pyb.delay(100)
                            if not F3():
                                pyb.delay(100)
                                if not F3():
                                    pyb.delay(100)
                                    while not F3():
                                        u6.writechar(33)
                                        print('Button F3 Pressed')
                                        pyb.delay(100)

    if sw and not F4():
        u6.writechar(34)
        print('Button F4 Pressed')
        sw=0
        sw=1
        pyb.delay(100)
        if not F4():
            pyb.delay(100)
            if not F4():
                pyb.delay(100)
                if not F4():
                    pyb.delay(100)
                    if not F4():
                        pyb.delay(100)
                        if not F4():
                            pyb.delay(100)
                            if not F4():
                                pyb.delay(200)
                                if not F4():
                                    pyb.delay(300)
                                    while not F4():
                                        u6.writechar(34)
                                        print('Button F4 Pressed')
                                        pyb.delay(100)

    if sw and not F5():
        u6.writechar(35)
        print('Button F5 Pressed')
        sw=0
        sw=1
        pyb.delay(100)
        if not F5():
            pyb.delay(100)
            if not F5():
                pyb.delay(100)
                if not F5():
                    pyb.delay(100)
                    if not F5():
                        pyb.delay(100)
                        if not F5():
                            pyb.delay(100)
                            if not F5():
                                pyb.delay(200)
                                if not F5():
                                    pyb.delay(300)
                                    while not F5():
                                        u6.writechar(35)
                                        print('Button F5 Pressed')
                                        pyb.delay(100)

    if sw and not F6():
        u6.writechar(36)
        print('Button F6 Pressed')
        sw=0
        sw=1
        pyb.delay(100)
        if not F6():
            pyb.delay(100)
            if not F6():
                pyb.delay(100)
                if not F6():
                    pyb.delay(100)
                    if not F6():
                        pyb.delay(100)
                        if not F6():
                            pyb.delay(100)
                            if not F6():
                                pyb.delay(200)
                                if not F6():
                                    pyb.delay(300)
                                    while not F6():
                                        u6.writechar(36)
                                        print('Button F6 Pressed')
                                        pyb.delay(100)


    if sw and not F7():
        u6.writechar(37)
        print('Button F7 Pressed')
        sw=0
        sw=1
        pyb.delay(100)
        if not F7():
            pyb.delay(100)
            if not F7():
                pyb.delay(100)
                if not F7():
                    pyb.delay(100)
                    if not F7():
                        pyb.delay(100)
                        if not F7():
                            pyb.delay(100)
                            if not F7():
                                pyb.delay(200)
                                if not F7():
                                    pyb.delay(300)
                                    while not F7():
                                        u6.writechar(37)
                                        print('Button F7 Pressed')
                                        pyb.delay(100)

    if sw and not SPACE():
        u6.writechar(38)
        print('Button SPACE Pressed')
        sw=0
        sw=1
        pyb.delay(100)
        if not SPACE():
            pyb.delay(100)
            if not SPACE():
                pyb.delay(100)
                if not SPACE():
                    pyb.delay(100)
                    if not SPACE():
                        pyb.delay(100)
                        if not SPACE():
                            pyb.delay(100)
                            if not SPACE():
                                pyb.delay(200)
                                if not SPACE():
                                    pyb.delay(300)
                                    while not SPACE():
                                        u6.writechar(38)
                                        print('Button SPACE Pressed')
                                        pyb.delay(100)
    if sw and not A():
        u6.writechar(41) 
        print('Button A Pressed')
        sw=0
        sw=1
        pyb.delay(100)
        if not A():
            pyb.delay(100)
            if not A():
                pyb.delay(100)
                if not A():
                    pyb.delay(100)
                    if not A():
                        pyb.delay(100)
                        if not A():
                            pyb.delay(100)
                            if not A():
                                pyb.delay(200)
                                if not A():
                                    pyb.delay(300)
                                    while not A():
                                        u6.writechar(41) 
                                        print('Button A Pressed')
                                        pyb.delay(100)

    if sw and not B():
        u6.writechar(42)
        print('Button B Pressed')
        sw=0
        sw=1
        pyb.delay(100)
        if not B():
            pyb.delay(100)
            if not B():
                pyb.delay(100)
                if not B():
                    pyb.delay(100)
                    if not B():
                        pyb.delay(100)
                        if not B():
                            pyb.delay(100)
                            if not B():
                                pyb.delay(200)
                                if not B():
                                    pyb.delay(300)
                                    while not B():
                                        u6.writechar(42)
                                        print('Button B Pressed')
                                        pyb.delay(100)



    if sw and not C():
        u6.writechar(43) 
        print('Button C Pressed')
        sw=0
        sw=1
        pyb.delay(100)
        if not C():
            pyb.delay(100)
            if not C():
                pyb.delay(100)
                if not C():
                    pyb.delay(100)
                    if not C():
                        pyb.delay(100)
                        if not C():
                            pyb.delay(100)
                            if not C():
                                pyb.delay(200)
                                if not C():
                                    pyb.delay(300)
                                    while not C():
                                        u6.writechar(43) 
                                        print('Button C Pressed')
                                        pyb.delay(100)

    if sw and not SHUTDOWN():
        u6.writechar(44)
        print('Button SHUTDOWN Pressed')
        sw=0
        sw=1
        pyb.delay(100)
        if not SHUTDOWN():
            pyb.delay(100)
            if not SHUTDOWN():
                pyb.delay(100)
                if not SHUTDOWN():
                    pyb.delay(100)
                    if not SHUTDOWN():
                        pyb.delay(100)
                        if not SHUTDOWN():
                            pyb.delay(100)
                            if not SHUTDOWN():
                                pyb.delay(200)
                                if not SHUTDOWN():
                                    pyb.delay(300)
                                    while not SHUTDOWN():
                                        u6.writechar(44)
                                        print('Button SHUTDOWN Pressed')
                                        pyb.delay(100)