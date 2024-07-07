# About

A simple script to place the current window into a virtual display grid as described by the provided parameters. 

Designed to be used on ultrawide monitors with custom system hotkeys!

*Note*: Windows with active size hints may have some offsets due to their size restrictions.

# How to use

Install the requirements:
  * python3 (and the module 'sh')
  * xdotool

Ensure the script does not throw any errors and is working as expected by executing in a consol:  
*(place the current window in the center of a 3-column grid [1|2|3], wait, place in the center of a 4-column grid [1|2|3|4])*:
```
./toGrid.py 3 2-2
sleep 1
./toGrid.py 4 2-3
```

Bind custom hotkeys in the window manager on your Linux OS to call the script with different grid and placement parameters.

## Example configuration

Here we use a virtual 7-columns grid for an ultrawide monitor to make the center area a bit wider (3-columns) than the left and right side panels (2-coluns).
So the panels will occupy 2+3+2 columns of the screen.
```
+-+-+-+-+-+-+-+
|1|2|3|4|5|6|7|
+-+-+-+-+-+-+-+
```

Full height columns:
```
Areas in the virtual 7-col grid:
+---+-----+---+
|1 2|3 4 5|6 7|
+---+-----+---+

Hotkey mapping:
super+shift+a      --> path-to-script/toGrid.py 7 1-2
super+shift+s      --> path-to-script/toGrid.py 7 3-5
super+shift+d      --> path-to-script/toGrid.py 7 6-7
```

Address the top row:
```
Areas in the virtual 7-col grid on the top half of the screen:
+---+-----+---+
|1 2|3 4 5|6 7|
|   |     |   |
+---+-----+---+

Hotkey mapping:
super+ctrl+shift+a --> path-to-script/toGrid.py 7 1-2 T
super+ctrl+shift+s --> path-to-script/toGrid.py 7 3-5 T
super+ctrl+shift+d --> path-to-script/toGrid.py 7 6-7 T
```

Address the bottom row:
```
Areas in the virtual 7-col grid on the bottom half of the screen:
+---+-----+---+
|   |     |   |
|1 2|3 4 5|6 7|
+---+-----+---+

Hotkey mapping:
super+alt+shift+a  --> path-to-script/toGrid.py 7 1-2 B
super+alt+shift+s  --> path-to-script/toGrid.py 7 3-5 B
super+alt+shift+d  --> path-to-script/toGrid.py 7 6-7 B
```

Similarly, the super+[zxcv] keys can be used to address a 4-column grid, etc.