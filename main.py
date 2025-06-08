import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from ui_dicegame import Ui_MainWindow
from logic import DiceGameLogic


class DiceGame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.logic = DiceGameLogic()

        self.ui.rollButton.clicked.connect(self.roll_dice)
        self.ui.resetButton.clicked.connect(self.reset_game)

        self.ui.statusLabel.setText("მოთამაშე 1-ის ჯერია")
        self.ui.scorePlayer1.setText("0")
        self.ui.scorePlayer2.setText("0")

    def roll_dice(self):
        current_turn = self.logic.turn
        roll, message = self.logic.roll_for_current_player()

        # Update image
        dice_label = self.ui.diceImage1 if current_turn == 1 else self.ui.diceImage2
        pixmap = QPixmap(f"images/dice_{roll}.png")
        resized = pixmap.scaled(128, 128, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        dice_label.setPixmap(resized)

        self.ui.statusLabel.setText(message)

        result = self.logic.evaluate_round()
        if result:
            self.ui.statusLabel.setText(result)
            self.ui.scorePlayer1.setText(str(self.logic.score_p1))
            self.ui.scorePlayer2.setText(str(self.logic.score_p2))

    def reset_game(self):
        self.logic.reset_game()
        self.ui.scorePlayer1.setText("0")
        self.ui.scorePlayer2.setText("0")
        self.ui.diceImage1.clear()
        self.ui.diceImage2.clear()
        self.ui.statusLabel.setText("თამაში დაიწყო! მოთამაშე 1-ის ჯერია")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DiceGame()
    window.show()
    sys.exit(app.exec_())
