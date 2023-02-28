from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout
import random

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Invisible Characters Demo")
        self.setGeometry(100, 100, 400, 200)

        self.label = QLabel("Enter a word:")
        self.input_field = QLineEdit()
        self.output_field = QLabel()

        self.convert_button = QPushButton("Convert")
        self.convert_button.clicked.connect(self.update_output)

        self.copy_button = QPushButton("Copy")
        self.copy_button.clicked.connect(self.copy_output)

        self.input_layout = QHBoxLayout()
        self.input_layout.addWidget(self.label)
        self.input_layout.addWidget(self.input_field)

        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.convert_button)
        self.button_layout.addWidget(self.copy_button)

        self.output_layout = QVBoxLayout()
        self.output_layout.addWidget(self.output_field)
        self.output_layout.addLayout(self.button_layout)

        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.input_layout)
        self.main_layout.addLayout(self.output_layout)

        self.setLayout(self.main_layout)

    def update_output(self):
        word = self.input_field.text()
        invisible_chars = ["\u2064", "\u2063", "\u2062"]
        word_with_invisibles = ""
        for letter in word:
            invisible_chars_subset = random.sample(invisible_chars, k=3)
            invisible_chars_str = "".join(invisible_chars_subset)
            word_with_invisibles += letter + invisible_chars_str
        self.output_field.setText(word_with_invisibles)

    def copy_output(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.output_field.text())

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
