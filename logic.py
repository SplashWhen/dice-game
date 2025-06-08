import random

class DiceGameLogic:
    def __init__(self):
        self.score_p1 = 0
        self.score_p2 = 0
        self.turn = 1
        self.last_roll_p1 = None
        self.last_roll_p2 = None

    def roll_for_current_player(self):
        roll = random.randint(1, 6)
        if self.turn == 1:
            self.last_roll_p1 = roll
            self.turn = 2
            return roll, "მოთამაშე 1-მა გააგორა"
        else:
            self.last_roll_p2 = roll
            self.turn = 1
            return roll, "მოთამაშე 2-მ გააგორა"

    def evaluate_round(self):
        if self.last_roll_p1 is not None and self.last_roll_p2 is not None:
            if self.last_roll_p1 > self.last_roll_p2:
                self.score_p1 += 1
                result = "მოთამაშე 1-მა მოიგო რაუნდი!"
            elif self.last_roll_p2 > self.last_roll_p1:
                self.score_p2 += 1
                result = "მოთამაშე 2-მ მოიგო რაუნდი!"
            else:
                result = "ფრეა!"

            self.last_roll_p1 = None
            self.last_roll_p2 = None

            return result
        return ""

    def reset_game(self):
        self.score_p1 = 0
        self.score_p2 = 0
        self.turn = 1
        self.last_roll_p1 = None
        self.last_roll_p2 = None
