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