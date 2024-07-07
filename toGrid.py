#!/bin/python3

# Origin: https://github.com/plasmobit/toGrid
# Author: plasmobit
# (c) 2024, MIT License

# == About:
# Place the current window into a grid as described by the provided parameters.
# Designed to be used with custom system hotkeys!
# Note: Windows with size hints may have some offsets due to their size restrictions.

# == How to use:
# Ensure the script does not throw any errors (place the current window in the center of a 3-column grid [1|2|3]):
#   path-to-script/toGrid.py 3 2-2
# Otherwise, install the requirements: python3 (and module 'sh'), xdotool.
#
# Bind hotkeys to call the script on your Linux OS. Example for an ultrawide monitor:
# Full height columns:
#   super+shift+a      --> path-to-script/toGrid.py 7 1-2
#   super+shift+s      --> path-to-script/toGrid.py 7 3-5
#   super+shift+d      --> path-to-script/toGrid.py 7 6-7
# Address the top row:
#   super+ctrl+shift+a --> path-to-script/toGrid.py 7 1-2 T
#   super+ctrl+shift+s --> path-to-script/toGrid.py 7 3-5 T
#   super+ctrl+shift+d --> path-to-script/toGrid.py 7 6-7 T
# Address the bottom row:
#   super+alt+shift+a  --> path-to-script/toGrid.py 7 1-2 B
#   super+alt+shift+s  --> path-to-script/toGrid.py 7 3-5 B
#   super+alt+shift+d  --> path-to-script/toGrid.py 7 6-7 B
# Similarly, the super+[yxcv] keys can be used to address a 4-column grid, etc.



from sys import argv, exit
from sh import xdotool

deb = 0 # print debug infos

class Cfg:
  cols = 3
  colspan = [1, 1]
  vpos = None

  @staticmethod
  def init():
    Cfg.cols = int(argv[1])
    if not (1 < Cfg.cols < 25):
      raise ValueError("Invalid column definition, choose a number from 2 to 24")
    Cfg.colspan = [int(i) for i in argv[2].split("-")]
    if not (len(Cfg.colspan) == 2 and 1 <= Cfg.colspan[0] and Cfg.colspan[0] <= Cfg.colspan[1] and Cfg.colspan[1] <= Cfg.cols):
      raise ValueError(f"Invalid colum range! Try something between 1-{Cfg.cols}")
    Cfg.vpos = argv[3] if len(argv) == 4 else None
    if not (Cfg.vpos is None or Cfg.vpos in "TB"):
      raise ValueError("Invalid row modifier use T or B for top or bottom!")

  def __str__(self):
    return f"Columns: {self.cols}, Range: {self.colspan}, Vertical modifier: {self.vpos}"


def main():
  winId = int(xdotool("getactivewindow").strip())
  if not winId:
    raise ValueError("No active window found!")
  
  dspTxt = xdotool("getdisplaygeometry").strip()
  dspXY = [int(i) for i in dspTxt.split(" ")]
  if not (len(dspXY) == 2 and 80 <= dspXY[0] <= (1 << 21) and 80 <= dspXY[1] <= (1 << 20)):
    raise ValueError(f"Invalid display geometry: {dspTxt}")
  dx = dspXY[0] / Cfg.cols
  dy = dspXY[1] if Cfg.vpos is None else (dspXY[1] // 2)

  lastCol = Cfg.colspan[1] == Cfg.cols
  x = 1 + int((Cfg.colspan[0] - 1) * dx + 0.5)
  xEnd = int((Cfg.colspan[1]) * dx + 0.5)
  y = 1 if Cfg.vpos is None or Cfg.vpos == 'T' else dy
  width = xEnd - x if not lastCol else dspXY[0] - x
  height = dy

  if deb:
    print(f"Place {winId} on X at {x} + {width} to {x + width} ")
  xdotool("windowsize", winId, width, height, "windowmove", winId, x, y)
  if deb:
    print(xdotool("getwindowgeometry", winId))


usage = """USAGE: toGrid.py number_of_columns first_col-last_col [T,B]
    e.g.: "7 3-5 T" -- for a wide-center, occupying cols 3 to 5 in a 7-col grid on the (T)op half of the display."""

if __name__ == "__main__":
  if not (3 <= len(argv) <= 4):
    print(usage)
    exit(0)

  try:
    Cfg.init()
    main()
  except ValueError as e:
    print(f"Error: ", str(e))
    exit(1)

