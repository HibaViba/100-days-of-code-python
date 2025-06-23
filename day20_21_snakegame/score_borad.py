from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(r"C:\Users\HP\Desktop\data.txt") as file:
            contents = file.read()
        self.high_score = contents
        self.hideturtle()
        self.goto(0, 275)  # Position at the very top center
        self.color("white")
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High score : {self.high_score}", align="center",
                   font=("Courier", 16, "normal"))

    # game_over(self):
    # self.goto(0,0)
    # self.write("Game Over", align="center", font=("Courier", 16, "normal"))

    def reset(self):
        # with open("data.txt", "w") as file:
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open(r"C:\Users\HP\Desktop\data.txt", "w") as file:
                # C:\Users\HP\PycharmProjects\day20_21_snakegame\main.py
                # C:\Users\HP\Desktop\data.txt
                contents = file.write(str(self.high_score))
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score = self.score + 1
        self.update_score()
