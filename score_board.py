from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 16, "bold")

class ScoreBoard(Turtle):
    def __init__(self):
        self.score = 0
        # get the high score from data file
        with open("data.txt") as data:
            highest_score = int(data.read())
        self.high_score = highest_score
        super().__init__()
        self.goto(0, 270)
        self.penup()
        self.hideturtle()
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def get_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.score))
        self.score = 0
        self.update_scoreboard()