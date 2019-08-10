# Connected Device IP Address Scanner Tool

This small lightweight program will let you know the IPs of the devices that are connected to your lan. This program fully runs on shell or bash.

## Installation

Use git clone command to download the program.

```
git clone https://github.com/shafinhasnat/Connected-device-IP-address-scanner.git
```

and unzip the zipped files. Here ```ipScanner_win.zip``` contains executable file for Windows, and ```ipScanner_linux.zip``` contains executable file for Linux.
Later to access the program directly from shell or bash, just follow the following steps-

For windows just add the location directory to Path. Just follow ```System>> Advanced System Settings>> Environment variables>> System variables>> Path>> New``` and paste directory location of ```ipScanner_win``` folder.

For Linux, open the terminal and type ```export PATH==$PATH:~/<Directory location of ipScanner_linux>```.

That is how you can make the software accessible from anywhere of your windows or linux system.

## Usage
To directly run from ```ipScanner.py``` file just type

```bash
python ipScanner.py -o <<w for windows || l for linux>> -f <<ip range start from>> -t <<ip range to>> 
```
as an example-

```bash
python ipScanner.py -o w -f 192.168.0.100 -t 110
```
If the path has been added to enviroment variable, you can simply access it by typing ```ipScanner```.

