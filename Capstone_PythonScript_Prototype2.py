import multiprocessing
import time
import argparse
import csv
from daqhats import hat_list, HatIDs, mcc134
import time

"""
LINKS:
    https://mccdaq.github.io/daqhats/python.html#mcc-134-class
    https://files.digilent.com/manuals/UL-Linux/python/overview.html#installation
    https://pimylifeup.com/raspberry-pi-accelerometer-adxl345/
"""

def Main(args):
    csv=args.csv
    #BoardDeclariations()
    with open(csv,'w') as csvfile:
        csvfile.write("Hour.,Min.,Sec.,X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,Nozzle Temp.,Bed Temp.,Ambient Temp.\n")
        while True:
            
            """
            pool=multiprocessing.Pool(processes=2)
            result1=pool.apply_async(ReadAccelerometerData)
            result2=pool.apply_async(ExtractThermocoupleData)
            output1=result1.get()
            output2=result2.get()
            for i in output1:
                csvfile.write(","+str(i))
            for i in output2:
                csvfile.write(","+str(i))
            """

            pool=multiprocessing.Pool(processes=2)
            result1=pool.apply_async(ReadAccelerometerData2)
            result2=pool.apply_async(ReadAccelerometerData3)
            output1=result1.get()
            output2=result2.get()

            csvfile.write(str(time.localtime().tm_hour)+","+str(time.localtime().tm_min)+","+str(time.localtime().tm_sec))
            for i in output1:
                csvfile.write(","+str(i))
            for i in output2:
                csvfile.write(","+str(i))
            csvfile.write("\n")
            time.sleep(1)

def BoardDeclariations():
    #Calls out the MCC 134 Board ID
    board=mcc134()
    #Notifies the board that channel 0 is a K thermocouple
    board.tc_type_write(channel=0,tc_type=1)
    #Notifies the board that channel 1 is a K thermocouple
    board.tc_type_write(channel=1,tc_type=1)
    #Notifies the board that channel 2 is a K thermocouple
    board.tc_type_write(channel=2,tc_type=1)

def ReadAccelerometerData(board):
    values=[]
    for channel in range(board.info().NUM_AI_CHANNELS):
        value=board.a_in_read(channel)
        print("Ch {0}: {1:3.f}".format(channel,value))
        values.append(value)
    return values

def ReadAccelerometerData2():
    listed=[40,7,6]
    return listed

def ReadAccelerometerData3():
    listed=[30,25,10]
    return listed

def ExtractThermocoupleData():
    NozzleTemp=board.t_in_read(0)
    BedTemp=board.t_in_read(1)
    AmbientTemp=board.t_in_read(2)
    temps=[NozzleTemp,BedTemp,AmbientTemp]
    return temps

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    
    #Argument for calling a linear regression function.
    parser.add_argument(
            '--csv',
            help="Insert the name and pathway towward saving sensor data.",
            required=True)

    args=parser.parse_args()
    Main(args)
