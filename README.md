K11Consult
==========

A python project that uses pyserial to interact with the ECU of Nissan vehicles that utilise the Nissan Consult protocol.

The protocol reads and writes hex via a serial connection, with dashboard.py sending the commands and reading in realtime the resultant data stream from the ECU. The script is essentially in two parts; a non blocking deamonised thread that interacts with the ECU, and a gui using pygame that displays the data in the style of a dashboard. There are no external images used as I've written this for minimal CPU usage and to show what's possible using the inbuilt drawing functions of pygame. A YouTube video can be [found here](http://youtu.be/cykgpQZ5iEU) of the program running in both windowed and fullscreen modes.

Update

The youtube video shows it running in Ubuntu - I've since switched to Debian as Ubuntu has a long-running bug that makes the keyboard unresponsive with applications that use fullscreen. So if you want to run this then don't use Ubuntu or Ubuntu-based distros.

To make it work in realtime (Debian):

$ sudo apt-get install cutecom socat pygame python-serial

$ sudo gpasswd --add $USER dialout

Then logout / reboot

$ socat -d -d pty,raw,echo=0 pty,raw,echo=0

This will give you the two virtual serial port addresses. Set PORT in dashboard.py to one, and in cutecom the other. Also, in cutecom -> baud rate -> 9600.

$ python dashboard.py

In cutecom you should see FF FF EF - reply with 10 and the dashboard.py window should come to life. cutecom -> send file -> test_data.hex file.

Currently the data displayed is MPH, RPM (large centre arcs), AAC, MAF, temperature and battery voltage. The script is actually streaming 14 data values but these are the most useful to display. Pressing f will make it go fullscreen, w will make it revert back to windowed mode.

