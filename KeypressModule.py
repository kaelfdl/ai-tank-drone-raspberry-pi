import curses
import time
import numpy as np

# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for keys

class Keypress():
    def __init__(self):

        self.screen  = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.screen.keypad(True)

        self.keys = np.zeros(4, dtype=np.int8)

    

    def get_key(self):
        char = self.screen.getch()

        flag = False
        

        if char == ord('w'):
            self.keys[0] = 1
        elif char == ord('a'):
            self.keys[1] = 1
        elif char == ord('s'):
            self.keys[2] = 1
        elif char == ord('d'):
            self.keys[3] = 1
        elif char == ord('q'):
            flag = True

        return flag

    # Close down curses properly and turn echo back on
    def cleanup(self):
        curses.nocbreak()
        self.screen.keypad(False)
        curses.echo()
        curses.endwin()



if __name__ == "__main__":

    keypress = Keypress()
    try:
        while True:
            if keypress.get_key():
                break
            print(keypress.keys) 
            keypress.keys *= 0
    finally:
        keypress.cleanup()
