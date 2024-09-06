import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class ADHDApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ADHD Signs of People-Pleasing")
        self.root.geometry("500x1000")
        self.root.resizable(True, True)

        self.options = [
            "Struggling to express our true feelings, even when asked directly",
            "Feeling like we always \"should have done better\" for them",
            "Letting toxic people back into our lives",
            "Hate asserting boundaries for potentially upsetting someone",
            "Difficulties knowing what we truly want for ourselves",
            "Neglecting our own needs to assist others",
            "Beating ourselves up for things that we excuse others on"
        ]

        self.image_files = [
            "image_1.png",
            "image_2.png",
            "image_3.png",
            "image_4.png",
            "image_5.png",
            "image_6.png",
            "image_7.png",
        ]

        self.selected_options = [tk.BooleanVar() for _ in self.options]

        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self.root)
        self.scrollbar = tk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.title_label = tk.Label(self.scrollable_frame, text="ADHD SIGNS OF PEOPLE-PLEASING", font=("Helvetica", 20, "bold"))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.subtitle_label = tk.Label(self.scrollable_frame, text="Select all that apply to you", font=("Arial", 14))
        self.subtitle_label.grid(row=1, column=0, columnspan=2, pady=10)

        for index, (option, image_file) in enumerate(zip(self.options, self.image_files)):
            image = Image.open(image_file)
            image = image.resize((150, 200), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            button = tk.Checkbutton(
                self.scrollable_frame,
                image=photo,
                text=option,
                variable=self.selected_options[index],
                compound="top",
                wraplength=200,
                justify=tk.CENTER,
                indicatoron=False,
                padx=10,
                pady=10,
                font=("Arial", 10),
                bg="light blue",
                selectcolor="light blue"
            )
            button.image = photo  # keep a reference to prevent garbage collection
            button.grid(row=(index // 2) + 2, column=index % 2, padx=10, pady=10)

            # Add hover effect
            button.bind("<Enter>", lambda e, b=button: b.config(bg="light green"))
            button.bind("<Leave>", lambda e, b=button: b.config(bg="light blue"))

        self.next_button = tk.Button(self.scrollable_frame, text="NEXT", command=self.on_next, bg="#FF007F", fg="white", font=("Arial", 12, "bold"), width=20, height=2)
        self.next_button.grid(row=(len(self.options) // 2) + 3, column=0, columnspan=2, pady=20)

    def on_next(self):
        selected = [option.get() for option in self.selected_options]
        selected_texts = [self.options[i] for i in range(len(selected)) if selected[i]]
        if selected_texts:
            self.show_selected_window(selected_texts)
        else:
            messagebox.showwarning("No Selection", "Please select at least one option.")

    def show_selected_window(self, selected_texts):
        selected_window = tk.Toplevel(self.root)
        selected_window.title("Selected ADHD Signs of People-Pleasing")
        selected_window.geometry("500x1000")
        selected_window.resizable(True, True)

        title_label = tk.Label(selected_window, text="You said you struggle with", font=("Helvetica", 16, "bold"))
        title_label.pack(pady=10)

        scrollable_frame = tk.Frame(selected_window)
        scrollable_frame.pack(fill="both", expand=True)

        canvas = tk.Canvas(scrollable_frame)
        scrollbar = tk.Scrollbar(scrollable_frame, orient="vertical", command=canvas.yview)
        frame = tk.Frame(canvas)

        frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        row = 0
        column = 0
        for option, image_file in zip(self.options, self.image_files):
            if option in selected_texts:
                image = Image.open(image_file)
                image = image.resize((150, 200), Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(image)
                button = tk.Button(
                    frame,
                    image=photo,
                    text=option,
                    compound="top",
                    wraplength=200,
                    justify=tk.CENTER,
                    padx=10,
                    pady=10,
                    font=("Arial", 10),
                    bg="light blue"
                )
                button.image = photo  # keep a reference to prevent garbage collection
                button.grid(row=row, column=column, padx=10, pady=10)

                if column == 0:
                    column = 1
                else:
                    column = 0
                    row += 1

        # Add the image from the uploaded file
        image_path = "/mnt/data/image.png"
        image = Image.open(image_path)
        image = image.resize((450, 600), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        image_label = tk.Label(selected_window, image=photo)
        image_label.image = photo  # keep a reference to prevent garbage collection
        image_label.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = ADHDApp(root)
    root.mainloop()
