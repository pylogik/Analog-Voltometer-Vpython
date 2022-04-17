# Analog-Voltometer-Vpython
Homework from Paul Mcwhorter. Using an Arduino with Python Lesson 4.
https://www.youtube.com/watch?v=4IqqXXMARr8&list=PLGs0VKk2DiYzWURfJCbCGPa8HI0APjBfo&index=4

##What is it?
This is an analog voltometer that is virtually displayed on the computers monitor. There is a potitiometer hooked up to an arduino; The device is connected to a computer, through USB. The results of the arduino are represented on the computer.

##How Does it Work?
There are two seprate scripts, or files. One is written in Arduino C; This is uploaded to the arduino. The final script is wriiten in Python 3.10. The script written in Python can be executed from the computer with the command "python3 <file_name>". The voltometer will open from your default browser. I could not get Vpython, a module used in the python script, to work properly with certain browsers, Firefox works fine out-of-the-box, chrome is recomeded by Vpython documentation.
