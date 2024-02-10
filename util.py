from PyQt6.QtCore import Qt, QSize, QEvent
from PyQt6.QtGui import QIcon, QFontDatabase
from PyQt6.QtWidgets import(
    QHBoxLayout, QLabel, QMainWindow,
    QToolButton, QVBoxLayout,
    QWidget, QSizeGrip
)

class WorkSpaceCanvas(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        # creates a canvas layout that's placed under the title bar in the container widget in MainWindow
        # Purpose is to make it easier to clear the canvas layout area for page switching
        self.canvas_layout = QVBoxLayout(self)
        self.canvas_layout.setContentsMargins(0, 0, 0, 0) # sets margin to 0 to fill the whole screen under title bar
    def window_page_changed(self):
        # Remove widgets from the layout and delete them
        while self.canvas_layout.count(): # executes when there's a widget inside
            # takes the item at index 0, if it's a widget and it's not empty,
            # delete them all after executing the while block
            item = self.canvas_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

class CustomTitleBar(QWidget):
    def __init__(self, parent):
        super().__init__(parent) # initializes the parent class's attributes

        # adds the San Fransisco Font to the code
        font_id = QFontDatabase.addApplicationFont("SanFrancisco/pro/SF-Pro-Text-Bold.otf")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]

        self.initial_pos = None # sets the initial mouse pressed title bar to be None

        title_bar_layout = QHBoxLayout(self) # creates a title bar layout in the form of a QHBoxLayout
        title_bar_layout.setContentsMargins(1, 1, 1, 1)
        title_bar_layout.setSpacing(2)

        self.title = QLabel(f"{self.__class__.__name__}", self) # takes the parent class title name
        self.title.setAlignment((Qt.AlignmentFlag.AlignCenter)) # centers the position of the title label
        # sets the styleSheet for the title label
        self.title.setStyleSheet(f"""QLabel 
        {{ text-transform:uppercase; font-size:10pt; margin-left: 48px; color:white; 
        font-family: "{font_family}", sans-serif;}}""")

        # assigns parent.windowTitle() to the variable title and checks if title is the same as parent.windowTitle()
        # if True, then the title label is set as the parent window title
        if title := parent.windowTitle():
            self.title.setText(title)

        title_bar_layout.addWidget(self.title) # puts the title label in the first element (leftmost) in the title bar layout (QHBoxLayout)

        # min button
        self.min_button = QToolButton(self)
        min_icon = QIcon()
        min_icon.addFile('min.svg')
        self.min_button.setIcon(min_icon)
        self.min_button.clicked.connect(self.window().showMinimized) # when clicked, connects the button to the window event minimized

        #max button
        self.max_button = QToolButton(self)
        max_icon =QIcon()
        max_icon.addFile('max.svg')
        self.max_button.setIcon(max_icon)
        self.max_button.clicked.connect(self.window().showMaximized)

        #close button
        self.close_button = QToolButton(self)
        close_icon = QIcon()
        close_icon.addFile('close.svg')
        self.close_button.setIcon(close_icon)
        self.close_button.clicked.connect(self.window().close)

        #normal button
        self.normal_button = QToolButton(self)
        normal_icon = QIcon()
        normal_icon.addFile('normal.svg')
        self.normal_button.setIcon(normal_icon)
        self.normal_button.clicked.connect(self.window().showNormal)
        self.normal_button.setVisible(False) # hides the normal button when window is not fullscreen

        # creates an iterable list of buttons
        buttons = [
            self.min_button,
            self.normal_button,
            self.max_button,
            self.close_button
        ]

        # iterates through the buttons list, sets the NoFocus policy to make the other widgets more prominent
        # sets the button size and the styleSheet, then add it to the title bar layout (QHBoxLayout)
        for button in buttons:
            button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
            button.setFixedSize(QSize(16, 16))
            button.setStyleSheet("""QToolButton { border: none; padding:2px;}""")
            title_bar_layout.addWidget(button)

    # this function is to change the visibility of normal and max button depending on the window state
    def window_state_changed(self, state):
        if state == Qt.WindowState.WindowMaximized:
            self.normal_button.setVisible(True)
            self.max_button.setVisible(False)
        else:
            self.normal_button.setVisible(False)
            self.max_button.setVisible(True)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__() # initializes the parent class's attributes
        # sets the window title. the TitleCustomBar class initialized in the __init__
        # of this function will take its parent's window title which is from this line
        self.setWindowTitle("Tic Tac Toe")
        # sets the window flags (properties that defines the appearance and behavior of the window)
        # to be frameless (without title bar, border, and buttons)
        # the purpose is to make a self-customized title bar
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        # sets the font for every word displayed on screen
        font_id = QFontDatabase.addApplicationFont("SanFrancisco/pro/SF-Pro-Text-Medium.otf")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]

        #creates a widget that contains everything from title bar to the work space (or canvas)
        self.central_widget = QWidget()
        self.central_widget.setObjectName("Container")
        self.central_widget.setStyleSheet(f"""
        #Container {{background: qlineargradient(x1:0 y1:0, x2:1 y2:1, stop:0 #051c2a stop:1 #44315f); border-radius: 5px;}}
        #text_default {{color:white; font-family: "{font_family}";}}"""
                                     )

        # creates an instance object of the CustomTitleBar class as a child of this class
        self.title_bar = CustomTitleBar(self)
        # creates an instance of object WorkSpaceCanvas class as a child of this class
        self.canvas = WorkSpaceCanvas(self)

        # creates a QVBoxLayout that contains the title bar and the work space layout
        # (work space layout to be added in each specific page)
        self.centra_widget_layout = QVBoxLayout()
        self.centra_widget_layout.setContentsMargins(0, 0, 0, 0)
        self.centra_widget_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.centra_widget_layout.addWidget(self.title_bar) # adds title bar to the window widget
        self.centra_widget_layout.addWidget(self.canvas)  # adds title bar to the window widget

        self.central_widget.setLayout(self.centra_widget_layout)
        self.setCentralWidget(self.central_widget)

        self.gripSize = 16
        self.grip = QSizeGrip(self)
    def setup_grip(self):
        # Assumes the existence of a vertical layout
        size_changer_layout = QVBoxLayout()

        # Adds self.grip widget to the bottom-right corner
        size_changer_layout.addWidget(self.grip, 0, Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignRight)

        # Set the layout to the central widget
        self.central_widget.setLayout(size_changer_layout)
        self.setCentralWidget(self.central_widget)

    def resizeEvent(self, event):
        QMainWindow.resizeEvent(self, event)
        rect = self.rect() #creates rectangle
        # Move the QSizeGrip to the bottom-right corner
        self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

    def showEvent(self, event):
        # Show the window in maximized mode (full-screen with title bar and toolbar)
        self.showMaximized()
        super().showEvent(event) # overrides the superclass to showMaximized() by default

    def changeEvent(self, event):
        # checks if the event type is a window state change event
        if event.type() == QEvent.Type.WindowStateChange:
            # calls the window_state_changed function from CustomTitleBar to synchronize the title bar
            self.title_bar.window_state_changed(self.windowState())
        super().changeEvent(event) # overrides the superclass to change the  default behavior
        event.accept() # marks the event as processed

    def window_state_changed(self, state):
        # shows normal button when window is maximized
        self.normal_button.setVisible(state == Qt.WindowState.WindowMaximized)
        # shows max button when window is not maximized
        self.max_button.setVisible(state != Qt.WindowState.WindowMaximized)
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton: # checks if mouse clicks on the title bar
            title_bar_rect = self.title_bar.geometry()
            if title_bar_rect.contains(event.pos()): # checks if title bar rectangle contains a position the mouse clicks
                self.initial_pos = event.position().toPoint() # enters value to the initial position
        super().mousePressEvent(event) # overrides the default behavior of the superclass
        event.accept() # marks the event as processed

    def mouseMoveEvent(self, event):
        if self.initial_pos is not None: # checks if initial_pos has a value assigned to it
            delta = event.position().toPoint() - self.initial_pos # finds the difference in position
            self.window().move(
                self.window().x() + delta.x(),
                self.window().y() + delta.y()
            ) # moves the window from the starting point to its endpoint
        super().mouseMoveEvent(event) # overrides the default behavior of the superclass
        event.accept() # marks the event as processed

    def mouseReleaseEvent(self, event):
        self.initial_pos = None # once released, sets the initial position as None again
        super().mouseReleaseEvent(event) # overrides the default behavior of the superclass
        event.accept() # marks the event as processed