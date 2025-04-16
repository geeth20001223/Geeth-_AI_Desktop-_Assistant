@echo off
python synthetic_monitor.py

rem Disconnect any existing ADB connections
echo Disconnecting old connections...
adb disconnect

rem Set up the device for TCP/IP mode on port 5555
echo Setting up connected device
adb tcpip 5555

rem Waiting for the device to initialize
echo Waiting for device to initialize
timeout 3

rem Dynamically retrieve the device's IP address (use this if you want dynamic retrieval)
FOR /F "tokens=2" %%G IN ('adb shell ip addr show wlan0 ^|find "inet "') DO set ipfull=%%G
FOR /F "tokens=1 delims=/" %%G in ("%ipfull%") DO set ip=%%G

rem Connect to the device using the dynamically retrieved IP address
echo Connecting to device with IP %ip%...
adb connect %ip%

rem --- Alternatively, use a hardcoded IP if you know the device IP in advance ---
rem Uncomment the following lines if you prefer a hardcoded IP:
rem set DEVICE_IP=192.168.1.196  (Replace with the actual IP address)
rem adb connect %DEVICE_IP%:5555

@echo on
