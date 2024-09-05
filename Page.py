import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton, QSlider, QWidget, QHBoxLayout, QFrame
from PyQt5.QtCore import Qt, QMargins
from PyQt5.QtGui import QFont, QPixmap
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

# PHQ-9 Questions and corresponding scores
questions = [
    "Little interest or pleasure in doing things.",
    "Feeling down, depressed, or hopeless.",
    "Trouble falling or staying asleep, or sleeping too much.",
    "Feeling tired or having little energy.",
    "Poor appetite or overeating.",
    "Feeling bad about yourself — or that you are a failure or have let yourself or your family down.",
    "Trouble concentrating on things, such as reading the newspaper or watching television.",
    "Moving or speaking so slowly that other people could have noticed. Or the opposite — being so fidgety or restless that you have been moving around a lot more than usual.",
    "Thoughts that you would be better off dead, or thoughts of hurting yourself in some way."
]

# Paths to question images
image_paths = [
    "assets/question1.png",
    "assets/question2.png",
    "assets/question3.png",
    "assets/question4.png",
    "assets/question5.png",
    "assets/question6.png",
    "assets/question7.png",
    "assets/question8.png",
    "assets/question9.png"
]

responses = []

# Function to speak text
def speak_text(text):
    engine.say(text)
    engine.runAndWait()

class SnapSlider(QSlider):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setTickPosition(QSlider.TicksBelow)
        self.setTickInterval(1)
        self.setSingleStep(1)

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        value = round((event.x() / self.width()) * self.maximum())
        self.setValue(value)

    def mouseMoveEvent(self, event):
        super().mouseMoveEvent(event)
        value = round((event.x() / self.width()) * self.maximum())
        self.setValue(value)

class PHQ9App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.question_index = 0
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PHQ-9 Mental Health Assessment')
        self.setGeometry(100, 100, 500, 700)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)

        # Set consistent padding
        self.main_layout.setContentsMargins(20, 20, 20, 20)

        self.content_widget = QWidget()
        self.content_layout = QVBoxLayout(self.content_widget)
        self.content_layout.setContentsMargins(0, 0, 0, 0)  # Remove default margins
        self.main_layout.addWidget(self.content_widget)

        self.show_intro_screen()

    def show_intro_screen(self):
        self.clear_layout(self.content_layout)

        title = QLabel("PHQ-9 Mental Health Assessment")
        title.setFont(QFont('Helvetica', 20, QFont.Bold))
        title.setStyleSheet("color: #FF6347;")
        title.setAlignment(Qt.AlignCenter)
        self.content_layout.addWidget(title)

        description = QLabel("This tool helps you reflect on your mental health over the last two weeks. Answer honestly for the most accurate results.")
        description.setFont(QFont('Helvetica', 12))
        description.setWordWrap(True)
        description.setAlignment(Qt.AlignCenter)
        self.content_layout.addWidget(description)

        start_button = QPushButton("Start")
        start_button.setFont(QFont('Helvetica', 14))
        start_button.setStyleSheet("""
            QPushButton {
                background-color: #FF1493;
                color: white;
                border-radius: 20px;
                padding: 10px 40px;
            }
            QPushButton:hover {
                background-color: #e01383;
            }
            QPushButton:pressed {
                background-color: #c00f6e;
            }
        """)
        start_button.clicked.connect(self.show_question_screen)
        self.content_layout.addWidget(start_button, alignment=Qt.AlignCenter)

        self.content_layout.addStretch(1)

    def show_question_screen(self):
        if self.question_index >= len(questions):
            self.show_completion_screen()
            return

        self.clear_layout(self.content_layout)

        question_prompt = QLabel("Over the last two weeks, how often have you been bothered by:")
        question_prompt.setFont(QFont('Helvetica', 14))
        question_prompt.setAlignment(Qt.AlignCenter)
        question_prompt.setWordWrap(True)
        self.content_layout.addWidget(question_prompt)

        question_text = QLabel(questions[self.question_index])
        question_text.setFont(QFont('Helvetica', 14, QFont.Bold))
        question_text.setAlignment(Qt.AlignCenter)
        question_text.setWordWrap(True)
        self.content_layout.addWidget(question_text)

        image_label = QLabel()
        image_path = image_paths[self.question_index]
        if os.path.exists(image_path):
            pixmap = QPixmap(image_path)
            pixmap = pixmap.scaled(700, 700, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignCenter)
        self.content_layout.addWidget(image_label)

        self.response_slider = SnapSlider(Qt.Horizontal)
        self.response_slider.setRange(0, 3)
        self.response_slider.setValue(0)
        self.response_slider.setTickInterval(1)
        self.response_slider.setSingleStep(1)
        self.response_slider.setTickPosition(QSlider.TicksBelow)

        self.response_slider.setStyleSheet("""
            QSlider::groove:horizontal {
                background: #d3d3d3;
                height: 10px;
                border-radius: 5px;
            }
            QSlider::handle:horizontal {
                background: #FF6347;
                border: 1px solid #5c5c5c;
                width: 20px;
                height: 20px;
                border-radius: 10px;
                margin: -5px 0;
            }
            QSlider::sub-page:horizontal {
                background: #FF6347;
                border-radius: 5px;
            }
        """)
        self.content_layout.addWidget(self.response_slider)

        response_layout = QHBoxLayout()
        response_labels = ["Not at all", "Several days", "More than half the days", "Nearly every day"]
        for label in response_labels:
            lbl = QLabel(label)
            lbl.setFont(QFont('Helvetica', 10))
            lbl.setAlignment(Qt.AlignCenter)
            lbl.setWordWrap(True)
            response_layout.addWidget(lbl)
        self.content_layout.addLayout(response_layout)

        next_button = QPushButton("Next")
        next_button.setFont(QFont('Helvetica', 12))
        next_button.setStyleSheet("""
            QPushButton {
                background-color: #FF1493;
                color: white;
                border-radius: 20px;
                padding: 10px 40px;
            }
            QPushButton:hover {
                background-color: #e01383;
            }
            QPushButton:pressed {
                background-color: #c00f6e;
            }
        """)
        next_button.clicked.connect(self.next_question)
        self.content_layout.addWidget(next_button, alignment=Qt.AlignCenter)

        self.content_layout.addStretch(1)

        speak_text(questions[self.question_index])

    def next_question(self):
        responses.append(self.response_slider.value())
        self.question_index += 1
        self.show_question_screen()

    def show_completion_screen(self):
        self.clear_layout(self.content_layout)

        completion_title = QLabel("Assessment Complete")
        completion_title.setFont(QFont('Helvetica', 16))
        completion_title.setAlignment(Qt.AlignCenter)
        self.content_layout.addWidget(completion_title)

        completion_text = QLabel("Thank you for completing the PHQ-9 assessment. Your responses can help you understand your mental health better.")
        completion_text.setFont(QFont('Helvetica', 12))
        completion_text.setWordWrap(True)
        completion_text.setAlignment(Qt.AlignCenter)
        self.content_layout.addWidget(completion_text)

        results_button = QPushButton("View Results")
        results_button.setFont(QFont('Helvetica', 14))
        results_button.setStyleSheet("""
            QPushButton {
                background-color: #FF1493;
                color: white;
                border-radius: 20px;
                padding: 10px 40px;
            }
            QPushButton:hover {
                background-color: #e01383;
            }
            QPushButton:pressed {
                background-color: #c00f6e;
            }
        """)
        results_button.clicked.connect(self.show_results_screen)
        self.content_layout.addWidget(results_button, alignment=Qt.AlignCenter)

        self.content_layout.addStretch(1)

    def show_results_screen(self):
        self.clear_layout(self.content_layout)

        total_score = sum(responses)
        score_label = QLabel(f"Your PHQ-9 Score: {total_score}")
        score_label.setFont(QFont('Helvetica', 16))
        score_label.setAlignment(Qt.AlignCenter)
        self.content_layout.addWidget(score_label)

        if total_score <= 4:
            interpretation = "Minimal depression"
        elif 5 <= total_score <= 9:
            interpretation = "Mild depression"
        elif 10 <= total_score <= 14:
            interpretation = "Moderate depression"
        elif 15 <= total_score <= 19:
            interpretation = "Moderately severe depression"
        else:
            interpretation = "Severe depression"

        interpretation_label = QLabel(f"Interpretation: {interpretation}")
        interpretation_label.setFont(QFont('Helvetica', 14))
        interpretation_label.setAlignment(Qt.AlignCenter)
        self.content_layout.addWidget(interpretation_label)

        resources_text = QLabel("If you need support, consider reaching out to a healthcare provider or the following resources:")
        resources_text.setFont(QFont('Helvetica', 12))
        resources_text.setWordWrap(True)
        resources_text.setAlignment(Qt.AlignCenter)
        self.content_layout.addWidget(resources_text)

        hotline_label1 = QLabel("Mental Health Hospital")
        hotline_label1.setFont(QFont('Helvetica', 12, QFont.Bold))
        hotline_label1.setAlignment(Qt.AlignCenter)
        self.content_layout.addWidget(hotline_label1)

        hotline_label2 = QLabel("National Therapeutic Center")
        hotline_label2.setFont(QFont('Helvetica', 12, QFont.Bold))
        hotline_label2.setAlignment(Qt.AlignCenter)
        self.content_layout.addWidget(hotline_label2)

        self.content_layout.addStretch(1)

    def clear_layout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PHQ9App()
    ex.show()
    sys.exit(app.exec_())