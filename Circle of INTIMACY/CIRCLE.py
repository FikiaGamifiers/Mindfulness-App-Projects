import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window size and title
        self.setWindowTitle("Analyzing Conversations")
        self.setGeometry(90, 90, 300, 1100)

        # Start with the first window
        self.init_first_window()

    def init_first_window(self):
        # Create a central widget and layout with padding
        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(70, 100, 70, 50)  # Padding: left, top, right, bottom
        layout.setSpacing(40)  # Space between widgets

        # Title Label
        title_label = QLabel("ANALYSE THE CONVERSATION", self)
        title_label.setAlignment(Qt.AlignCenter)
        title_font = QFont("Arial", 28, QFont.Bold)
        title_label.setFont(title_font)

        # Subtitle Label
        subtitle_label = QLabel("Alex Mercer is an international spy working for ‘The Division’.", self)
        subtitle_label.setAlignment(Qt.AlignCenter)
        subtitle_font = QFont("Arial", 16)
        subtitle_label.setFont(subtitle_font)

        # Description Label
        description_text = (
            "As Alex goes about his mission he gets into several conversations. Analyse "
            "these to work out where people are using their childlike, parentlike, or "
            "adultlike parts of themselves."
        )
        description_label = QLabel(description_text, self)
        description_label.setAlignment(Qt.AlignCenter)
        description_label.setWordWrap(True)
        description_label.setFont(subtitle_font)

        # Bullet Points
        bullet_text = (
            "• Childlike Part: Emotional and reactive, driven by feelings and impulses.\n\n"
            "• Parentlike Part: Authoritative and judgmental, enforcing rules and expectations.\n\n"
            "• Adultlike Part: Rational and balanced, focused on logic and problem-solving."
        )
        bullet_label = QLabel(bullet_text, self)
        bullet_label.setAlignment(Qt.AlignCenter)
        bullet_label.setWordWrap(True)
        bullet_font = QFont("Arial", 14)
        bullet_label.setFont(bullet_font)

        # Start Button
        start_button = QPushButton("Start", self)
        start_button.setFixedSize(150, 50)
        start_button_font = QFont("Arial", 14)
        start_button.setFont(start_button_font)

        # Styling the button with rounded corners and color
        start_button.setStyleSheet("""
            QPushButton {
                background-color: #e3007a;
                color: white;
                border-radius: 15px;
            }
            QPushButton:hover {
                background-color: #ff5806;
            }
        """)

        # Connect the Start button to the method that updates the window
        start_button.clicked.connect(self.update_to_second_window)
        
        # Add widgets to the layout
        layout.addWidget(title_label)
        layout.addWidget(subtitle_label)
        layout.addWidget(description_label)
        layout.addWidget(bullet_label)
        layout.addStretch()  # Add space between bullet points and button
        layout.addWidget(start_button, alignment=Qt.AlignCenter)

        # Set the central widget
        self.setCentralWidget(central_widget)

    def update_to_second_window(self):
        # Clear the central widget
        self.centralWidget().deleteLater()

        # Create a new central widget and layout
        central_widget = QWidget(self)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(70, 50, 70, 50)  # Reduced top margin
        main_layout.setSpacing(10)  # Reduced spacing between title and message box

        # Title Label
        title_label = QLabel("ANALYSE THE CONVERSATION", self)
        title_label.setAlignment(Qt.AlignCenter)
        title_font = QFont("Arial", 28, QFont.Bold)
        title_label.setFont(title_font)

        # Message Label with embedded Director Evelyn Chase
        message_text = QLabel("Director Evelyn Chase\n\nAlex, this mission is critical. Retrieve the data and extract "
                              "without making a scene. Failure is not an option.", self)
        message_text.setFont(QFont("Arial", 14))
        message_text.setAlignment(Qt.AlignCenter)  # Center-align the text inside the message box
        message_text.setWordWrap(True)
        message_text.setStyleSheet("background-color: #f4c7d9; padding: 15px; border-radius: 10px; color: #e3007a;")

        # Image Label
        image_label = QLabel(self)
        pixmap = QPixmap("image.png")

        # Scale the image to increase its size
        scaled_pixmap = pixmap.scaled(1100, 1100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        image_label.setPixmap(scaled_pixmap)
        image_label.setAlignment(Qt.AlignCenter)  # Center the image

        # Next Button
        next_button = QPushButton("Next", self)
        next_button.setFixedSize(150, 50)
        next_button_font = QFont("Arial", 14)
        next_button.setFont(next_button_font)
        next_button.setStyleSheet("""
            QPushButton {
                background-color: #e3007a;
                color: white;
                border-radius: 15px;
            }
            QPushButton:hover {
                background-color: #ff5806;
            }
        """)

        # Connect the Next button to the method that updates the window to the third page
        next_button.clicked.connect(self.update_to_third_window)

        # Add widgets to the main layout
        main_layout.addWidget(title_label)
        main_layout.addWidget(message_text)
        main_layout.addWidget(image_label)
        main_layout.addWidget(next_button, alignment=Qt.AlignCenter)  # Add Next button below the image

        # Set the central widget with the new layout
        self.setCentralWidget(central_widget)

    def update_to_third_window(self):
        # Clear the central widget
        self.centralWidget().deleteLater()

        # Create a new central widget and layout
        central_widget = QWidget(self)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(70, 50, 70, 50)  # Adjusted margins
        main_layout.setSpacing(10)

        # Title Label
        title_label = QLabel("ANALYSE THE CONVERSATION", self)
        title_label.setAlignment(Qt.AlignCenter)
        title_font = QFont("Arial", 28, QFont.Bold)
        title_label.setFont(title_font)

        # Subtitle Label
        subtitle_label = QLabel("What part of self was this spoken from?", self)
        subtitle_label.setAlignment(Qt.AlignCenter)
        subtitle_font = QFont("Arial", 16)
        subtitle_label.setFont(subtitle_font)

        # Message Label with embedded Director Evelyn Chase
        message_text = QLabel("Director Evelyn Chase\n\nAlex, this mission is critical. Retrieve the data and extract "
                              "without making a scene. Failure is not an option.", self)
        message_text.setFont(QFont("Arial", 14))
        message_text.setAlignment(Qt.AlignCenter)
        message_text.setWordWrap(True)
        message_text.setStyleSheet("background-color: #f4c7d9; padding: 15px; border-radius: 10px; color: #e3007a;")

        # Dynamic Response Label
        self.response_label = QLabel("", self)
        self.response_label.setFont(QFont("Arial", 14))
        self.response_label.setAlignment(Qt.AlignCenter)
        self.response_label.setWordWrap(True)

        # Buttons for Adult, Parent, and Child
        adult_button = QPushButton("Adult", self)
        parent_button = QPushButton("Parent", self)
        child_button = QPushButton("Child", self)

        # Button styling
        for button in [adult_button, parent_button, child_button]:
            button.setFixedSize(120, 50)
            button.setFont(QFont("Arial", 14))
            button.setStyleSheet("""
                QPushButton {
                    background-color: white;
                    color: #003366;
                    border: 2px solid #003366;
                    border-radius: 15px;
                }
                QPushButton:hover {
                    background-color: #f2f2f2;
                }
                QPushButton:pressed {
                    background-color: #123456;
                    color: white;
                }
            """)

        # Connect buttons to their respective functions
        adult_button.clicked.connect(self.display_adult_message)
        parent_button.clicked.connect(self.display_parent_message)
        child_button.clicked.connect(self.display_child_message)

        # Layout for the buttons
        button_layout = QHBoxLayout()
        button_layout.addWidget(adult_button)
        button_layout.addWidget(parent_button)
        button_layout.addWidget(child_button)
        button_layout.setSpacing(20)  # Space between buttons

        # Submit Button
        submit_button = QPushButton("Submit", self)
        submit_button.setFixedSize(150, 50)
        submit_button_font = QFont("Arial", 14)
        submit_button.setFont(submit_button_font)
        submit_button.setStyleSheet("""
            QPushButton {
                background-color: #e3007a;
                color: white;
                border-radius: 15px;
            }
            QPushButton:hover {
                background-color: #ff5806;
            }
            QPushButton:pressed {
                background-color: #99004c;
            }
        """)
        submit_button.setEnabled(False)  # Disable submit button initially

        # Store the submit button reference
        self.submit_button = submit_button

        # Add widgets to the main layout
        main_layout.addWidget(title_label)
        main_layout.addWidget(subtitle_label)
        main_layout.addWidget(message_text)
        main_layout.addLayout(button_layout)  # Add buttons layout
        main_layout.addWidget(self.response_label)
        main_layout.addWidget(submit_button, alignment=Qt.AlignCenter)  # Add Submit button

        # Set the central widget with the new layout
        self.setCentralWidget(central_widget)

        # Connect submit button to the fourth window
        submit_button.clicked.connect(self.update_to_fourth_window)

    def update_to_fourth_window(self):
        # Clear the central widget
        self.centralWidget().deleteLater()

        # Initialize the sequence of images and texts
        self.current_index = 0  # Start at the first image and text
        self.image_paths = [
            "/mnt/data/image.png",  # Replace with actual paths
            "/mnt/data/image-1OTjBaYWnEEOJdfTlCqitmAw.png",
            "/mnt/data/image-o1YFL36qC4lk3yD7UHElXpuC.png",
            "/mnt/data/image-pvUK5ZSe9zv6RmfIEX9j0aA7.png"
        ]
        self.texts = [
            "Alex Mercer\n\nAlmost there. Keep it quiet.",
            "Alex Mercer\n\nJust a few more seconds...",
            "Alex Mercer\n\nGot it. Stay focused. In and out, no complications.",
            "Alex Mercer\n\nMission accomplished. Let's head back."
        ]

        # Create a new central widget and layout
        central_widget = QWidget(self)
        self.main_layout = QVBoxLayout(central_widget)
        self.main_layout.setContentsMargins(70, 50, 70, 50)  # Adjusted margins
        self.main_layout.setSpacing(20)

        # Title Label
        title_label = QLabel("ANALYSE THE CONVERSATION", self)
        title_label.setAlignment(Qt.AlignCenter)
        title_font = QFont("Arial", 28, QFont.Bold)
        title_label.setFont(title_font)

        # Message Label
        self.message_text = QLabel(self.texts[self.current_index], self)
        self.message_text.setFont(QFont("Arial", 16))
        self.message_text.setAlignment(Qt.AlignLeft)  # Align text to the left as per the design
        self.message_text.setWordWrap(True)
        self.message_text.setStyleSheet("""
            background-color: #e0e7ff; 
            padding: 20px; 
            border-radius: 15px; 
            color: #2f2f2f;
        """)

        # Image Label with Navigation Arrows
        self.image_label = QLabel(self)
        self.update_image_and_text()  # Set initial image and text
        self.image_label.setAlignment(Qt.AlignCenter)  # Center the image

        # Create navigation arrow labels
        self.left_arrow = QLabel("←", self)
        self.left_arrow.setFont(QFont("Arial", 48))
        self.left_arrow.setAlignment(Qt.AlignCenter)
        self.left_arrow.setStyleSheet("color: #e3007a;")

        self.right_arrow = QLabel("→", self)
        self.right_arrow.setFont(QFont("Arial", 48))
        self.right_arrow.setAlignment(Qt.AlignCenter)
        self.right_arrow.setStyleSheet("color: #e3007a;")

        # Layout for the image and arrows
        image_layout = QHBoxLayout()
        image_layout.addWidget(self.left_arrow, alignment=Qt.AlignLeft)
        image_layout.addWidget(self.image_label, alignment=Qt.AlignCenter)
        image_layout.addWidget(self.right_arrow, alignment=Qt.AlignRight)

        # Add mouse event handling to the image and arrows
        self.image_label.mousePressEvent = self.handle_image_click
        self.left_arrow.mousePressEvent = self.handle_left_arrow_click
        self.right_arrow.mousePressEvent = self.handle_right_arrow_click

        # Next Button (Initially Hidden)
        self.next_button = QPushButton("NEXT", self)
        self.next_button.setFixedSize(150, 50)
        next_button_font = QFont("Arial", 16)
        self.next_button.setFont(next_button_font)
        self.next_button.setStyleSheet("""
            QPushButton {
                background-color: #e3007a;
                color: white;
                border-radius: 25px;
            }
            QPushButton:hover {
                background-color: #ff5806;
            }
        """)
        self.next_button.setVisible(False)  # Hide the button initially

        # Connect the Next button to the next window (if you have more pages)
        # self.next_button.clicked.connect(self.update_to_fifth_window)

        # Add widgets to the main layout
        self.main_layout.addWidget(title_label)
        self.main_layout.addWidget(self.message_text)
        self.main_layout.addLayout(image_layout)  # Add the image layout with arrows
        self.main_layout.addStretch()  # Add stretch to push the button to the bottom
        self.main_layout.addWidget(self.next_button, alignment=Qt.AlignCenter)

        # Set the central widget with the new layout
        self.setCentralWidget(central_widget)

    def update_image_and_text(self):
        """Update the image and text based on the current index."""
        pixmap = QPixmap(self.image_paths[self.current_index])
        scaled_pixmap = pixmap.scaled(600, 600, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.image_label.setPixmap(scaled_pixmap)
        self.message_text.setText(self.texts[self.current_index])

    def handle_image_click(self, event):
        """Handle left or right click on the image."""
        if event.button() == Qt.LeftButton:
            self.handle_left_arrow_click(event)
        elif event.button() == Qt.RightButton:
            self.handle_right_arrow_click(event)

    def handle_left_arrow_click(self, event):
        """Handle left arrow click."""
        if self.current_index > 0:
            self.current_index -= 1
            self.update_image_and_text()
            self.next_button.setVisible(False)

    def handle_right_arrow_click(self, event):
        """Handle right arrow click."""
        if self.current_index < len(self.image_paths) - 1:
            self.current_index += 1
            self.update_image_and_text()

        # Show the Next button if we've reached the last image
        if self.current_index == len(self.image_paths) - 1:
            self.next_button.setVisible(True)
        else:
            self.next_button.setVisible(False)

    def display_adult_message(self):
        self.response_label.setText("We would disagree with you:\n\nThis message sounds more like an example of the Parent part rather than the Adult part.")
        self.submit_button.setEnabled(False)  # Keep submit button disabled

    def display_parent_message(self):
        self.response_label.setText("We would agree with you:\n\nWe think this sounds like an example of the critical parent. By explicitly mentioning that the data must be retrieved without making a scene, it implies that Alex would make a scene (something generally not considered positive).")
        self.submit_button.setEnabled(True)  # Enable submit button

    def display_child_message(self):
        self.response_label.setText("We would disagree with you:\n\nWe think this sounds like an example of the critical parent. By explicitly mentioning that the data must be retrieved without making a scene, it implies that Alex would make a scene (something generally not considered positive).")
        self.submit_button.setEnabled(False)  # Keep submit button disabled

app = QApplication(sys.argv)

window = MainWindow()

window.show()
sys.exit(app.exec_())
