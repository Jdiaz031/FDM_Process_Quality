#!/bin/bash

sudo apt-get update
sudo apt-get upgrade
sudo raspi-config
sudo apt-get install python3-dev python3-pip python3-smbus i2c-tools git python3-multiprocess libraspberrypi-dev -y
git clone https://github.com/mccdaq/daqhats
cd daqhats
sudo ./install.sh
sudo daqhats_read_eeproms
