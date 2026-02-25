import curses
import time
from drop import Drop

class Rain:
    def __init__(self):
        self.drops = []
        self.drop_coefficient = 0.75

    def resize(self, max_x, max_y):
        num_drops = int(max_x * self.drop_coefficient)
        
        if len(self.drops) < num_drops:
            for _ in range(num_drops - len(self.drops)):
                self.drops.append(Drop(max_x, max_y))
        elif len(self.drops) > num_drops:
            self.drops = [d for d in self.drops if d.x < max_x]
            
        for drop in self.drops:
            drop.update_bounds(max_x, max_y)

    def run(self, stdscr):
        curses.curs_set(0)
        stdscr.nodelay(True)
        curses.start_color()
        
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)

        max_y, max_x = stdscr.getmaxyx()
        self.resize(max_x, max_y)

        while True:
            key = stdscr.getch()
            if key in [ord('q'), ord('Q'), 27]:
                break

            current_y, current_x = stdscr.getmaxyx()
            if (current_y, current_x) != (max_y, max_x):
                max_y, max_x = current_y, current_x
                stdscr.clear()
                self.resize(max_x, max_y)

            stdscr.erase()
            
            for drop in self.drops:
                drop.draw(stdscr)
                drop.fall()

            stdscr.refresh()
            time.sleep(0.03)

if __name__ == "__main__":
    rain = Rain()
    curses.wrapper(rain.run)