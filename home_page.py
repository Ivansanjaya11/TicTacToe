from PyQt6.QtCore import Qt
from util import MainWindow
from PyQt6.QtWidgets import QVBoxLayout, QPushButton, QLabel

class HOME(MainWindow):
    def __init__(self, false: bool):
        super().__init__()

        # sets a false variable to check if it's after quitting a game back to home page.
        # If True, then title bar is set to hide
        if false != False:
            self.title_bar.setVisible(False)

        # sets the work space to be a vertical layout
        self.work_space_layout = QVBoxLayout()
        self.work_space_layout.setContentsMargins(11, 11, 11, 11)
        self.canvas.canvas_layout.addLayout(self.work_space_layout)  # add work space horizontal layout to the centra_widget_layout (QVBoxLayout) in the parent (MainWindow) class

        self.work_space_layout.addStretch()

        self.setStyleSheet(
            "#text_default {font-size: 50pt;} "
            "#start_button {background: transparent; color: white; text-align: center; horizontal-align: center; border: 15px transparent; font-size: 50px;}"
            "#start_button:hover {color: green;}"
        )

        # creates labels to display the game title
        self.label_welcome = QLabel("WELCOME TO")
        self.label_welcome.setObjectName('text_default')
        self.label_game = QLabel("TIC TAC TOE THE GAME")
        self.label_game.setObjectName('text_default')
        self.work_space_layout.addWidget(self.label_welcome)
        self.work_space_layout.addWidget(self.label_game)

        # sets a start button. When clicked, it'll go to a game choose page
        self.start_button = QPushButton("START", self)
        self.start_button.setObjectName('start_button')
        self.start_button.clicked.connect(self.start_button_click) # handles the event of clicking the button
        self.work_space_layout.addWidget(self.start_button)

        self.work_space_layout.addStretch()

        # sets the labels and button into the work space layout, and add spacing between them
        self.work_space_layout.setAlignment(self.label_welcome, Qt.AlignmentFlag.AlignCenter)
        self.work_space_layout.setAlignment(self.label_game, Qt.AlignmentFlag.AlignCenter)
        self.work_space_layout.setAlignment(self.start_button, Qt.AlignmentFlag.AlignCenter)
        self.work_space_layout.setSpacing(20)

    def start_button_click(self):
        # calls the window page changed function to erase all widgets inside canvas layout
        self.canvas.window_page_changed()
        del self.work_space_layout # delete the work space layout

        from choose_game import CHOOSE # imports the choose page

        self.choose_page_game = CHOOSE() # creates an instance of the choose game page
        # sets the choose page on the now blank canvas layout
        self.canvas.canvas_layout.addWidget(self.choose_page_game)