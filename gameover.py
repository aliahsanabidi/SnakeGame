#Using Scoreboard as super class and changing the position and text to mention game over in the center

from scoreboard import Scoreboard
ALIGNMENT = "center"
FONT = ("Courier", 15, "bold")

class Gameover(Scoreboard):
    def __init__(self):
        super().__init__()
        self.clear()
        self.goto(0,0)
        self.write("Game Over!", align=ALIGNMENT, font=FONT)