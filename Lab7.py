import tkinter as tk
import random

# Thai consonants with their names
thai_consonants = [
    ("ก", "กอ ไก่ (gor gai)"),
    ("ข", "ขอ ไข่ (kho khai)"),
    ("ค", "คอ ควาย (kho khwai)"),
    ("ง", "งอ งู (ngo ngu)"),
    ("จ", "จอ จาน (jor jan)"),
]


class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Thai Consonant Flashcards")
        self.root.geometry("400x300")

        self.current_card = {}

        self.card_frame = tk.Frame(self.root, width=300, height=200, bg="white")
        self.card_frame.pack(pady=50)

        self.card_label = tk.Label(self.card_frame, text="", font=("Arial", 48), bg="white")
        self.card_label.pack(expand=True)

        self.card_frame.bind("<Button-1>", self.flip_card)
        self.card_label.bind("<Button-1>", self.flip_card)

        self.next_button = tk.Button(self.root, text="Next", command=self.next_card)
        self.next_button.pack()

        self.next_card()

    def next_card(self):
        self.current_card = random.choice(thai_consonants)
        self.card_label.config(text=self.current_card[0])
        self.is_flipped = False

    def flip_card(self, event):
        if not self.is_flipped:
            self.card_label.config(text=self.current_card[1])
            self.is_flipped = True
        else:
            self.card_label.config(text=self.current_card[0])
            self.is_flipped = False


if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()
