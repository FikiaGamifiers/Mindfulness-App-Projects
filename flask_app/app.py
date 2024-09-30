from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QTextEdit, QMessageBox, QStackedWidget, QGridLayout)
from PySide6.QtGui import QIcon, QPixmap, QFont
from PySide6.QtCore import QSize, Qt
import sys

class ReflectionApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("What's Stopping Me?")
        self.setGeometry(400, 300, 700, 900)  # Adjust the window size

        # Set background to white and text to black
        self.setStyleSheet("""
            QWidget { background-color: white; }
            QLabel, QPushButton, QTextEdit { color: black; }
        """)

        # Store user input
        self.user_response = ""
        self.selected_supports = []  # List to store selected supports

        # Main Layout
        self.layout = QVBoxLayout()

        # Stacked Widget for switching between screens
        self.stack = QStackedWidget(self)
        self.layout.addWidget(self.stack)

        # Create screens
        self.create_welcome_screen()
        self.create_reflection_screen()
        self.create_first_question_screen()
        self.create_first_support_screen()
        self.create_second_question_screen()  # This was missing
        self.create_second_support_screen()
        self.create_third_question_screen()  # This was missing
        self.create_third_support_screen()
        self.create_fourth_question_screen()  # This was missing
        self.create_fourth_support_screen()
        self.create_reflective_screen()  # Add reflective screen

        self.setLayout(self.layout)

    def create_welcome_screen(self):
        """Welcome screen with 'START' button."""
        welcome_screen = QWidget()
        welcome_layout = QVBoxLayout()

        # Welcome message
        welcome_label = QLabel("Ready to take control of your life? Let’s start by reflecting on what might be holding you back.")
        welcome_label.setAlignment(Qt.AlignCenter)
        welcome_label.setWordWrap(True)
        welcome_label.setFont(QFont('Arial', 12))
        welcome_layout.addWidget(welcome_label)

        # Start button
        start_button = QPushButton("START")
        start_button.setStyleSheet("background-color: #FF69B4; color: white; border-radius: 15px; padding: 10px;")
        start_button.clicked.connect(self.go_to_reflection_screen)
        start_button.setFixedSize(100, 50)
        welcome_layout.addWidget(start_button, alignment=Qt.AlignCenter)

        welcome_screen.setLayout(welcome_layout)
        self.stack.addWidget(welcome_screen)

    def create_reflection_screen(self):
        """Reflection input screen (after pressing START)."""
        reflection_screen = QWidget()
        reflection_layout = QVBoxLayout()

        # Reflection question
        question_label = QLabel("What’s Stopping Me?")
        question_label.setAlignment(Qt.AlignCenter)
        question_label.setFont(QFont('Arial', 18))
        reflection_layout.addWidget(question_label)

        # Explanation
        explanation_label = QLabel("What are some things in your life that you’re thinking about changing or improving?")
        explanation_label.setAlignment(Qt.AlignCenter)
        explanation_label.setWordWrap(True)
        explanation_label.setFont(QFont('Arial', 12))
        reflection_layout.addWidget(explanation_label)

        # Text box for user input
        self.text_box = QTextEdit()  # Text edit for user input
        self.text_box.setFixedHeight(100)
        reflection_layout.addWidget(self.text_box)

        # NEXT button to proceed
        next_button = QPushButton("NEXT")
        next_button.setStyleSheet("background-color: #FF69B4; color: white; border-radius: 15px; padding: 10px;")
        next_button.setFixedSize(100, 50)
        next_button.clicked.connect(self.save_and_go_to_first_question)
        reflection_layout.addWidget(next_button, alignment=Qt.AlignCenter)

        reflection_screen.setLayout(reflection_layout)
        self.stack.addWidget(reflection_screen)

    def go_to_reflection_screen(self):
        """Navigate to the reflection input screen."""
        self.stack.setCurrentIndex(1)

    def save_and_go_to_first_question(self):
        """Save user input and go to the first Yes/No question."""
        self.user_response = self.text_box.toPlainText().strip()

        # Check if input is empty
        if not self.user_response:
            QMessageBox.warning(self, "Input Error", "Please enter a response before proceeding.")
        else:
            # Proceed to the first Yes/No question screen
            self.stack.setCurrentIndex(2)

    def create_first_question_screen(self):
        """First Yes/No question screen: 'Do you feel physically able to do this?'."""
        first_question_screen = QWidget()
        first_question_layout = QVBoxLayout()

        question_label = QLabel("Do you feel physically able to do this activity?")
        question_label.setAlignment(Qt.AlignCenter)
        question_label.setFont(QFont('Arial', 16))
        first_question_layout.addWidget(question_label)

        # Image between question and buttons
        image_label = QLabel()
        pixmap = QPixmap('your_image.png')  # Replace with actual image path
        pixmap = pixmap.scaled(200, 200, Qt.KeepAspectRatio)
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignCenter)
        first_question_layout.addWidget(image_label)

        # Yes/No buttons
        yes_button = QPushButton("YES")
        yes_button.setFixedSize(100, 50)
        yes_button.setStyleSheet("background-color: #4CAF50; color: white; border-radius: 15px;")
        yes_button.clicked.connect(self.go_to_second_question)
        first_question_layout.addWidget(yes_button, alignment=Qt.AlignCenter)

        no_button = QPushButton("NO")
        no_button.setFixedSize(100, 50)
        no_button.setStyleSheet("background-color: #FF6347; color: white; border-radius: 15px;")
        no_button.clicked.connect(self.go_to_first_support_screen)
        first_question_layout.addWidget(no_button, alignment=Qt.AlignCenter)

        first_question_screen.setLayout(first_question_layout)
        self.stack.addWidget(first_question_screen)

    def create_first_support_screen(self):
        """Support options screen for Action 1."""
        support_screen = QWidget()
        support_layout = QVBoxLayout()

        # Support header
        header_label = QLabel("Tell us if you think any of the support we can provide would be useful to you:")
        header_label.setAlignment(Qt.AlignCenter)
        header_label.setFont(QFont('Arial', 14))
        support_layout.addWidget(header_label)

        # Grid layout for support options
        support_grid = QGridLayout()

        options = [
            ("Physical Exercises or Movement Suggestions", "your_image.png"),
            ("Adapting the Task", "your_image.png"),
            ("Breaking It Down into Steps", "your_image.png")
        ]

        for i, (title, img) in enumerate(options):
            option_layout = QVBoxLayout()
            option_button = QPushButton()
            option_button.setIcon(QIcon(img))
            option_button.setIconSize(QSize(120, 120))
            option_button.clicked.connect(lambda _, t=title: self.show_support_popup(t))  # Capture title correctly
            option_layout.addWidget(option_button)
            option_label = QLabel(title)
            option_label.setAlignment(Qt.AlignCenter)
            option_layout.addWidget(option_label)
            support_grid.addLayout(option_layout, i // 2, i % 2)

        support_layout.addLayout(support_grid)

        # NEXT button
        next_button = QPushButton("NEXT")
        next_button.setStyleSheet("background-color: #FF69B4; color: white; border-radius: 15px;")
        next_button.setFixedSize(100, 50)
        next_button.clicked.connect(self.go_to_second_question)
        support_layout.addWidget(next_button, alignment=Qt.AlignCenter)

        support_screen.setLayout(support_layout)
        self.stack.addWidget(support_screen)

    def go_to_first_support_screen(self):
        """Navigate to the first support screen."""
        self.stack.setCurrentIndex(3)

    def go_to_second_question(self):
        """Navigate to the second Yes/No question screen."""
        self.stack.setCurrentIndex(4)

    def create_second_question_screen(self):
        """Second Yes/No question screen: 'Do you feel like you know how to do this?'."""
        second_question_screen = QWidget()
        second_question_layout = QVBoxLayout()

        question_label = QLabel("Do you feel like you know how to do this or have the skills you need?")
        question_label.setAlignment(Qt.AlignCenter)
        question_label.setFont(QFont('Arial', 16))
        second_question_layout.addWidget(question_label)

        # Image between question and buttons
        image_label = QLabel()
        pixmap = QPixmap('your_image.png')  # Replace with actual image path
        pixmap = pixmap.scaled(200, 200, Qt.KeepAspectRatio)
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignCenter)
        second_question_layout.addWidget(image_label)

        # Yes/No buttons
        yes_button = QPushButton("YES")
        yes_button.setFixedSize(100, 50)
        yes_button.setStyleSheet("background-color: #4CAF50; color: white; border-radius: 15px;")
        yes_button.clicked.connect(self.go_to_third_question)
        second_question_layout.addWidget(yes_button, alignment=Qt.AlignCenter)

        no_button = QPushButton("NO")
        no_button.setFixedSize(100, 50)
        no_button.setStyleSheet("background-color: #FF6347; color: white; border-radius: 15px;")
        no_button.clicked.connect(self.go_to_second_support_screen)
        second_question_layout.addWidget(no_button, alignment=Qt.AlignCenter)

        second_question_screen.setLayout(second_question_layout)
        self.stack.addWidget(second_question_screen)

    def create_second_support_screen(self):
        """Support options screen for Action 2."""
        support_screen = QWidget()
        support_layout = QVBoxLayout()

        # Support header
        header_label = QLabel("Tell us if you think any of the support we can provide would be useful to you:")
        header_label.setAlignment(Qt.AlignCenter)
        header_label.setFont(QFont('Arial', 14))
        support_layout.addWidget(header_label)

        # Grid layout for support options
        support_grid = QGridLayout()

        options = [
            ("Clear, Simple Instructions", "your_image.png"),
            ("Learning Resources", "your_image.png"),
            ("Practical Tips", "your_image.png"),
            ("Practicing Together", "your_image.png")
        ]

        for i, (title, img) in enumerate(options):
            option_layout = QVBoxLayout()
            option_button = QPushButton()
            option_button.setIcon(QIcon(img))
            option_button.setIconSize(QSize(120, 120))
            option_button.clicked.connect(lambda _, t=title: self.show_support_popup(t))  # Capture title correctly
            option_layout.addWidget(option_button)
            option_label = QLabel(title)
            option_label.setAlignment(Qt.AlignCenter)
            option_layout.addWidget(option_label)
            support_grid.addLayout(option_layout, i // 2, i % 2)

        support_layout.addLayout(support_grid)

        # NEXT button
        next_button = QPushButton("NEXT")
        next_button.setStyleSheet("background-color: #FF69B4; color: white; border-radius: 15px;")
        next_button.setFixedSize(100, 50)
        next_button.clicked.connect(self.go_to_third_question)
        support_layout.addWidget(next_button, alignment=Qt.AlignCenter)

        support_screen.setLayout(support_layout)
        self.stack.addWidget(support_screen)

    def go_to_second_support_screen(self):
        """Navigate to the second support screen."""
        self.stack.setCurrentIndex(5)

    def go_to_third_question(self):
        """Navigate to the third Yes/No question screen."""
        self.stack.setCurrentIndex(6)

    def create_third_question_screen(self):
        """Third Yes/No question screen: 'Do you have the right tools or environment?'."""
        third_question_screen = QWidget()
        third_question_layout = QVBoxLayout()

        question_label = QLabel("Do you have everything you need to make this change, like the right tools or environment?")
        question_label.setAlignment(Qt.AlignCenter)
        question_label.setFont(QFont('Arial', 16))
        third_question_layout.addWidget(question_label)

        # Image between question and buttons
        image_label = QLabel()
        pixmap = QPixmap('your_image.png')  # Replace with actual image path
        pixmap = pixmap.scaled(200, 200, Qt.KeepAspectRatio)
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignCenter)
        third_question_layout.addWidget(image_label)

        # Yes/No buttons
        yes_button = QPushButton("YES")
        yes_button.setFixedSize(100, 50)
        yes_button.setStyleSheet("background-color: #4CAF50; color: white; border-radius: 15px;")
        yes_button.clicked.connect(self.go_to_fourth_question)
        third_question_layout.addWidget(yes_button, alignment=Qt.AlignCenter)

        no_button = QPushButton("NO")
        no_button.setFixedSize(100, 50)
        no_button.setStyleSheet("background-color: #FF6347; color: white; border-radius: 15px;")
        no_button.clicked.connect(self.go_to_third_support_screen)
        third_question_layout.addWidget(no_button, alignment=Qt.AlignCenter)

        third_question_screen.setLayout(third_question_layout)
        self.stack.addWidget(third_question_screen)

    def create_third_support_screen(self):
        """Support options screen for Action 3."""
        support_screen = QWidget()
        support_layout = QVBoxLayout()

        # Support header
        header_label = QLabel("Tell us if you think any of the support we can provide would be useful to you:")
        header_label.setAlignment(Qt.AlignCenter)
        header_label.setFont(QFont('Arial', 14))
        support_layout.addWidget(header_label)

        # Grid layout for support options
        support_grid = QGridLayout()

        options = [
            ("Help Finding Resources", "your_image.png"),
            ("Making Your Environment Easier", "your_image.png")
        ]

        for i, (title, img) in enumerate(options):
            option_layout = QVBoxLayout()
            option_button = QPushButton()
            option_button.setIcon(QIcon(img))
            option_button.setIconSize(QSize(120, 120))
            option_button.clicked.connect(lambda _, t=title: self.show_support_popup(t))  # Capture title correctly
            option_layout.addWidget(option_button)
            option_label = QLabel(title)
            option_label.setAlignment(Qt.AlignCenter)
            option_layout.addWidget(option_label)
            support_grid.addLayout(option_layout, i // 2, i % 2)

        support_layout.addLayout(support_grid)

        # NEXT button
        next_button = QPushButton("NEXT")
        next_button.setStyleSheet("background-color: #FF69B4; color: white; border-radius: 15px;")
        next_button.setFixedSize(100, 50)
        next_button.clicked.connect(self.go_to_fourth_question)
        support_layout.addWidget(next_button, alignment=Qt.AlignCenter)

        support_screen.setLayout(support_layout)
        self.stack.addWidget(support_screen)

    def go_to_third_support_screen(self):
        """Navigate to the third support screen."""
        self.stack.setCurrentIndex(7)

    def go_to_fourth_question(self):
        """Navigate to the fourth Yes/No question screen."""
        self.stack.setCurrentIndex(8)

    def create_fourth_question_screen(self):
        """Fourth Yes/No question screen: 'Do you have support from others?'."""
        fourth_question_screen = QWidget()
        fourth_question_layout = QVBoxLayout()

        question_label = QLabel("Do you have support from friends, family, or others to help you do this?")
        question_label.setAlignment(Qt.AlignCenter)
        question_label.setFont(QFont('Arial', 16))
        fourth_question_layout.addWidget(question_label)

        # Image between question and buttons
        image_label = QLabel()
        pixmap = QPixmap('your_image.png')  # Replace with actual image path
        pixmap = pixmap.scaled(200, 200, Qt.KeepAspectRatio)
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignCenter)
        fourth_question_layout.addWidget(image_label)

        # Yes/No buttons
        yes_button = QPushButton("YES")
        yes_button.setFixedSize(100, 50)
        yes_button.setStyleSheet("background-color: #4CAF50; color: white; border-radius: 15px;")
        yes_button.clicked.connect(self.go_to_reflective_screen)
        fourth_question_layout.addWidget(yes_button, alignment=Qt.AlignCenter)

        no_button = QPushButton("NO")
        no_button.setFixedSize(100, 50)
        no_button.setStyleSheet("background-color: #FF6347; color: white; border-radius: 15px;")
        no_button.clicked.connect(self.go_to_fourth_support_screen)
        fourth_question_layout.addWidget(no_button, alignment=Qt.AlignCenter)

        fourth_question_screen.setLayout(fourth_question_layout)
        self.stack.addWidget(fourth_question_screen)

    def create_fourth_support_screen(self):
        """Support options screen for Action 4."""
        support_screen = QWidget()
        support_layout = QVBoxLayout()

        # Support header
        header_label = QLabel("Tell us if you think any of the support we can provide would be useful to you:")
        header_label.setAlignment(Qt.AlignCenter)
        header_label.setFont(QFont('Arial', 14))
        support_layout.addWidget(header_label)

        # Grid layout for support options
        support_grid = QGridLayout()

        options = [
            ("Working Out Who Can Support You", "your_image.png"),
            ("Connecting with Supportive Groups", "your_image.png"),
            ("Accountability Buddy", "your_image.png")
        ]

        for i, (title, img) in enumerate(options):
            option_layout = QVBoxLayout()
            option_button = QPushButton()
            option_button.setIcon(QIcon(img))
            option_button.setIconSize(QSize(120, 120))
            option_button.clicked.connect(lambda _, t=title: self.show_support_popup(t))  # Capture title correctly
            option_layout.addWidget(option_button)
            option_label = QLabel(title)
            option_label.setAlignment(Qt.AlignCenter)
            option_layout.addWidget(option_label)
            support_grid.addLayout(option_layout, i // 2, i % 2)

        support_layout.addLayout(support_grid)

        # NEXT button
        next_button = QPushButton("NEXT")
        next_button.setStyleSheet("background-color: #FF69B4; color: white; border-radius: 15px;")
        next_button.setFixedSize(100, 50)
        next_button.clicked.connect(self.go_to_reflective_screen)
        support_layout.addWidget(next_button, alignment=Qt.AlignCenter)

        support_screen.setLayout(support_layout)
        self.stack.addWidget(support_screen)

    def go_to_fourth_support_screen(self):
        """Navigate to the fourth support screen."""
        self.stack.setCurrentIndex(9)

    def create_reflective_screen(self):
        """Final reflective screen showing the user's response and selected supports."""
        reflective_screen = QWidget()
        reflective_layout = QVBoxLayout()

        # Reflective message
        reflective_label = QLabel("You said you wanted to change your life by:")
        reflective_label.setAlignment(Qt.AlignCenter)
        reflective_label.setFont(QFont('Arial', 14))
        reflective_layout.addWidget(reflective_label)

        # User's response (what they want to change)
        response_label_text = f"I want to {self.user_response}." if self.user_response else "(No input provided)"
        response_label = QLabel(response_label_text)
        response_label.setAlignment(Qt.AlignCenter)
        response_label.setFont(QFont('Arial', 16, QFont.Bold))
        reflective_layout.addWidget(response_label)

        # Instructions message
        instructions_label = QLabel("To do this, you’ve indicated that you could benefit from:")
        instructions_label.setAlignment(Qt.AlignCenter)
        instructions_label.setFont(QFont('Arial', 14))
        reflective_layout.addWidget(instructions_label)

        # Display the selected supports
        if self.selected_supports:
            for support in self.selected_supports:
                support_button = QPushButton(support)
                support_button.setStyleSheet("border: 1px solid lightgray; padding: 10px; border-radius: 10px;")
                support_button.setFixedHeight(50)
                reflective_layout.addWidget(support_button)
        else:
            no_support_label = QLabel("You did not select any support options.")
            no_support_label.setAlignment(Qt.AlignCenter)
            no_support_label.setFont(QFont('Arial', 14))
            reflective_layout.addWidget(no_support_label)

        # FINISH button to conclude
        finish_button = QPushButton("FINISH")
        finish_button.setStyleSheet("background-color: #FF69B4; color: white; border-radius: 15px; padding: 10px;")
        finish_button.setFixedSize(100, 50)
        finish_button.clicked.connect(self.show_completion_message)
        reflective_layout.addWidget(finish_button, alignment=Qt.AlignCenter)

        reflective_screen.setLayout(reflective_layout)
        self.stack.addWidget(reflective_screen)

    def show_support_popup(self, selected_support):
        """Show a pop-up message informing the user of their selected support option."""
        if selected_support not in self.selected_supports:
            self.selected_supports.append(selected_support)  # Add selected support to list if not already selected
        QMessageBox.information(self, "Support Selection", f"You selected: {selected_support}")

    def go_to_reflective_screen(self):
        """Navigate to the final reflective screen."""
        # Refresh the reflective screen with latest user inputs
        self.stack.removeWidget(self.stack.widget(10))  # Remove old reflective screen
        self.create_reflective_screen()
        self.stack.setCurrentIndex(10)  # Show updated reflective screen

    def show_completion_message(self):
        """Show a completion message after the last Yes/No question."""
        QMessageBox.information(self, "Action Plan", "Great! You've reflected and created an action plan. You're ready to take the next step.")

# Application Entry
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ReflectionApp()
    window.show()
    sys.exit(app.exec_())
