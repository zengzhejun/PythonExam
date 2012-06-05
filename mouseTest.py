import subprocess

import win32ui,win32con,pythoncom,win32gui,win32process,win32api

import time

import string

from ctypes import *

##open mouse properties

process = subprocess.Popen("control.exe main.cpl")

time.sleep(1)

pwin = win32gui.FindWindow(0,'Mouse Properties')

text = win32gui.GetWindowText(pwin)

print(text)

def _windowEnumerationHandler(hwnd, resultList):

     '''Pass to win32gui.EnumWindows() to generate list of window handle,

     window text, window class tuples.'''

     ##print(win32gui.GetWindowText(hwnd))

     resultList.append((hwnd,

                        win32gui.GetWindowText(hwnd),

                        win32gui.GetClassName(hwnd)))

windows = []

win32gui.EnumChildWindows(pwin, _windowEnumerationHandler, windows)

isRight = 0

def ClickChildControl(hwnd):

     (left, top, right, bottom) = win32gui.GetWindowRect(hwnd)

     print(left,top,right,bottom)

     windll.user32.SetCursorPos(left + (right - left)/2, top + (bottom - top)/2)

     time.sleep(0.5)

     if isRight:

         win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)

         time.sleep(0.05)

         win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)

         time.sleep(0.05)

     else:

         win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)

         time.sleep(0.05)

         win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

         time.sleep(0.05)

wantText = "Switch primary and secondary buttons"

for hwnd, windowText, windowClass in windows:

     if wantText in windowText:

         print('switch')

         isRight = win32gui.SendMessage(hwnd, win32con.BM_GETCHECK, 0, 0)

         ClickChildControl(hwnd)

         isRight = not isRight


for hwnd, windowText, windowClass in windows:

     if 'OK' in windowText:

         print('Get Ok')

         ClickChildControl(hwnd)
