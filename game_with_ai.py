from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap, QPainter
from util import MainWindow
from home_page import HOME
from PyQt6.QtWidgets import (
    QApplication, QWidget,
    QGridLayout, QVBoxLayout, QPushButton,
    QLabel, QSizePolicy, QHBoxLayout,
)


# change superclass to canvas
class AIGAME(MainWindow):
    def __init__(self):
        super().__init__()  # initializes the parent class's attributes

        self.title_bar.setVisible(False)  # hides title bar to avoid duplicates

        self.is_game_over = False # checks if it's game over after human moves. If it is (True), stops the AI from moving

        # sets the work space to be a horizontal layout of 3x3 grid layout (nested) and 1x2 grid layout (nested)
        self.work_space_layout = QHBoxLayout()
        self.work_space_layout.setContentsMargins(11, 11, 11, 11)
        self.canvas.canvas_layout.addLayout(self.work_space_layout)  # add work space horizontal layout to the centra_widget_layout (QVBoxLayout) in the parent (MainWindow) class

        grid_layout = QGridLayout()  # create a grid layout for the tic tac toe grid (3x3)

        # make 9 buttons with object name 'grid' to set the styleSheet in one go.
        # When pressed, it will start an event whose functionality will be created in a subclass
        self.button1 = QLabel()
        self.button1.setObjectName("grid")
        self.button2 = QLabel()
        self.button2.setObjectName("grid")
        self.button3 = QLabel()
        self.button3.setObjectName("grid")
        self.button4 = QLabel()
        self.button4.setObjectName("grid")
        self.button5 = QLabel()
        self.button5.setObjectName("grid")
        self.button6 = QLabel()
        self.button6.setObjectName("grid")
        self.button7 = QLabel()
        self.button7.setObjectName("grid")
        self.button8 = QLabel()
        self.button8.setObjectName("grid")
        self.button9 = QLabel()
        self.button9.setObjectName("grid")

        # sets the stylesheet for all widgets with object names)
        self.setStyleSheet("#grid {background: transparent; border: 3px solid black;} "
                           "#grid:hover {background: green;}"
                           "#player {background: transparent; border: 3px solid black;}"
                           "#turn_color_green {background: green; border: 0px; margin: 15px;}"
                           "#turn_color_red {background: red; border: 0px; margin: 15px;}"
                           "#image_player_setting {margin:10px}"
                           )

        # Add a size policy to the label
        self.button1.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.button2.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.button3.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.button4.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.button5.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.button6.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.button7.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.button8.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.button9.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        # adds 9 widgets into the allocated slots in the 3x3 grid layout
        grid_layout.addWidget(self.button1, 0, 0)
        grid_layout.addWidget(self.button2, 0, 1)
        grid_layout.addWidget(self.button3, 0, 2)
        grid_layout.addWidget(self.button4, 1, 0)
        grid_layout.addWidget(self.button5, 1, 1)
        grid_layout.addWidget(self.button6, 1, 2)
        grid_layout.addWidget(self.button7, 2, 0)
        grid_layout.addWidget(self.button8, 2, 1)
        grid_layout.addWidget(self.button9, 2, 2)

        # created a widget for the left part of the work space layout (QHBoxLayout)
        grid1 = QWidget()
        grid1.setLayout(grid_layout)  # adds the 3x3 grid layout into the grid1 widget

        # created a 1x2 grid layout for the player id grid
        player_layout = QGridLayout()
        self.labelp1 = QLabel()  # first player label
        self.labelp1.setObjectName("player")
        self.labelp2 = QLabel()  # second player label
        self.labelp2.setObjectName("player")

        # sets the size policy for the 2x1 grid layout
        self.labelp1.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.labelp2.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        # adds the 2 label widgets into the 2x1 grid layout
        player_layout.addWidget(self.labelp1, 0, 0)
        player_layout.addWidget(self.labelp2, 0, 1)

        # creates a QVBoxLayout for the leftmost box in the 2x1 grid (player 1 layout)
        self.p1_inner_layout = QVBoxLayout()

        # adds player 1 identity image (cross) into the leftmost box in the 2x1 layout grid
        self.label_inner_p1 = QLabel()
        self.label_inner_p1.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.label_inner_p1.setObjectName('image_player_setting')
        self.draw_cross(self.label_inner_p1)
        self.p1_inner_layout.addWidget(self.label_inner_p1)

        # adds the 'PLAYER 1' label to the box
        self.label_inner_p1_id = QLabel("PLAYER 1")
        self.label_inner_p1_id.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        font = QFont()
        font.setPointSize(50)  # Set the font size to 50
        self.label_inner_p1_id.setFont(font)
        self.label_inner_p1_id.setObjectName('text_default')
        self.p1_inner_layout.addWidget(self.label_inner_p1_id)

        # adds color to indicate turns. Green indicates it's the particular player's turn
        # Every turn, the color will switch from green to red and vice versa
        self.label_inner_initial_turn_color1 = QLabel()
        self.label_inner_initial_turn_color1.setObjectName('turn_color_green')
        self.label_inner_initial_turn_color1.setFixedHeight(300)
        self.label_inner_initial_turn_color1.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.p1_inner_layout.addWidget(self.label_inner_initial_turn_color1)

        # creates a QVBoxLayout for the leftmost box in the 2x1 grid (player 1 layout)
        self.p2_inner_layout = QVBoxLayout()

        # adds player 2 identity image (circle) into the rightmost box in the 2x1 layout grid
        self.label_inner_p2 = QLabel()
        self.label_inner_p2.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.label_inner_p2.setObjectName('image_player_setting')
        self.draw_circle(self.label_inner_p2)
        self.p2_inner_layout.addWidget(self.label_inner_p2)

        # adds the 'PLAYER 2' label to the box
        self.label_inner_p2_id = QLabel("PLAYER 2")
        self.label_inner_p2_id.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        font = QFont()
        font.setPointSize(50)  # Set the font size to 55
        self.label_inner_p2_id.setFont(font)
        self.label_inner_p2_id.setObjectName('text_default')
        self.p2_inner_layout.addWidget(self.label_inner_p2_id)

        # adds color to indicate turns. Red indicates it's not the particular player's turn
        # Every turn, the color will switch from red to green and vice versa
        self.label_inner_initial_turn_color2 = QLabel()
        self.label_inner_initial_turn_color2.setObjectName('turn_color_red')
        self.label_inner_initial_turn_color2.setFixedHeight(300)
        self.label_inner_initial_turn_color2.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.p2_inner_layout.addWidget(self.label_inner_initial_turn_color2)

        player_layout.addLayout(self.p1_inner_layout, 0, 0)  # adds the QVBoxLayout into the parent layout (player layout)
        player_layout.addLayout(self.p2_inner_layout, 0, 1)  # adds the QVBoxLayout into the parent layout (player layout)

        # created a widget as a container for the 2x1 player grid layout and add player_layout into the widget
        grid2 = QWidget()
        grid2.setLayout(player_layout)

        # adds the widget containing the 3x3 grid layout
        # and the widget containing 2x1 grid layout
        # into the work space layout (QHBoxLayout)
        self.work_space_layout.addWidget(grid1)
        self.work_space_layout.addWidget(grid2)

    def draw_cross(self, label):
        # creates a method to draw a cross using QPixmap (transparent background)
        pixmap = QPixmap(325, 325)
        pixmap.fill(Qt.GlobalColor.transparent)
        painter = QPainter(pixmap)
        pen = painter.pen()
        pen.setColor(Qt.GlobalColor.white)
        pen.setWidth(20)
        painter.setPen(pen)

        # draws the cross
        painter.drawLine(10, 10, 315, 315)
        painter.drawLine(10, 315, 315, 10)

        painter.end()  # releases any resources associated with 'painter'

        # associates the pixmap image to the label and shows the image on the label
        label.setPixmap(pixmap)

    def draw_circle(self, label):
        # creates a method to draw a circle using QPixmap (transparent background)
        pixmap = QPixmap(325, 325)
        pixmap.fill(Qt.GlobalColor.transparent)
        painter = QPainter(pixmap)
        pen = painter.pen()
        pen.setColor(Qt.GlobalColor.white)
        pen.setWidth(20)
        painter.setPen(pen)

        # draws the circle
        painter.drawEllipse(10, 10, 305, 305)

        painter.end()  # releases any resources associated with 'painter'

        # associates the pixmap image to the label and shows the image on the label
        label.setPixmap(pixmap)


class AIGAMESTART(AIGAME):
    def __init__(self):
        super().__init__()  # initializes the parent class's attributes
        self.turn = 'p1'  # marks whose turn right now
        self.cross = 'cross'
        self.circle = 'circle'
        self.result = None  # cross when cross wins, circle when circle wins, None when tie
        # dummy variable for current state check
        # When False and all boxes are filled, it's tie.
        # If it's True, then there's a winner
        self.dummy = False

        # dummy variable for AI recursive future possibilities check
        # When False and all boxes are filled, it's tie.
        # If it's True, then there's a winner
        self.dummy2 = False

        # creates a dictionary to keep track the marks of each boxes as the current game state
        self.button_marks = {
            'button1': None, 'button2': None, 'button3': None,
            'button4': None, 'button5': None, 'button6': None,
            'button7': None, 'button8': None, 'button9': None
        }

        # creates a dictionary to connect the AI with the appropriate button
        self.button_marker_for_ai = {
            'self.button1': self.button1, 'self.button2': self.button2, 'self.button3': self.button3,
            'self.button4': self.button4, 'self.button5': self.button5, 'self.button6': self.button6,
            'self.button7': self.button7, 'self.button8': self.button8, 'self.button9': self.button9
        }

        # marks each button as initially not clicked
        self.button1.clicked = False; self.button2.clicked = False; self.button3.clicked = False
        self.button4.clicked = False; self.button5.clicked = False; self.button6.clicked = False
        self.button7.clicked = False; self.button8.clicked = False; self.button9.clicked = False

        # when any of the button is clicked, the lambda function is triggered
        self.button1.mousePressEvent = lambda event: self.click_tictactoe_grid_and_change_turn(self.button1, 'button1')
        self.button2.mousePressEvent = lambda event: self.click_tictactoe_grid_and_change_turn(self.button2, 'button2')
        self.button3.mousePressEvent = lambda event: self.click_tictactoe_grid_and_change_turn(self.button3, 'button3')
        self.button4.mousePressEvent = lambda event: self.click_tictactoe_grid_and_change_turn(self.button4, 'button4')
        self.button5.mousePressEvent = lambda event: self.click_tictactoe_grid_and_change_turn(self.button5, 'button5')
        self.button6.mousePressEvent = lambda event: self.click_tictactoe_grid_and_change_turn(self.button6, 'button6')
        self.button7.mousePressEvent = lambda event: self.click_tictactoe_grid_and_change_turn(self.button7, 'button7')
        self.button8.mousePressEvent = lambda event: self.click_tictactoe_grid_and_change_turn(self.button8, 'button8')
        self.button9.mousePressEvent = lambda event: self.click_tictactoe_grid_and_change_turn(self.button9, 'button9')

    def click_tictactoe_grid_and_change_turn(self, button, which):
        if not button.clicked:  # checks if the button has been clicked. If it's been clicked, there's an x or o mark. If it's not clicked, proceed
            button.clicked = True  # change the button to clicked
            self.show_cross(button)  # creates cross on the button
            self.button_marks[which] = self.cross  # updates the value of the button in the dictionary to cross
            self.check_game()  # checks if it's a win, lose, tie, or the game goes on

            # every time the turn changes, the color indicator changes. Green means it's the player's turn
            self.setStyleSheet(super().styleSheet() +
                               "#turn_color_green {background: red;}" +
                               "#turn_color_red {background: green;}"
                               )

            self.setStyleSheet(super().styleSheet() + "#grid:hover {background: transparent;}")
            self.check_game()

            if self.is_game_over == True: # if cross already wins (True), stops the execution of this function
                return

            # copies the button_marks dict for the AI to keep track of the future possibilities
            # indicated by 'board' variable in the minimax algorithm function
            button_marker_dict_temp = self.button_marks.copy()
            self.ai_step_for_marker = self.get_best_move(button_marker_dict_temp) # calculates the best move for the AI to make

            # gets the variable of the best move button and shows the circle on the GUI on that button
            self.ai_step_for_display = self.button_marker_for_ai[f'self.{self.ai_step_for_marker}']
            self.show_circle(self.ai_step_for_display)

            # updates the dictionary used by the game to keep track of current game state
            self.button_marks[self.ai_step_for_marker] = self.circle

            self.check_game() # checks if it's a win, lose, tie, or the game goes on

            # every time the turn changes, the color indicator changes. Green means it's the player's turn
            self.setStyleSheet(super().styleSheet() +
                               "#turn_color_green {background: green;}" +
                               "#turn_color_red {background: red;}"
                               )
            self.setStyleSheet(super().styleSheet() + "#grid:hover {background: green;}")

    def show_cross(self, button):
        # creates a method to draw a cross using QPixmap (transparent background)
        pixmap = QPixmap(200, 200)
        pixmap.fill(Qt.GlobalColor.transparent)
        painter = QPainter(pixmap)
        pen = painter.pen()
        pen.setColor(Qt.GlobalColor.white)
        pen.setWidth(10)
        painter.setPen(pen)

        # draws the cross
        painter.drawLine(10, 10, 190, 190)
        painter.drawLine(10, 190, 190, 10)

        painter.end()  # releases any resources associated with 'painter'

        button.setAlignment(Qt.AlignmentFlag.AlignCenter)
        button.setContentsMargins(0, 0, 0, 0)

        # associates the pixmap image to the label and shows the image on the label
        button.setPixmap(pixmap)

    def show_circle(self, button):
        # creates a method to draw a circle using QPixmap (transparent background)
        pixmap = QPixmap(200, 200)
        pixmap.fill(Qt.GlobalColor.transparent)
        painter = QPainter(pixmap)
        pen = painter.pen()
        pen.setColor(Qt.GlobalColor.white)
        pen.setWidth(10)
        painter.setPen(pen)

        # draws the circle
        painter.drawEllipse(10, 10, 180, 180)

        painter.end()  # releases any resources associated with 'painter'

        button.setAlignment(Qt.AlignmentFlag.AlignCenter)
        button.setContentsMargins(0, 0, 0, 0)

        # associates the pixmap image to the label and shows the image on the label
        button.setPixmap(pixmap)

    def check_game(self):
        # horizontal check
        for i in range(3):
            if (self.button_marks[f'button{i * 3 + 1}'] == self.button_marks[f'button{i * 3 + 2}'] == self.button_marks[
                f'button{i * 3 + 3}']) and self.button_marks[f'button{i * 3 + 1}'] is not None:
                self.result = self.button_marks[f'button{i * 3 + 1}']
                self.dummy = True  # when self.dummy == True, that means there's a winner
                # If there's a winner, all 9 buttons are inaccessible
                self.button1.mousePressEvent = lambda event: None
                self.button2.mousePressEvent = lambda event: None
                self.button3.mousePressEvent = lambda event: None
                self.button4.mousePressEvent = lambda event: None
                self.button5.mousePressEvent = lambda event: None
                self.button6.mousePressEvent = lambda event: None
                self.button7.mousePressEvent = lambda event: None
                self.button8.mousePressEvent = lambda event: None
                self.button9.mousePressEvent = lambda event: None
                # change the hover background of the button = transparent
                # purpose is to make it look like it's not clickable
                self.setStyleSheet(super().styleSheet() + "#grid:hover {background: transparent;}")

        # vertical check
        for i in range(3):
            if (self.button_marks[f'button{i + 1}'] == self.button_marks[f'button{i + 4}'] == self.button_marks[
                f'button{i + 7}']) and self.button_marks[f'button{i + 1}'] is not None:
                self.result = self.button_marks[f'button{i + 1}']
                self.dummy = True  # when self.dummy == True, that means there's a winner
                # If there's a winner, all 9 buttons are inaccessible
                self.button1.mousePressEvent = lambda event: None
                self.button2.mousePressEvent = lambda event: None
                self.button3.mousePressEvent = lambda event: None
                self.button4.mousePressEvent = lambda event: None
                self.button5.mousePressEvent = lambda event: None
                self.button6.mousePressEvent = lambda event: None
                self.button7.mousePressEvent = lambda event: None
                self.button8.mousePressEvent = lambda event: None
                self.button9.mousePressEvent = lambda event: None
                # change the hover background of the button = transparent
                # purpose is to make it look like it's not clickable
                self.setStyleSheet(super().styleSheet() + "#grid:hover {background: transparent;}")

        # diagonal check 1
        if (self.button_marks["button1"] == self.button_marks["button5"] == self.button_marks["button9"]) and \
                self.button_marks['button1'] is not None:
            self.result = self.button_marks["button1"]
            self.dummy = True  # when self.dummy == True, that means there's a winner
            # If there's a winner, all 9 buttons are inaccessible
            self.button1.mousePressEvent = lambda event: None
            self.button2.mousePressEvent = lambda event: None
            self.button3.mousePressEvent = lambda event: None
            self.button4.mousePressEvent = lambda event: None
            self.button5.mousePressEvent = lambda event: None
            self.button6.mousePressEvent = lambda event: None
            self.button7.mousePressEvent = lambda event: None
            self.button8.mousePressEvent = lambda event: None
            self.button9.mousePressEvent = lambda event: None
            # change the hover background of the button = transparent
            # purpose is to make it look like it's not clickable
            self.setStyleSheet(super().styleSheet() + "#grid:hover {background: transparent;}")

        # diagonal check 2
        if (self.button_marks['button3'] == self.button_marks['button5'] == self.button_marks['button7']) and \
                self.button_marks['button3'] is not None:
            self.result = self.button_marks["button3"]
            self.dummy = True  # when self.dummy == True, that means there's a winner
            # If there's a winner, all 9 buttons are inaccessible
            self.button1.mousePressEvent = lambda event: None
            self.button2.mousePressEvent = lambda event: None
            self.button3.mousePressEvent = lambda event: None
            self.button4.mousePressEvent = lambda event: None
            self.button5.mousePressEvent = lambda event: None
            self.button6.mousePressEvent = lambda event: None
            self.button7.mousePressEvent = lambda event: None
            self.button8.mousePressEvent = lambda event: None
            self.button9.mousePressEvent = lambda event: None
            # change the hover background of the button = transparent
            # purpose is to make it look like it's not clickable
            self.setStyleSheet(super().styleSheet() + "#grid:hover {background: transparent;}")

        # If self.dummy == False, that means there's no winner (3 in a row, column, or diagonal)
        # Second condition checks if all boxes are filled
        # If both conditions are fulfilled, the result is a tie
        if self.dummy == False and all(self.button_marks.values()):
            self.result = 'tie'

        # calls the function that will handle the behavior when the result has been known
        self.game_over_event()

    def game_over_event(self):
        # Creates a label to be filled with "Player 1 or 2 wins"
        self.over_label1 = QLabel()
        self.over_label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.over_label1.setObjectName('over_label1')
        self.over_label1.setStyleSheet('#over_label1 {color:white; font-size:30pt;}')
        self.over_layout1 = QVBoxLayout()
        self.over_layout1.addWidget(self.over_label1)

        # Creates a label to be filled with "Player 1 or 2 wins"
        self.over_label2 = QLabel()
        self.over_label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.over_label2.setObjectName('over_label2')
        self.over_label2.setStyleSheet('#over_label2 {color:white; font-size:30pt;}')
        self.over_layout2 = QVBoxLayout()
        self.over_layout2.addWidget(self.over_label2)

        # Creates a label to ask if the player wants to play again
        self.try_again = QLabel('Play Again?')
        self.try_again.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.try_again.setObjectName('try_question')
        self.try_again.setStyleSheet('#try_question {color:white; font-size:30pt}')

        # Creates a button that handles the behavior when the player wants to play again
        self.yes_try = QPushButton('Yes')
        self.yes_try.setObjectName('yes')
        self.yes_try.setStyleSheet('#yes {border:5px solid green; color:white; font-size:30pt}'
                                   '#yes:hover {background-color: green; border:2px solid green; color:white; font-size:30pt}'
                                   )

        self.yes_try.clicked.connect(self.play_again)  # calls the play_again function

        # Creates a button that handles the behavior when the player doesn't want to play again
        self.no_try = QPushButton('No')
        self.no_try.setObjectName('no')
        self.no_try.setStyleSheet('#no {border:5px solid green; color:white; font-size:30pt}'
                                  '#no:hover {background-color: green; border:2px solid green; color:white; font-size:30pt}'
                                  )

        self.no_try.clicked.connect(self.back_to_home_page)  # calls the back_to_home_page function

        # handles the display when player 1 wins
        if self.result == 'cross':
            self.over_label1.setText('Player 1 Wins')

            self.over_layout1.addWidget(self.try_again)
            self.over_layout1.addWidget(self.yes_try)
            self.over_layout1.addWidget(self.no_try)

            self.label_inner_initial_turn_color1.setLayout(self.over_layout1)
            # sets to True when game is over with player 1 as the winner
            # the purpose is to stop the AI from executing its move
            self.is_game_over = True

        # handles the display when player 2 wins
        if self.result == 'circle':
            self.over_label2.setText('Player 2 Wins')

            self.over_layout2.addWidget(self.try_again)
            self.over_layout2.addWidget(self.yes_try)
            self.over_layout2.addWidget(self.no_try)

            self.label_inner_initial_turn_color2.setLayout(self.over_layout2)

        # handles the display when the game ends with a tie
        if self.result == 'tie':
            self.over_label1.setText('It\'s a tie')
            self.over_label2.setText('It\'s a tie')

            self.over_layout1.addWidget(self.try_again)
            self.over_layout1.addWidget(self.yes_try)
            self.over_layout1.addWidget(self.no_try)

            self.label_inner_initial_turn_color1.setLayout(self.over_layout1)
            # sets to True when game is over with a tie
            # the purpose is to stop the AI from executing its move
            # this is because there's no more boxes to fill
            # therefore, the game can crash when the AI executes its calculation if set to False
            self.is_game_over = True

    def play_again(self):
        # when clicking two player game page button, triggers a function that removes all widget on canvas layout
        self.canvas.window_page_changed()
        del self.work_space_layout  # deletes work space layout. A new one is created in every page

        self.another_game = AIGAMESTART()  # creates an instance of the two player game page
        self.canvas.canvas_layout.addWidget(self.another_game)  # sets all the widgets and layouts on the canvas

    def back_to_home_page(self):
        # when clicking two player game page button, triggers a function that removes all widget on canvas layout
        self.canvas.window_page_changed()
        del self.work_space_layout  # deletes work space layout. A new one is created in every page

        # creates an instance of the home page with parameter True
        # this indicates that home_page doesn't need to create a title bar duplicate for display
        self.home_page_again = HOME(True)
        self.canvas.canvas_layout.addWidget(self.home_page_again)  # sets all the widgets and layouts on the canvas

    def minimax_evaluate_board(self, board: dict):
        # horizontal check
        for i in range(3):
            if (board[f'button{i * 3 + 1}'] == board[f'button{i * 3 + 2}'] == board[
                f'button{i * 3 + 3}']) and board[f'button{i * 3 + 1}'] is not None:
                self.dummy2 = True
                # returns +10 if it's the AI's turn in the recursive tree
                return 10 if board[f'button{i * 3 + 1}'] == self.circle else -10

        # vertical check
        for i in range(3):
            if (board[f'button{i + 1}'] == board[f'button{i + 4}'] == board[
                f'button{i + 7}']) and board[f'button{i + 1}'] is not None:
                self.dummy2 = True
                # returns +10 if it's the AI's turn in the recursive tree
                return 10 if board[f'button{i + 1}'] == self.circle else -10

        # diagonal check 1
        if (board["button1"] == board["button5"] == board["button9"]) and \
                board['button1'] is not None:
            self.dummy2 = True
            # returns +10 if it's the AI's turn in the recursive tree
            return 10 if board["button1"] == self.circle else -10

        # diagonal check 2
        if (board['button3'] == board['button5'] == board['button7']) and \
                board['button3'] is not None:
            self.dummy2 = True
            # returns +10 if it's the AI's turn in the recursive tree
            return 10 if board["button3"] == self.circle else -10

        # if all boxes are filled and there's no winner, returns 0 (tie)
        if self.dummy2 == False and all(board.values()):
            return 0

        # returns nothing if there's no winner or tie yet (game continues)
        return None

    def minimax_algorithm(self, board:dict, depth: int, is_maximizer: bool):
        # calls the minimax_evaluate_board function to score each possible moves
        score = self.minimax_evaluate_board(board)

        # when calculation is done (depth == 0) or score has already been assigned, return the score
        if score is not None or depth == 0:
            return score

        if is_maximizer: # when it's the AI's turn
            max_eval = float('-inf') # sets the max_eval as -infinity
            for key, value in board.items(): # accesses the key value pair in board argument
                if value is None: # checks if the 'value' is empty, if yes, execute the next block
                    board[key] = self.cross # assign the value of that key as cross (predicts human's move)
                    # performs recursive function to predict and simulate the next step after player 1 makes a move
                    # this is done by modifying the depth of the recursive tree (depth-1)
                    # and by switching the value of is_maximizer
                    # is_maximizer is the current player's turn
                    # by adding 'not', it changes the boolean value every time the function is called,
                    # effectively changing the turn
                    # max_eval is set as -infinity to ensure the initial max function works as a recursive function
                    max_eval = max(max_eval, self.minimax_algorithm(board, depth-1, not is_maximizer))
                    board[key] = None # clears the board again
            return max_eval - depth # depth is used to help with calculating the least path to win for the AI
        else: # when it's the human's turn
            min_eval = float('inf') # sets the min_eval as +infinity
            for key, value in board.items(): # accesses the key value pair in board argument
                if value is None: # checks if the 'value' is empty, if yes, execute the next block
                    board[key] = self.circle # assign the value of that key as circle (simulates AI's move)
                    # performs recursive function to predict and simulate the next step after AI makes a move
                    # this is done by modifying the depth of the recursive tree (depth-1)
                    # and by switching the value of is_maximizer
                    # is_maximizer is the current player's turn
                    # by adding 'not', it changes the boolean value every time the function is called,
                    # effectively changing the turn
                    # min_eval is set as +infinity to ensure the initial min function works as a recursive function
                    min_eval = min(min_eval, self.minimax_algorithm(board, depth-1, not is_maximizer))
                    board[key] = None # clears the board again
            return min_eval + depth # depth is used to help with calculating the least path to win for the AI

    def get_best_move(self, board: dict):
        best_score = float('-inf') # sets best_score as -infinity
        best_move = None # sets best move as None
        for key, value in board.items(): # accesses key value pair in board dictionary
            if board[key] == None: # if the value of the key in the loop is empty, execute the next code
                # assign the value of the key
                # (in the temporary dictionary as a copy of the self.button_marks dictionary) as circle (AI)
                # purpose will be to simulate the next steps in the recursive function
                # in the event that the AI places circle in that particular box
                # the for loop makes sure the AI considers every move in the grid
                board[key] = self.circle
                # calculates score using the recursive minimax_algorithm function
                score = self.minimax_algorithm(board, depth=9, is_maximizer=True)
                board[key] = None # clears the value in the key being analyzed
                # whenever the current score is higher than previous best_score,
                # executes the next block of code
                if score > best_score:
                    best_score = score # assigns the current score as the new best_score
                    best_move = key # assigns the current key being analyzed as the new best_move
        return f'{best_move}' # returns the string of the best_move