K11Consult
==========

A python project to interact with the ECU of Nissan vehicles that utilise the Nissan Consult protocol.

The protocol reads and writes hex via a serial connection, with dashboard.py sending the commands and reading in realtime the resultant data stream from the ECU. The script is essentially in two parts; a non blocking thread that interacts with the ECU, and a gui using pygame that displays the data in the style of a dashboard. There are no external images used as I've written this for minimal CPU usage and to show what's possible using the drawing commands of pygame - although it does use pygame.gfxdraw for drawing arcs, something that pygame doesn't support. A YouTube video can be [found here](http://youtu.be/cykgpQZ5iEU) of the program running in both windowed and fullscreen modes.

To make it work (ubuntu):

$ sudo apt-get install gtkterm socat

$ sudo gpasswd --add $USER dialout

Then logout / reboot

$ socat -d -d pty,raw,echo=0 pty,raw,echo=0

This will give you the two virtual serial port addresses. Set PORT in dashboard.py to one, and in gtkterm the other. Also, in gtkterm -> view set to hexidecimal, and also select send hexidecimal data. 

$ python dashboard.py

In gtkterm you should see FF FF EF - reply with 10 and the dashboard.py window should come to life. Gtkterm -> File -> send raw file, select the test_data.hex file.

Currently the data displayed is MPH, RPM (large centre arcs), AAC, MAF, temperature and battery voltage. The script is actually streaming 14 data values but these are the most useful to display. Pressing f will make it go fullscreen, w will make it revert back to windowed mode.

