# Signal-Reader
This software will essentially read the most recent exported .csv data output from TinySA-App.exe, extract the highest dB along with its frequency and display it.
Afterwards the .csv file is moved to old_csv folder to be stored. You can choose to delete its contents if you wish.
Make sure to save the expoerted .csv file to the same folder as the signal-ready.py as it reads the local folder.


Authors:
[LouisT123](https://github.com/LouisT123)
[Kiyandere](https://github.com/Kiyandere)

Feel free to contact me at `DNguyen#0929` on Discord


#### TODO
- [ ] Compare frequency and decibel with SWR-Bridge's data in order to send data to RT21 to rotate the antenna towards the best position.
- [ ] Impliment frontrear.py, widebeam.py, maxgain.py
- [ ] Might need to impliment a script to read the .cvs file instead of putting it in maxgain.py

## Installation
Install [Python 3.9](https://www.python.org/downloads/release/python-390/) 
(Make sure it's added to PATH)


## Running the application
Go into the Signal-Reader folder and run it with terminal
```
python ./maxgain.py
```
Or you can just double click maxgain.py

## Different Modes
### Front/Rear
This mode find front to rear ratio of the antenna.

### Max Gain
This mode will take .cvs in the folder and find the frequecy with the highest gain and display it. You will also be able to compare different .cvs files and see which one has the highest gain at the frequency of your choosing.

You will also have an option to move the .cvs file to the old_csv folder or keep it there for comparison.

### Wide Beam
Due to time contrainst, the next capstone team will need to implement this feature.
