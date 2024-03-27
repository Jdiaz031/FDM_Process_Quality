from smbus2 import SMBus
import time
import argparse
import board
import busio
import adafruit_adxl34x
import csv

"""
LINKS:
    https://mccdaq.github.io/daqhats/python.html#mcc-134-class
    https://files.digilent.com/manuals/UL-Linux/python/overview.html#installation
    https://pimylifeup.com/raspberry-pi-accelerometer-adxl345/
"""




def Main(args):
    i2c=busio.I2C(board.SCL,board.SDA)
    accelerometer=adafruit_adx134x.ADXL345(i2c)
    with open(args.csv,'w') as csvfile:
        while True:
            print("%f %f %f"%accelerometer.acceleration+"\n")
            time.sleep(1)

"""
import sys
from daqhats import hat_list, HatIDs, mcc134
board_list=hat_list(filter_by_id=HatIDs.ANY)
if not board_list:
    print("No boards found")
    sys.exit()
    for entry in board_list:
        if entry.id == HatIDs.MCC_134:
            print("Board {}: MCC 134".format(entry.address))
            board=mcc134(entry.address)
            for channel in range(board.info().NUM_AI_CHANNELS):
                value=board.a_in_read(channel)
                print("Ch {0}: {1:3.f}".format(channel,value))
"""

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    
    #Argument for calling a linear regression function.
    parser.add_argument(
            '--csv',
            help="Insert the name and pathway towward saving sensor data.",
            required=True)

    args=parser.parse_args()
    Main(args)
