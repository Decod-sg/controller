import pyb
import micropython
micropython.alloc_emergency_exception_buf(100)

from pyb import ExtInt
from pyb import Pin
from pyb import I2C
from pyb import UART

class Controller(object):
    def __init__(self, led):
        self.led = led
        self.i2c = I2C(2, I2C.MASTER)
        self.buf1 =  bytearray(2)
        self.buf2 =  bytearray(2)
        self.buf1 = self.i2c.mem_read(2, 0x26, 0)
        self.buf2 = self.i2c.mem_read(2, 0x27, 0)
        self.intr1 = 0
        self.intr2 = 0
        self.counter = 0
        self.left_down = Pin('X12', Pin.IN, Pin.PULL_UP) 
        self.left_enter = Pin('Y12', Pin.IN, Pin.PULL_UP)
        self.camera = Pin('X11', Pin.IN, Pin.PULL_UP)
        self.u6 = UART(6, baudrate=9600, read_buf_len=4096)
        print (self.buf1)
        print (self.buf2)
        print ("hello world")
        ExtInt('X19', ExtInt.IRQ_FALLING, Pin.PULL_UP, self.intr1_cb)
        ExtInt('X20', ExtInt.IRQ_FALLING, Pin.PULL_UP, self.intr2_cb)


    def intr1_cb(self, tim):
        self.intr1 = 1
        self.led.toggle()
        
    def intr2_cb(self, tim):
        self.intr2 = 1
        self.led.toggle()
		
    def read_I2C(self):
        while True:
            #pyb.delay(1000)
            if self.intr1 or self.intr2:
                self.counter = self.counter + 1
                self.intr1 = 0
                self.intr2 = 0
                self.buf1 = self.i2c.mem_read(2, 0x26, 0)
                self.buf2 = self.i2c.mem_read(2, 0x27, 0)
                #print(self.counter,self.buf1,self.buf2)
                if (self.buf1 == b'\xdf\xff' and self.buf2 == b'\xff\xff'): 
                    self.u6.writechar(21)
                    print('Button Fan Pressed')
                elif (self.buf1 == b'\x7f\xff' and self.buf2 == b'\xff\xff'): 
                    self.u6.writechar(22)
                    print('Button RC Pressed')
                elif (self.buf2 == b'\xfe\xff' and self.buf1 == b'\xff\xff'): 
                    self.u6.writechar(23)
                    print('Button FNSCREEN Pressed')
                elif (self.buf1 == b'\xef\xff' and self.buf2 == b'\xff\xff'): 
                    self.u6.writechar(24)
                    print('Button ESTOP Pressed')
                elif (self.buf2 == b'\xff\xfd' and self.buf1 == b'\xff\xff'): 
                    self.u6.writechar(12)
                    print('Button GPS Pressed')
                elif (self.buf2 == b'\xff\xfe' and self.buf1 == b'\xff\xff'): 
                    self.u6.writechar(13)
                    print('Button SPEED Pressed')
                elif (self.buf2 == b'\xef\xff' and self.buf1 == b'\xff\xff'): 
                    self.u6.writechar(14)
                    print('Button right UP Pressed')
                elif (self.buf2 == b'\xf7\xff' and self.buf1 == b'\xff\xff'): 
                    self.u6.writechar(15)
                    print('Button right DOWN Pressed')
                elif (self.buf2 == b'\xfd\xff' and self.buf1 == b'\xff\xff'): 
                    self.u6.writechar(16)
                    print('Button right LEFT Pressed')
                elif (self.buf2 == b'\xfb\xff' and self.buf1 == b'\xff\xff'): 
                    self.u6.writechar(17)
                    print('Button right RIGHT Pressed')
                elif (self.buf2 == b'\xbf\xff' and self.buf1 == b'\xff\xff'): 
                    self.u6.writechar(18)
                    print('Button right ENTER Pressed')
                elif (self.buf2 == b'\xdf\xff' and self.buf1 == b'\xff\xff'): 
                    self.u6.writechar(19)
                    print('Button right STOP Pressed')
                elif (self.buf1 == b'\xff\xf7' and self.buf2 == b'\xff\xff'): 
                    self.u6.writechar(1)
                    print('Button SCAN Pressed')
                elif (self.buf1 == b'\xff\xef' and self.buf2 == b'\xff\xff'): 
                    self.u6.writechar(2)
                    print('Button ADJUST Pressed')
                elif (self.buf1 == b'\xff\xdf' and self.buf2 == b'\xff\xff'): 
                    self.u6.writechar(3)
                    print('Button left STOP Pressed')
                elif (self.buf1 == b'\xff\x7f' and self.buf2 == b'\xff\xff'): 
                    self.u6.writechar(4)
                    print('Button left UP Pressed')
                elif (self.buf1 == b'\xff\xfb' and self.buf2 == b'\xff\xff'): 
                    self.u6.writechar(6)
                    print('Button left LEFT Pressed')
                elif (self.buf1 == b'\xff\xbf' and self.buf2 == b'\xff\xff'): 
                    self.u6.writechar(7)
                    print('Button left RIGHT Pressed')
                elif (self.buf1 == b'\xff\xff' and self.buf2 == b'\xff\xff' and self.left_enter.value() == 0): 
                    self.u6.writechar(8)
                    print('Button left ENTER Pressed')
                elif (self.buf1 == b'\xff\xff' and self.buf2 == b'\xff\xfb'): 
                    self.u6.writechar(31)
                    print('Button F1 Pressed')
                elif (self.buf1 == b'\xff\xff' and self.buf2 == b'\xff\xf7'): 
                    self.u6.writechar(32)
                    print('Button F2 Pressed')
                elif (self.buf1 == b'\xff\xff' and self.buf2 == b'\xff\xdf'): 
                    self.u6.writechar(33)
                    print('Button F3 Pressed')
                elif (self.buf1 == b'\xff\xff' and self.buf2 == b'\xff\xef'): 
                    self.u6.writechar(34)
                    print('Button F4 Pressed')
                elif (self.buf1 == b'\xff\xff' and self.buf2 == b'\xff\xbf'): 
                    self.u6.writechar(35)
                    print('Button F5 Pressed')
                elif (self.buf1 == b'\xff\xff' and self.buf2 == b'\xff\x7f'): 
                    self.u6.writechar(36)
                    print('Button F6 Pressed')
                elif (self.buf1 == b'\xff\xfe' and self.buf2 == b'\xff\xff'): 
                    self.u6.writechar(37)
                    print('Button F7 Pressed')
                elif (self.buf1 == b'\xbf\xff' and self.buf2 == b'\xff\xff'): 
                    self.u6.writechar(38)
                    print('Button SPACE Pressed')
                elif (self.buf1 == b'\xfb\xff' and self.buf2 == b'\xff\xff'): 
                    self.u6.writechar(41)
                    print('Button A Pressed')
                elif (self.buf1 == b'\xfe\xff' and self.buf2 == b'\xff\xff'): 
                    self.u6.writechar(42)
                    print('Button B Pressed')
                elif (self.buf1 == b'\xfd\xff' and self.buf2 == b'\xff\xff'): 
                    self.u6.writechar(43)
                    print('Button C Pressed')
                elif (self.buf1 == b'\xf7\xff' and self.buf2 == b'\xff\xff'): 
                    self.u6.writechar(44)
                    print('Button SHUTDOWN Pressed')
                pyb.delay(500)

if __name__ == "__main__":
    red = Controller(pyb.LED(1))
    red.read_I2C()