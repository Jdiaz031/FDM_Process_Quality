#!/bin/bash

sudo apt-get update
sudo apt-get upgrade
sudo raspi-config
sudo apt-get install vim vim-airline vim-airline-themes python3-dev libraspberrypi-dev -y
sudo apt remove nano
git clone https://github.com/mccdaq/daqhats
cd daqhats
sudo ./install.sh
sudo daqhats_read_eeproms
cd ..
mv VIMSetup ~/.vimrc
