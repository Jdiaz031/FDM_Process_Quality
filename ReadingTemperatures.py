import sys
import time
import argparse
import csv
from daqhats import hat_list, HatIDs, mcc134
import time

"""
LINKS:
    https://mccdaq.github.io/daqhats/python.html#mcc-134-class
"""

def Main(args):
    csv=args.csv
    board=BoardDeclariations()
    print("Board Connected \n")
    with open(csv,'w') as csvfile:
        csvfile.write("Hour.,Min.,Sec.,
                      Nozzle Temp.,Bed Temp.,Ambient Temp.\n")
        while True:
            temps=ExtractThermocoupleData()
            csvfile.write(str(time.localtime().tm_hour)+
                          ","+str(time.localtime().tm_min)+","+
                          str(time.localtime().tm_sec))
            csvfile.write(str(temps[0])+
                          ","+str(temps[1])+
                          ","+str(temps[2])+
                          ", \n")
            time.sleep(1)

def BoardDeclariations():
    board_list = hat_list(filter_by_id = HatIDs.ANY)
    if not board_list:
        print("No boards found")
        sys.exit()

    # Read and display every channel
    for entry in board_list:
        if entry.id == HatIDs.MCC_134:
        if entry.id == HatIDs.MCC_134:
            board = mcc134(entry.address)
            board.tc_type_write(channel=0,tc_type=1)
            #Notifies the board that channel 1 is a K thermocouple
            board.tc_type_write(channel=1,tc_type=1)
            #Notifies the board that channel 2 is a K thermocouple
            board.tc_type_write(channel=2,tc_type=1)
    return board


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
