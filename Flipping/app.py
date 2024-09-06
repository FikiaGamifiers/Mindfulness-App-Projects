import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QSlider, QStackedWidget, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont

class FlipWidget(QWidget):
    def __init__(self, front_image_path, back_text, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Front Side (Image)
        self.front_label = QLabel(self)
        self.front_label.setPixmap(QPixmap(front_image_path).scaled(600, 400, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.front_label.setAlignment(Qt.AlignCenter)

        # Back Side (Text)
        self.back_label = QLabel(back_text, self)
        self.back_label.setStyleSheet("font-size: 18px; padding: 20px;")
        self.back_label.setAlignment(Qt.AlignCenter)
        self.back_label.setWordWrap(True)

        # StackedWidget to hold both front and back
        self.stack = QStackedWidget(self)
        self.stack.addWidget(self.front_label)
        self.stack.addWidget(self.back_label)

        layout = QVBoxLayout(self)
        layout.addWidget(self.stack)

        # Handle flipping
        self.front_label.mousePressEvent = self.flip_to_back
        self.back_label.mousePressEvent = self.flip_to_front

    def flip_to_back(self, event):
        self.stack.setCurrentIndex(1)

    def flip_to_front(self, event):
        self.stack.setCurrentIndex(0)


class BoundaryApp(QWidget):
    def __init__(self):
        super().__init__()

        self.boundary_categories = [
            {
                "label": "What boundaries do you have with {name} for personal space and amount of touch that you feel comfortable with?",
                "flip_widgets": [
                    FlipWidget(
                        front_image_path="porous_touch.png",
                        back_text="• You let others invade your personal space, feeling uncomfortable but unable to say no.\n"
                                  "• You tolerate unwanted touch to avoid conflict or please others.\n"
                                  "• You struggle to express your need for space, leading to discomfort or resentment."
                    ),
                    FlipWidget(
                        front_image_path="healthy_touch.png",
                        back_text="• You express your comfort with touch and personal space clearly.\n"
                                  "• You welcome appropriate contact and confidently reject unwanted touch.\n"
                                  "• You adjust boundaries based on the situation, allowing closeness with trusted people."
                    ),
                    FlipWidget(
                        front_image_path="rigid_touch.png",
                        back_text="• You keep a large distance from others, avoiding touch and closeness.\n"
                                  "• You avoid social situations to prevent contact, resulting in loneliness.\n"
                                  "• You set inflexible personal space rules, rejecting affection even when appropriate."
                    )
                ]
            },
            {
                "label": "What boundaries do you have with {name} for your ideas and beliefs and how much you are open to sharing them?",
                "flip_widgets": [
                    FlipWidget(
                        front_image_path="porous_beliefs.png",
                        back_text="• Freely sharing ideas with those who may not respect them, leading to feeling undervalued.\n"
                                  "• Agreeing with others to avoid conflict, often compromising your beliefs.\n"
                                  "• Adjusting opinions to fit in, driven by concern over others’ perceptions."
                    ),
                    FlipWidget(
                        front_image_path="healthy_beliefs.png",
                        back_text="• You express your comfort with sharing ideas clearly.\n"
                                  "• You welcome appropriate discussions and confidently stand by your beliefs.\n"
                                  "• You adjust your openness based on the situation, allowing constructive feedback from trusted people."
                    ),
                    FlipWidget(
                        front_image_path="rigid_beliefs.png",
                        back_text="• Stubbornly holding onto beliefs, refusing new perspectives, hindering growth.\n"
                                  "• Criticizing others' views without consideration, blocking communication.\n"
                                  "• Believing your ideas are superior, avoiding dialogue or collaboration."
                    )
                ]
            }
        ]

        self.current_category_index = 0
        self.selected_boundaries = ["Porous", "Porous"]  # Default selections

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 600, 800)
        self.setWindowTitle("Boundary Exploration")

        # Main layout for switching between screens
        self.stacked_widget = QStackedWidget(self)
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.stacked_widget)

        # Name input screen
        self.name_input_screen = QWidget()
        self.init_name_input_screen()
        self.stacked_widget.addWidget(self.name_input_screen)

        # Boundary identification screen
        self.boundary_screen = QWidget()
        self.init_boundary_screen()
        self.stacked_widget.addWidget(self.boundary_screen)

        # Summary screen
        self.summary_screen = QWidget()
        self.init_summary_screen()
        self.stacked_widget.addWidget(self.summary_screen)

        # Show the name input screen first
        self.stacked_widget.setCurrentWidget(self.name_input_screen)

    def init_name_input_screen(self):
        layout = QVBoxLayout(self.name_input_screen)
        layout.setAlignment(Qt.AlignCenter)

        # Title
        title = QLabel("BOUNDARY EXPLORATION")
        title.setStyleSheet("font-size: 40px; font-weight: bold; color: #00cc44;")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Question Label
        question_label = QLabel("Who do you struggle to set healthy boundaries with:")
        question_label.setStyleSheet("font-size: 20px;")
        question_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(question_label)

        # Name input label and field
        name_layout = QHBoxLayout()
        name_label = QLabel("Name:  ")
        name_label.setStyleSheet("font-size: 20px;")
        name_label.setAlignment(Qt.AlignRight)

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("_______________________")
        self.name_input.setFont(QFont("Arial", 20))
        self.name_input.setAlignment(Qt.AlignLeft)

        name_layout.addWidget(name_label)
        name_layout.addWidget(self.name_input)
        layout.addLayout(name_layout)

        # Next button
        next_button = QPushButton("NEXT")
        next_button.setStyleSheet("background-color: #ff0066; color: white; font-size: 18px; padding: 10px 20px;")
        next_button.clicked.connect(self.go_to_boundary_screen)
        layout.addWidget(next_button, alignment=Qt.AlignCenter)

    def go_to_boundary_screen(self):
        self.person_name = self.name_input.text().strip()
        if not self.person_name:  # Check if name is empty
            QMessageBox.warning(self, "Input Error", "Please enter a name before proceeding.")
            return  # Stop here if no name is entered

        # Reset the slider to the beginning
        self.boundary_slider.setValue(0)
        self.update_boundary_info()
        self.stacked_widget.setCurrentWidget(self.boundary_screen)

    def init_boundary_screen(self):
        layout = QVBoxLayout(self.boundary_screen)

        # Title
        self.boundary_label = QLabel("")
        self.boundary_label.setStyleSheet("font-size: 18px;")
        self.boundary_label.setWordWrap(True)
        self.boundary_label.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.boundary_label)

        # Slider for selecting the boundary type
        self.boundary_slider = QSlider(Qt.Horizontal)
        self.boundary_slider.setMinimum(0)
        self.boundary_slider.setMaximum(2)
        self.boundary_slider.setSingleStep(1)
        self.boundary_slider.setFixedWidth(300)
        self.boundary_slider.valueChanged.connect(self.update_boundary_info)
        self.boundary_type_label = QLabel("Porous")
        self.boundary_type_label.setStyleSheet("font-size: 24px;")
        self.boundary_type_label.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.boundary_type_label)
        layout.addWidget(self.boundary_slider, alignment=Qt.AlignCenter)

        # Placeholder for flip widget, initially the first widget of the first category
        self.current_flip_widget = self.boundary_categories[self.current_category_index]["flip_widgets"][0]
        layout.addWidget(self.current_flip_widget)

        # Navigation buttons
        nav_layout = QHBoxLayout()
        prev_button = QPushButton("PREVIOUS")
        prev_button.setStyleSheet("background-color: #ff0066; color: white; font-size: 18px; padding: 10px 20px;")
        prev_button.clicked.connect(self.previous_category)
        next_button = QPushButton("NEXT")
        next_button.setStyleSheet("background-color: #ff0066; color: white; font-size: 18px; padding: 10px 20px;")
        next_button.clicked.connect(self.next_category)

        nav_layout.addWidget(prev_button)
        nav_layout.addWidget(next_button)

        layout.addLayout(nav_layout)

    def init_summary_screen(self):
        layout = QVBoxLayout(self.summary_screen)
        layout.setAlignment(Qt.AlignCenter)

        # Title
        title = QLabel("BOUNDARY EXPLORATION")
        title.setStyleSheet("font-size: 40px; font-weight: bold; color: #00cc44;")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Summary of boundaries
        self.summary_label = QLabel("")
        self.summary_label.setStyleSheet("font-size: 24px;")
        self.summary_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.summary_label)

        # Physical boundaries summary
        self.physical_summary = QLabel("Physical boundaries:")
        self.physical_summary.setStyleSheet("font-size: 18px;")
        self.physical_image = QLabel()
        self.physical_image.setPixmap(QPixmap("porous_touch.png").scaled(150, 150, Qt.KeepAspectRatio))
        layout.addWidget(self.physical_summary)
        layout.addWidget(self.physical_image)

        # Intellectual boundaries summary
        self.intellectual_summary = QLabel("Intellectual boundaries:")
        self.intellectual_summary.setStyleSheet("font-size: 18px;")
        self.intellectual_image = QLabel()
        self.intellectual_image.setPixmap(QPixmap("porous_beliefs.png").scaled(150, 150, Qt.KeepAspectRatio))
        layout.addWidget(self.intellectual_summary)
        layout.addWidget(self.intellectual_image)

        # Finish button
        finish_button = QPushButton("Finish")
        finish_button.setStyleSheet("background-color: #ff0066; color: white; font-size: 18px; padding: 10px 20px;")
        layout.addWidget(finish_button, alignment=Qt.AlignCenter)

    def update_boundary_info(self):
        boundary_types = ["Porous", "Healthy", "Rigid"]
        selected_index = self.boundary_slider.value()

        # Update the displayed boundary type label
        self.boundary_type_label.setText(boundary_types[selected_index])

        # Store the selected boundary for the current category
        self.selected_boundaries[self.current_category_index] = boundary_types[selected_index]

        # Replace the current flip widget with the new one corresponding to the slider's position
        self.boundary_screen.layout().removeWidget(self.current_flip_widget)
        self.current_flip_widget.setParent(None)  # This prevents the widget from being destroyed

        self.current_flip_widget = self.boundary_categories[self.current_category_index]["flip_widgets"][selected_index]
        self.boundary_screen.layout().insertWidget(1, self.current_flip_widget)

        # Update the boundary label text based on the selected category
        self.boundary_label.setText(self.boundary_categories[self.current_category_index]["label"].format(name=self.person_name))

    def previous_category(self):
        if self.current_category_index > 0:
            self.current_category_index -= 1
            self.update_boundary_info()

    def next_category(self):
        if self.current_category_index < len(self.boundary_categories) - 1:
            self.current_category_index += 1
            self.update_boundary_info()
        else:
            self.show_summary()

    def show_summary(self):
        # Update the summary screen with the selected boundaries and corresponding images
        self.summary_label.setText(f"The boundaries you have with {self.person_name}")

        # Update physical boundaries summary
        physical_boundary_type = self.selected_boundaries[0]
        self.physical_summary.setText(f"Physical boundaries:\n{physical_boundary_type}")
        self.physical_image.setPixmap(QPixmap(f"{physical_boundary_type.lower()}_touch.png").scaled(150, 150, Qt.KeepAspectRatio))

        # Update intellectual boundaries summary
        intellectual_boundary_type = self.selected_boundaries[1]
        self.intellectual_summary.setText(f"Intellectual boundaries:\n{intellectual_boundary_type}")
        self.intellectual_image.setPixmap(QPixmap(f"{intellectual_boundary_type.lower()}_beliefs.png").scaled(150, 150, Qt.KeepAspectRatio))

        # Switch to the summary screen
        self.stacked_widget.setCurrentWidget(self.summary_screen)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = BoundaryApp()
    ex.show()
    sys.exit(app.exec_())
