from os import write
import random
import serial
import serial.tools.list_ports
import time


class Communication:
    baudrate = "9600"
    portName = "/dev/ttyUSB1"
    dummyPlug = False
    ports = serial.tools.list_ports.comports()
    ser = serial.Serial()

    def __init__(self):
        self.baudrate = 9600
        print("the available ports are (if none appear, press any letter): ")
        for i, port in enumerate(self.ports):
            print(("{}: {}".format(i, port)))

        # Select the port
        self.portName = str(
            self.ports[int(input("write serial port number : "))].device
        )
        # self.portName = "1"
        try:
            self.ser = serial.Serial(self.portName, self.baudrate)
            self.dummyPlug = False
            print("set dummy false")
        except serial.serialutil.SerialException:
            print("Can't open : ", self.portName)
            self.dummyPlug = True
            print("Dummy mode activated")

    def close(self):
        if self.ser.isOpen():
            self.ser.close()
        else:
            print(self.portName, " it's already closed")

    def getData(self):
        print(self.dummyPlug)
        if not self.dummyPlug:
            print("real")
            value = self.ser.readline()  # read line (single value) from the serial port
            print("get value", value)
            decoded_bytes = str(value[0 : len(value) - 2].decode("utf-8"))
            # print(decoded_bytes)
            data = decoded_bytes.split(",")
            print(data)
        else:
            data = (
                [int(time.time())]
                + random.sample(range(0, 300), 1)
                + [random.getrandbits(1)]
                + random.sample(range(-10, 10), 1)
                + random.sample(range(-180, 180), 3)
                + random.sample(range(-10, 10), 4)
            )
        return data

    def isOpen(self):
        return self.ser.isOpen()

    def dummyMode(self):
        return self.dummyPlug
