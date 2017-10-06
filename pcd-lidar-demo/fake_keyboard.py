#!/usr/bin/env python
from __future__ import division
from __future__ import print_function
import time
import keyboard



switch_workspaces = True 

def check_toggle_key(e):
    global switch_workspaces
    for code in keyboard._pressed_events:
        if str(code) == '41':
            switch_workspaces = not switch_workspaces
            time.sleep(1)


def main():
    global switch_workspaces
    keyboard.on_press(check_toggle_key)
    while True:

        if switch_workspaces: 
            keyboard.press_and_release('win+4')
            time.sleep(15)
            keyboard.press_and_release('win+5')
            time.sleep(15)
            keyboard.press_and_release('win+6')
            time.sleep(30)
         

if __name__ == '__main__':

    try:
        main()
    except KeyboardInterrupt:
        print('Bye bye!')
