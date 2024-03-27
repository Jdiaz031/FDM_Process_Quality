#!/bin/bash

sudo apt-get update
sudo apt-get upgrade
sudo raspi-config
sudo apt-get install python3-dev python3-pip python3-smbus i2c-tools git -y
sudo pip3 install -r requirements.txt
git clone https://github.com/mccdaq/daqhats.git
cd ./daqhats/
sudo ./install.sh
