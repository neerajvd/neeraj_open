import tkinter as tk
from components import *
import queslib
import random
import startLayout
from startLayout import *

global highlight_color
highlight_color = "#FDD032"

# Shuffle questions and trim to 15 questions only
question_list = queslib.question_list
random.shuffle(question_list)
question_list = question_list[:15]
 
class QuestionLayout:
    def __init__(self, root):
        self.root = root
        self.root.config(padx=50, pady=50)
        self.root.columnconfigure(0, weight=3, uniform="a")
        self.root.columnconfigure(1, weight=1, uniform="a")
        self.root.rowconfigure(0, weight=1, uniform="a")
        self.frame1 = None
        self.frame2 = None
        self.levelNo = None
        self.quesLabel = None
        self.choice = None
        self.rad_frame = None
        self.rad = None
        self.lockBtn = None
        self.quitBtn = None
        self.heading = None
        self.labels = []
        self.index = 0

    def create_layout(self):
        # Create the first frame
        self.frame1 = tk.Frame(self.root, background="#fff")
        self.frame1.grid(
            row=0,
            column=0,
            sticky="nswe",
            padx=(0, 20),
        )
        self.frame1.columnconfigure(
            (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), weight=4, uniform="a"
        )
        self.frame1.columnconfigure((0, 16), weight=1, uniform="a")
        self.frame1.rowconfigure(
            (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16), weight=3, uniform="a"
        )
        self.frame1.rowconfigure((0, 16), weight=1, uniform="a")
        # Create the second frame
        self.frame2 = tk.Frame(self.root, background="#fff")
        self.frame2.grid(row=0, column=1, sticky="nswe")

        # Label in first frame
        self.levelNo = Label(
            self.frame1,
            text="Level",
            font=("Arial", 14, "bold"),
            borderwidth=1,
            relief=GROOVE,
        )
        
        self.levelNo.grid(
            row=2, rowspan=1, column=2, columnspan=2, sticky="nsew", ipadx=10, ipady=5
        ) 
        self.quesLabel = tk.Label(
            self.frame1,
            text="What is the capital of France?",
            font=("Arial", 20, "bold"),
            borderwidth=1,
            relief=GROOVE,
        )
        self.quesLabel.grid(
            row=4,
            rowspan=3,
            column=2,
            columnspan=8,
            sticky="nsew",
            pady=(0, 10),
        )

        # # create frame for radio buttons
        self.rad = RadioButtonManager(self.frame1)
        self.rad.create_radio_button([])

        # # Buttons in first frame
        self.lockBtn = CTkButton(
            self.frame1, text="Lock", font=("Arial", 18), command=self.lock_ans
        )
        self.lockBtn.grid(row=13, rowspan=1, column=2, columnspan=8, sticky="nsew")
 
        self.quitBtn = CTkButton(
            self.frame1, text="Quit", font=("Arial", 12), command=self.game_lost
        )
        self.quitBtn.grid(row=15, column=9, columnspan=1)

        # # Heading in second frame
        self.heading = tk.Label(
            self.frame2, text="Levels", font=("Arial", 24, "bold"), background="#fff"
        )
        self.heading.pack(pady=(40, 10))

        # # List of labels in second frame
        for i, money in enumerate(queslib.money_levels):
            label = tk.Label(
                self.frame2,
                text=f"{money}",
                font=("Arial", 16),
                pady=4,
                background="#fff",
            )
            label.pack(fill="x")
            self.labels.append(label)
            if i == len(queslib.money_levels) - 1:
                label.config(background=highlight_color)

    # to load new text in each element
    def load_ques(self, index):
        if index > 0:
            startLayout.play_sound("correct", 1)
        startLayout.play_sound("suspense", 1)
        self.levelNo.config(text=f"Level : {self.index+1}")
        question = question_list[index]["question"]
        optionsList = question_list[index]["options"]
        random.shuffle(optionsList)
        self.quesLabel.config(text=insert_newlines(question))
        self.rad.create_radio_button(optionsList)

    def lock_ans(self):
        startLayout.play_sound("suspense", 3)
        self.choice = self.rad.getValue()
        if question_list[self.index]["answer"] == self.choice:
            # for last(15th) question
            if self.index == len(question_list) - 1:
                print("index is", self.index)
                self.destroy_layout()
                startLayout.end_game(self.index)
                print("index is", self.index)
                return self.index
            # for other questions
            self.index += 1
            self.load_ques(self.index)
            # remove highlight from all(previous) level
            for i in range(len(self.labels)):
                self.labels[i].config(background="#fff")
            # highlight current level
            self.labels[len(question_list) - self.index - 1].config(
                background=highlight_color
            )
        else:
            self.game_lost()

    def game_lost(self):
        startLayout.play_sound("hooter", 1)
        self.destroy_layout()
        startLayout.end_game(self.index)

    def destroy_layout(self):
        self.frame1.destroy()
        self.frame2.destroy()
