import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

# Define the card data (image paths and questions)
cards = [
    {"image": "card1.png", "question": "What emotions or thoughts arise when you are in a situation where the outcome is unclear or the path is obscured?"},
    {"image": "card2.png", "question": "What might be holding you back from stepping into new opportunities or experiences in your life?"},
    {"image": "card3.png", "question": "How do you find stability or hope when faced with turbulent situations or emotional storms?"},
    {"image": "card4.png", "question": "In what ways do you feel fragmented or disconnected from your sense of self, and what might be contributing to this?"},
    {"image": "card5.png", "question": "What transitional phases are you currently experiencing, and what uncertainties do they bring?"},
    {"image": "card6.png", "question": "What are the sources of nourishment and support in your life that help you sustain yourself during challenging times?"},
    {"image": "card7.png", "question": "What aspects of yourself or your life feel obscured or hidden from view, and how do you feel about this?"},
    {"image": "card8.png", "question": "What decisions or choices are you currently grappling with, and how do you weigh the different options available to you?"},
    {"image": "card9.png", "question": "How do you feel about revealing your true self to others, and what influences your level of openness or secrecy?"},
    {"image": "card10.png", "question": "What dreams or aspirations feel distant or unclear to you, and how do you approach the pursuit of these goals?"},
    {"image": "card11.png", "question": "What reflections or realizations might emerge if you took a step back and view your life from a broader perspective?"},
    {"image": "card12.png", "question": "How do you handle the sense of following in someone else’s footsteps versus creating your own path?"},
    {"image": "card13.png", "question": "What past experiences or memories do you find difficult to revisit, and how do you approach confronting or integrating these aspects of your history?"},
    {"image": "card14.png", "question": "How do you cope with feelings of solitude or moments when you feel disconnected from others?"},
    {"image": "card15.png", "question": "How do you feel about the passage of time and the way it impacts your life and decisions?"},
    {"image": "card16.png", "question": "How do you deal with moments of darkness or uncertainty, and what sources of light or hope do you rely on?"},
    {"image": "card17.png", "question": "What role does patience and perseverance play in your journey through periods of ambiguity?"},
    {"image": "card18.png", "question": "What steps are you currently taking to reach your goals and what motivates you to continue?"}
]

class CardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Think About")
        self.root.geometry("600x800")
        self.root.configure(bg="white")

        self.current_card_index = 0  # Track current card index

        # Create title label
        self.title_label = tk.Label(self.root, text="THINK ABOUT", font=("Helvetica", 32, "bold"), bg="white", fg="#13294B")
        self.title_label.pack(pady=20)

        # Create a frame to hold the card image and question
        self.card_frame = tk.Frame(self.root, bg="white")
        self.card_frame.pack(pady=10)

        # Create UI components within the frame
        self.card_label = tk.Label(self.card_frame, bg="white")
        self.card_label.pack(pady=(10, 0))

        self.question_label = tk.Label(self.card_frame, text="", wraplength=500, justify="center", font=("Arial", 14), bg="white", fg="black")
        self.question_label.pack(pady=(10, 20))  # Bring text closer to the image

        # Create button frame for better control of button positioning
        self.button_frame = tk.Frame(self.root, bg="white")
        self.button_frame.pack(pady=20)

        # Create buttons with rounded corners
        self.try_another_button = tk.Button(self.button_frame, text="Try Another", command=self.try_another, bg="#E0007F", fg="white", font=("Arial", 12, "bold"), relief="flat", padx=20, pady=10, bd=0, highlightthickness=0)
        self.try_another_button.pack(side=tk.LEFT, padx=20)
        self.try_another_button.config(borderwidth=1, highlightbackground="#E0007F", highlightcolor="#E0007F", relief="solid")
        self.try_another_button.config(cursor="hand2")

        self.finish_button = tk.Button(self.button_frame, text="Finish", command=self.finish, bg="#E0007F", fg="white", font=("Arial", 12, "bold"), relief="flat", padx=20, pady=10, bd=0, highlightthickness=0)
        self.finish_button.pack(side=tk.RIGHT, padx=20)
        self.finish_button.config(borderwidth=1, highlightbackground="#E0007F", highlightcolor="#E0007F", relief="solid")
        self.finish_button.config(cursor="hand2")

        # Apply hover effects
        self.apply_hover_effects(self.try_another_button, "#E0007F", "#C0005E")
        self.apply_hover_effects(self.finish_button, "#E0007F", "#C0005E")

        # Load the first card
        self.show_card()

    def apply_hover_effects(self, button, normal_color, hover_color):
        button.config(bg=normal_color, activebackground=hover_color)
        button.bind("<Enter>", lambda e: button.config(bg=hover_color))
        button.bind("<Leave>", lambda e: button.config(bg=normal_color))

    def show_card(self):
        if self.current_card_index >= len(cards):
            self.finish()
            return

        card_image_path = cards[self.current_card_index]["image"]

        # Check if the image file exists
        if not os.path.exists(card_image_path):
            messagebox.showerror("Error", f"Image {card_image_path} not found.")
            return
        
        card_image = Image.open(card_image_path)

        # Resize the image to fit into a square, keeping the aspect ratio
        max_side = 600
        card_image.thumbnail((max_side, max_side), Image.Resampling.LANCZOS)

        # Create a blank white image of size (max_side, max_side)
        square_image = Image.new("RGBA", (max_side, max_side), (255, 255, 255, 0))

        # Center the resized image on the blank square image
        offset = ((max_side - card_image.width) // 2, (max_side - card_image.height) // 2)
        square_image.paste(card_image, offset)

        card_photo = ImageTk.PhotoImage(square_image)

        # Update the label with the new image
        self.card_label.config(image=card_photo)
        self.card_label.image = card_photo

        # Update the question label
        card_question = cards[self.current_card_index]["question"]
        self.question_label.config(text=card_question)

        # Move to the next card
        self.current_card_index += 1

    def try_another(self):
        self.show_card()

    def finish(self):
        messagebox.showinfo("Finish", "Thank you for using the Card App!")
        self.root.destroy()  # Close the application window

# Main application
if __name__ == "__main__":
    root = tk.Tk()
    app = CardApp(root)
    root.mainloop()
