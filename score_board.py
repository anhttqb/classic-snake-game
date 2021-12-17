from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 16, "bold")

class ScoreBoard(Turtle):
    def __init__(self):
        self.score = 0
        super().__init__()
        self.goto(0, 270)
        self.penup()
        self.hideturtle()
        self.color("white")
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def get_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.home()
        self.write("Game Over!", align=ALIGNMENT, font=FONT)