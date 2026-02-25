---

# PYRAIN

A terminal-based rain animation ported to Python from the original C++ implementation by Oakamoore.

---

## Overview

**PYRAIN** simulates a rainfall effect in the terminal. This project is a Python port of the C++ terminal-based rain visualization originally developed by [Oakamoore/terminal-rain](https://github.com/Oakamoore/terminal-rain). It features depth perception through different characters and colors, and dynamically scales the number of drops based on the terminal window size.

<img width="1919" height="1080" alt="image" src="https://github.com/user-attachments/assets/7c5edf98-da64-41ee-b200-29d4e37df002" />


---

## Key Features

* **Depth Perception**: Simulates three visual planes using different characters and colors to create a 3D effect.
* **Dynamic Scaling**: Rain density automatically adjusts based on your terminal width.
* **Responsive Design**: The animation automatically detects terminal resize events and adjusts the drop count and screen buffer accordingly.
* **Lightweight**: Optimized using the `curses` library for minimal resource consumption.

---

## Logic and Implementation

The program follows a modular design divided into two main components:

### 1. Depth Simulation

To create the depth effect, the program assigns attributes based on "distance" using different characters (`|`, `:`, `.`) and color intensities:

| Layer | Character | Color | Speed | Visual Effect |
| --- | --- | --- | --- | --- |
| **Close** | ` | ` | White | Fast |
| **Mid** | `:` | Cyan | Medium | Midground |
| **Far** | `.` | Blue | Slow | Background |

### 2. Density Algorithm

The system calculates the number of drops ($N$) based on the terminal width using a $0.75$ coefficient:

$$N = \text{terminal width} \times 0.75$$

---

## Installation and Usage

### Prerequisites

* **Python 3.x**.
* A terminal supporting colors and the `curses` library.

### Configuration

1. Place `drop.py` and `main.py` in the same directory.
2. **Windows Users**: You must install the `windows-curses` package:
```bash
pip install windows-curses

```



### Execution

Run the application from your terminal:

```bash
python main.py

```

---

## Controls

* **Q / Escape**: Exit the application.
* **Resize**: The animation automatically adjusts to window dimensions.

---

## File Structure

* **drop.py**: Defines the `Drop` class, which handles properties like position, speed, and character representation.
* **main.py**: Contains the `Rain` engine and the main execution loop, managing terminal initialization and frame rate.

---

## Credits

This program is based on the C++ project [terminal-rain](https://github.com/Oakamoore/terminal-rain) by Oakamoore, which was inspired by nkleemann's implementation in C.

---
