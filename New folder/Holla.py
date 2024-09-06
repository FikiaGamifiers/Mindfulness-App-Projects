import sys
import random
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QSlider,
    QHBoxLayout
)
from PyQt5.QtGui import QPixmap, QFont, QImage, QColor
from PyQt5.QtCore import Qt, QRect

class RoundedButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setStyleSheet("""
            QPushButton {
                background-color: #FF5C8D;
                border-radius: 25px;
                color: white;
                font-size: 16px;
                height: 50px;
                width: 120px;
            }
            QPushButton:pressed {
                background-color: #e5537e;
            }
        """)
        self.setMinimumHeight(50)
        self.setMinimumWidth(120)

class ConflictApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Conflict Style Assessment")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: white;")

        # Main layout
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Define the full set of questions and images
        self.questions = {
            "Assertive": [
                {
                    "question": "How often can you handle criticism without feeling overly defensive or hurt?",
                    "statement": "I [answer] handle criticism without feeling overly defensive or hurt.",
                    "image": "assertive_1.png"
                },
                {
                    "question": "How often do you feel comfortable making requests of others?",
                    "statement": "I [answer] feel comfortable making requests of others.",
                    "image": "assertive_2.png"
                },
                {
                    "question": "How often do you speak up in group situations, even when you have a different opinion?",
                    "statement": "I [answer] speak up in group situations, even when I have a different opinion.",
                    "image": "assertive_3.png"
                },
                {
                    "question": "How often do you feel at ease when you need to negotiate or compromise in a situation?",
                    "statement": "I [answer] feel at ease when I need to negotiate or compromise in a situation.",
                    "image": "assertive_4.png"
                }
            ],
            "Aggressive": [
                {
                    "question": "How often do you raise your voice or speak forcefully to make a point?",
                    "statement": "I [answer] tend to raise my voice or speak forcefully when I want to make a point.",
                    "image": "aggressive_1.png"
                },
                {
                    "question": "How often do you interrupt others when you believe they are wrong?",
                    "statement": "I [answer] find myself interrupting others when I believe they are wrong.",
                    "image": "aggressive_2.png"
                },
                {
                    "question": "How often do you use sarcasm or a harsh tone when frustrated?",
                    "statement": "I [answer] use sarcasm or a harsh tone when I’m frustrated with someone.",
                    "image": "aggressive_3.png"
                },
                {
                    "question": "How often do you insist on getting your way, regardless of others' opinions?",
                    "statement": "I [answer] insist on getting my way, even if it means disregarding others’ opinions.",
                    "image": "aggressive_4.png"
                },
                {
                    "question": "How often do you criticize others openly when they don't meet your standards?",
                    "statement": "I [answer] feel justified in criticizing others openly when they don’t meet my standards.",
                    "image": "aggressive_5.png"
                }
            ],
            "Passive": [
                {
                    "question": "How often do you keep your opinions to yourself to avoid conflict?",
                    "statement": "I [answer] keep my opinions to myself to avoid conflict.",
                    "image": "passive_1.png"
                },
                {
                    "question": "How often do you struggle to say 'no,' even when you don't want to do something?",
                    "statement": "I [answer] struggle to say 'no,' even when I don’t want to do something.",
                    "image": "passive_2.png"
                },
                {
                    "question": "How often do you avoid expressing your true feelings for fear of negative reactions?",
                    "statement": "I [answer] avoid expressing my true feelings because I fear others might react negatively.",
                    "image": "passive_3.png"
                },
                {
                    "question": "How often do you agree with others just to keep the peace, even if you disagree?",
                    "statement": "I [answer] agree with others, even when I secretly disagree, just to keep the peace.",
                    "image": "passive_4.png"
                },
                {
                    "question": "How often do you let others take advantage of you to avoid tension?",
                    "statement": "I [answer] let others take advantage of me because I don’t want to create tension.",
                    "image": "passive_5.png"
                }
            ],
            "Passive Aggressive": [
                {
                    "question": "How often do you agree to do things but don't follow through to show displeasure?",
                    "statement": "I [answer] agree to do things but then don't follow through as a way of showing my displeasure.",
                    "image": "passive_aggressive_1.png"
                },
                {
                    "question": "How often do you make sarcastic remarks instead of directly expressing dissatisfaction?",
                    "statement": "I [answer] make sarcastic remarks instead of directly expressing my dissatisfaction.",
                    "image": "passive_aggressive_2.png"
                },
                {
                    "question": "How often do you give the silent treatment when upset instead of discussing the issue?",
                    "statement": "I [answer] give the silent treatment when I’m upset instead of talking about what’s bothering me.",
                    "image": "passive_aggressive_3.png"
                },
                {
                    "question": "How often do you subtly undermine others when unhappy instead of confronting the issue?",
                    "statement": "I [answer] subtly undermine others when I’m unhappy with them, rather than confronting the issue.",
                    "image": "passive_aggressive_4.png"
                },
                {
                    "question": "How often do you agree to others' requests but secretly resent them?",
                    "statement": "I [answer] agree to others’ requests, but I secretly resent them.",
                    "image": "passive_aggressive_5.png"
                }
            ]
        }
        
        # Randomize and flatten the list of questions
        self.selected_questions = []
        for style, questions in self.questions.items():
            random.shuffle(questions)  # Randomize questions within each style
            self.selected_questions.extend([{"style": style, **q} for q in questions])

        random.shuffle(self.selected_questions)  # Further randomize the order of all questions

        self.current_question_index = 0
        self.responses = {style: 0 for style in self.questions}

        # Header - Conflict Style Title
        self.header_label = QLabel(self)
        self.header_label.setFont(QFont("Arial", 24, QFont.Bold))
        self.header_label.setStyleSheet("color: #FF5C8D;")
        self.header_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.header_label)

        # Top Section - Question Text
        self.question_label = QLabel(self)
        self.question_label.setFont(QFont("Arial", 16))
        self.question_label.setAlignment(Qt.AlignCenter)
        self.question_label.setWordWrap(True)
        self.layout.addWidget(self.question_label)

        # Middle Section - Statement Display
        self.statement_label = QLabel(self)
        self.statement_label.setFont(QFont("Arial", 14, QFont.Bold))
        self.statement_label.setAlignment(Qt.AlignCenter)
        self.statement_label.setWordWrap(True)
        self.layout.addWidget(self.statement_label)

        # Image Display (Centered)
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.image_label)

        # Middle Section - Response Slider
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setRange(0, 4)
        self.slider.setSingleStep(1)
        self.slider.valueChanged.connect(self.update_statement)
        self.slider.setStyleSheet("""
            QSlider::groove:horizontal {
                height: 10px;
                background: lightgray;
                border-radius: 5px;
            }
            QSlider::handle:horizontal {
                background: orange;
                border: 1px solid #5c5c5c;
                width: 18px;
                margin: -5px 0;
                border-radius: 9px;
            }
        """)
        self.layout.addWidget(self.slider)

        # Slider Labels
        self.slider_labels_layout = QHBoxLayout()
        self.layout.addLayout(self.slider_labels_layout)
        self.slider_labels = []
        for label_text in ["Never", "Rarely", "Sometimes", "Often", "Always"]:
            lbl = QLabel(label_text)
            lbl.setFont(QFont("Arial", 10))
            lbl.setAlignment(Qt.AlignCenter)
            self.slider_labels_layout.addWidget(lbl)
            self.slider_labels.append(lbl)

        # Action Button (Rounded)
        self.next_button = RoundedButton("NEXT", self)
        self.next_button.clicked.connect(self.next_question)
        self.layout.addWidget(self.next_button)

        # Load the first question
        self.load_question()

    def load_question(self):
        question_data = self.selected_questions[self.current_question_index]
        self.header_label.setText(question_data["style"])
        self.question_label.setText(question_data["question"])
        self.original_statement = question_data["statement"]
        self.update_statement(self.slider.value())  # Initialize the statement with the current slider value
        self.load_image(question_data["image"])

    def load_image(self, image_path):
        if not image_path:
            self.image_label.setText("Image not available")
            return

        image = QImage(image_path)
        if image.isNull():
            self.image_label.setText("Failed to load image")
            return

        cropped_image = image.copy(self.find_image_bounding_box(image))
        pixmap = QPixmap.fromImage(cropped_image).scaled(
            900, 950, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.image_label.setPixmap(pixmap)

    def find_image_bounding_box(self, image):
        min_x, min_y, max_x, max_y = image.width(), image.height(), 0, 0

        for y in range(image.height()):
            for x in range(image.width()):
                color = QColor(image.pixel(x, y))
                if color.alpha() > 0:
                    min_x = min(min_x, x)
                    min_y = min(min_y, y)
                    max_x = max(max_x, x)
                    max_y = max(max_y, y)

        return QRect(min_x, min_y, max_x - min_x + 1, max_y - min_y + 1)

    def resizeEvent(self, event):
        # Override resizeEvent to do nothing, effectively removing resizing effect
        pass

    def update_statement(self, value):
        answers = ["Never", "Rarely", "Sometimes", "Often", "Always"]
        index = int(value)
        updated_statement = self.original_statement.replace("[answer]", answers[index].lower())
        self.statement_label.setText(updated_statement)

    def next_question(self):
        # Record the current answer
        response = int(self.slider.value())
        style = self.selected_questions[self.current_question_index]["style"]
        self.responses[style] += response

        # Move to the next question
        self.current_question_index += 1
        if self.current_question_index < len(self.selected_questions):
            self.load_question()
        else:
            self.show_results()

    def show_results(self):
        # Hide the NEXT button and slider labels when showing results
        self.next_button.hide()
        for lbl in self.slider_labels:
            lbl.hide()

        # Determine the dominant conflict style
        dominant_style = max(self.responses, key=self.responses.get)

        # Clear the existing layout
        for i in reversed(range(self.layout.count())):
            widget = self.layout.itemAt(i).widget()
            if widget is not None and widget is not self.next_button:
                widget.deleteLater()

        # Display the results
        result_header_label = QLabel(dominant_style, self)
        result_header_label.setFont(QFont("Arial", 24, QFont.Bold))
        result_header_label.setStyleSheet("color: #FF5C8D;")
        result_header_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(result_header_label)

        result_label = QLabel("Your Conflict Style:", self)
        result_label.setFont(QFont("Arial", 16))
        result_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(result_label)

        dominant_label = QLabel(dominant_style, self)
        dominant_label.setFont(QFont("Arial", 18, QFont.Bold))
        dominant_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(dominant_label)

        # Display responses in a text-based format
        results_text = "\n".join(f"{style}: {score}" for style, score in self.responses.items())
        results_label = QLabel(results_text, self)
        results_label.setFont(QFont("Arial", 14))
        results_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(results_label)

        # Finish Button (Rounded)
        finish_button = RoundedButton("FINISH", self)
        finish_button.clicked.connect(self.close)
        self.layout.addWidget(finish_button)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ConflictApp()
    window.show()
    sys.exit(app.exec_())
