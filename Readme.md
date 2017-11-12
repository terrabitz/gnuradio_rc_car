# HackRF RC Car Controller

This repository is for the Gnuradio-Companion code to create a simple
RC car controller, as well as a python companion file to allow use 
of the keyboard arrow keys. 

To run, first launch the `top_block.py` file, which should launch the 
main controller itself. You can use the provided buttons to controll 
the car. If you want to use the arrow keys, run the `car_replay_gui.py`
file in a separate process. This should interface with the original 
process over XMLRPC. 
