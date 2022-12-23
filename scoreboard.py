from turtle import Turtle
FONT = ("bold", 20, "normal")
level = 1


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed(0)
        self.goto(-270, 250)
        self.write(f"level {level}", align="left", font=FONT)

    def update_scoreboard(self, levels):
        self.clear()
        self.write(f"level {levels}", align="left", font=FONT)

    def game_over(self):
        self.goto(-100, 0)
        self.color("red")
        self.write("GAME OVER", align="left", font=("bold", 30, "normal"))


