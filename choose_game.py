from PyQt6.QtCore import Qt
from util import MainWindow
from PyQt6.QtWidgets import QVBoxLayout, QPushButton, QLabel, QHBoxLayout
from game_with_ai import AIGAMESTART
from game_2_players import TWOPGAMESTART

class CHOOSE(MainWindow):
    def __init__(self):
        super().__init__()

        self.title_bar.setVisible(False) # hides title bar to avoid duplicates

        # sets the work space to be a vertical layout
        self.work_space_layout = QVBoxLayout()
        self.work_space_layout.setContentsMargins(11, 11, 11, 11)
        self.canvas.canvas_layout.addLayout(self.work_space_layout)  # add work space horizontal layout to the centra_widget_layout (QVBoxLayout) in the parent (MainWindow) class

        self.work_space_layout.addStretch()

        self.setStyleSheet(
            "#text_default {font-size: 50pt;} "
            "#2p_game {background: transparent; color: white; text-align: center; horizontal-align: center; border: 15px transparent; font-size: 50px;}"
            "#2p_game:hover {color: green;}"
            "#ai_game {background: transparent; color: white; text-align: center; horizontal-align: center; border: 15px transparent; font-size: 50px;}"
            "#ai_game:hover {color: green;}"
        )

        # creates a label to tell players to choose a game
        self.label_choose = QLabel("Choose Game")
        self.label_choose.setObjectName('text_default')
        self.label_choose.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.work_space_layout.addWidget(self.label_choose)

        self.work_space_layout.addStretch()

        self.choosing_layout = QHBoxLayout()
        self.choosing_layout.setContentsMargins(11, 11, 11, 11)
        self.work_space_layout.addLayout(self.choosing_layout)

        # creates a button, that, when clicked, will go to the two player game page
        self.game_2p_button = QPushButton("Two Players", self)
        self.game_2p_button.setObjectName('2p_game')
        self.game_2p_button.clicked.connect(self.game_2p_button_click)

        # creates a button, that, when clicked, will go to the vs AI game page
        self.game_vsai_button = QPushButton("Vs AI", self)
        self.game_vsai_button.setObjectName('ai_game')
        self.game_vsai_button.clicked.connect(self.game_vsai_button_click)

        self.choosing_layout.addWidget(self.game_2p_button)
        self.choosing_layout.addWidget(self.game_vsai_button)

        self.work_space_layout.addStretch()

        self.work_space_layout.setSpacing(20)

    def game_2p_button_click(self):
        # when clicking two player game page button, triggers a function that removes all widget on canvas layout
        self.canvas.window_page_changed()
        del self.work_space_layout # deletes work space layout. A new one is created in every page

        self.game = TWOPGAMESTART() # creates an instance of the two player game page
        self.canvas.canvas_layout.addWidget(self.game) # sets all the widgets and layouts on the canvas

    def game_vsai_button_click(self):
        # when clicking two player game page button, triggers a function that removes all widget on canvas layout
        self.canvas.window_page_changed()
        del self.work_space_layout # deletes work space layout. A new one is created in every page

        self.game = AIGAMESTART() # creates an instance of the vs AI game page
        self.canvas.canvas_layout.addWidget(self.game) # sets all the widgets and layouts on the canvas