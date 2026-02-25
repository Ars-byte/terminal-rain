```markdown
# PYRAIN

A terminal-based rain animation ported to Python from the original C++ implementation by Oakamoore.

---

## Overview

PYRAIN simulates a rainfall effect in the terminal. This project is a Python port of the C++ terminal-based rain visualisation originally developed by [Oakamoore/terminal-rain](https://github.com/Oakamoore/terminal-rain). It features depth perception through different characters and colors, and dynamically scales the number of drops based on the terminal window size.

## Logic and Implementation

The program follows a modular design divided into two main components:

* **Depth Simulation**: Raindrops use different characters (`|`, `:`, `.`) and color intensities to represent distance.
* **Dynamic Scaling**: The system calculates the number of drops based on the terminal width using a $0.75$ coefficient.
* **Responsive Design**: The animation automatically detects terminal resize events and adjusts the drop count and screen buffer accordingly.

## File Structure

* **drop.py**: Defines the `Drop` class, which handles properties like position, speed, and character representation.
* **main.py**: Contains the `Rain` engine and the main execution loop, managing terminal initialization and frame rate.

## Requirements

* Python 3.x
* A terminal supporting colors and the `curses` library.
* **Windows Users**: Install the `windows-curses` package:
  ```bash
  pip install windows-curses

```

## Usage

1. Place `drop.py` and `main.py` in the same directory.
2. Run the application:
```bash
python main.py

```



## Controls

* **Q / Escape**: Exit the application.
* **Resize**: The animation automatically adjusts to window dimensions.

## Credits

This program is based on the C++ project [terminal-rain](https://github.com/Oakamoore/terminal-rain) by Oakamoore, which was inspired by nkleemann's implementation in C.

```

---

### 2. drop.py

```python
import random
import curses

class Drop:
    CHARACTERS = ['|', ':', '.']
    
    def __init__(self, max_x, max_y):
        self.max_x = max_x
        self.max_y = max_y
        self.reset()

    def reset(self):
        self.x = random.randint(0, max(0, self.max_x - 1))
        self.y = 0
        self.distance_idx = random.randint(0, len(self.CHARACTERS) - 1)
        self.char = self.CHARACTERS[self.distance_idx]
        self.speed = random.randint(1, 3)
        self.color_pair = self.distance_idx + 1 

    def draw(self, stdscr):
        try:
            if 0 <= self.y < self.max_y and 0 <= self.x < self.max_x:
                stdscr.addch(int(self.y), self.x, self.char, curses.color_pair(self.color_pair))
        except curses.error:
            pass

    def fall(self):
        if self.y >= self.max_y:
            self.reset()
        else:
            self.y += self.speed

    def update_bounds(self, max_x, max_y):
        self.max_x = max_x
        self.max_y = max_y

```

---

### 3. main.py

```python
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

```
