This is the GitHub repository for the FDM Process Quality Capstone at 
New Mexico State University.

The tool here is used on a Raspberry Pi utilizing an MCC 134 DAQ board sheil.
The following steps are used to run the Python script on an SSH
Raspberry Pi after downloading the repository.All Python scripts utilize a flag "csv" to declare the pathway in
which a csv containing sensor data to be saved.

```
cd ~/Downloads
sudo apt install git
git clone https://github.com/Jdiaz031/FDM_Process_Quality.git
cd FDM_Process_Quality
chmod +x raspberrypi_setup.sh
./raspberrypi_setup.sh
python3 Capstone_PythonScript.py --csv /path/to/file
```
