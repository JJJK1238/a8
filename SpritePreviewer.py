# GitHub Repo: https://github.com/JJJK1238/a8
import math

from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

# This function loads a series of sprite images stored in a folder with a
# consistent naming pattern: sprite_# or sprite_##. It returns a list of the images.
def load_sprite(sprite_folder_name, number_of_frames):
    frames = []
    padding = math.ceil(math.log(number_of_frames - 1, 10))
    for frame in range(number_of_frames):
        folder_and_file_name = sprite_folder_name + "/sprite_" + str(frame).rjust(padding, '0') + ".png"
        frames.append(QPixmap(folder_and_file_name))

    return frames

class SpritePreview(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sprite Animation Preview")
        # This loads the provided sprite and would need to be changed for your own.
        self.num_frames = 21
        self.frames = load_sprite('spriteImages',self.num_frames)

        # Add any other instance variables needed to track information as the program
        # runs here
        self.current_frame = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)

        # Make the GUI in the setupUI method
        self.setupUI()


    def setupUI(self):
        # An application needs a central widget - often a QFrame
        frame = QFrame()

        # Add a lot of code here to make layouts, more QFrame or QWidgets, and
        # the other components of the program.
        # Create needed connections between the UI components and slot methods
        # you define in this class.
        main_layout = QVBoxLayout()

        self.sprite_label = QLabel()
        self.sprite_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sprite_label.setPixmap(self.frames[0])

        top_layout.addWidget(self.sprite_label)

        self.slider = QSlider(Qt.Orientation.Vertical)
        self.slider.setRange(1, 100)
        self.slider.setValue(1)
        self.slider.setTickPosition(QSlider.TickPosition.TicksBothSides)
        self.slider.setTickInterval(10)
        self.slider.valueChanged.connect(self.update_fps)

        top_layout.addWidget(self.slider)

        main_layout.addLayout(top_layout)

# FPS
        fps_layout = QHBoxLayout()

        self.fps_text = QLabel("Frames per second")
        self.fps_value = QLabel("1")

        self.fps_text.setFont(QFont("Arial", 18))
        self.fps_value.setFont(QFont("Arial", 18))

        fps_layout.addStretch()
        fps_layout.addWidget(self.fps_text)
        fps_layout.addSpacing(10)
        fps_layout.addWidget(self.fps_value)
        fps_layout.addStretch()

        main_layout.addLayout(fps_layout)
# Start Button
        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.start_stop)
        self.start_button.setMinimumHeight(50)
        self.start_button.setFont(QFont("Arial", 18))

        main_layout.addWidget(self.start_button)

        frame.setLayout(main_layout)
        self.setCentralWidget(frame)

        self.create_menu()

    def create_menu(self):

        menu = self.menuBar()

        file_menu = menu.addMenu("File")

        pause_action = QAction("Pause", self)
        pause_action.triggered.connect(self.pause_animation)

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)

        file_menu.addAction(pause_action)
        file_menu.addAction(exit_action)

    def update_fps(self):
        fps = self.slider.value()
        self.fps_value.setText(str(fps))
        delay = int(1000 / fps)
        self.timer.setInterval(delay)

    def start_stop(self):

        if self.start_button.text() == "Start":

            fps = self.slider.value()
            delay = int(1000 / fps)

            self.timer.start(delay)

            self.start_button.setText("Stop")

        else:

            self.timer.stop()
            self.start_button.setText("Start")

    def pause_animation(self):

        self.timer.stop()
        self.start_button.setText("Start")

    def update_frame(self):

        self.current_frame += 1

        if self.current_frame >= self.num_frames:
            self.current_frame = 0

        self.sprite_label.setPixmap(self.frames[self.current_frame])

    # You will need methods in the class to act as slots to connect to signals


def main():
    app = QApplication([])
    # Create our custom application
    window = SpritePreview()
    # And show it
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
