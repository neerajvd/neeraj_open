from tkinter import *
import customtkinter as ctk
from customtkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import random
from components import *
from queslib import money_levels, question_list
from components import *
from questionLayout import QuestionLayout
from endLayout import EndLayout
from pygame import mixer
import pygame
import queslib  

global bgColor, purple_color, layout
layout = None

bgColor = "#fff"
purple_color = ""
# Shuffle the questions
random.shuffle(question_list)

# playsound function

def play_sound(sound,query):
    mixer.init()
    path=get_song_path(sound)
    mixer.music.load(path)
    
    if query == 0:
        mixer.music.pause()	
    elif query ==1:
        mixer.music.play()
    elif query == 3:
        mixer.music.stop()
    elif query == 4:
        mixer.music.unpause()
    if sound=="hooter":
        pygame.time.wait(1550)
    if sound=="correct":
        pygame.time.wait(1350)
    
def get_song_path(sound):
    for song in queslib.song_list:
        if song["sound"] == sound:
            return song["path"]
    return None  # Return None if the sound is not found in the list

class StartLayout:
    def __init__(self, root):
        self.root = root
        self.frame = None
        self.image_label = None
        self.frame_image_label = None
        self.label1 = None
        self.label2 = None
        self.entry = None
        self.button = None
        self.name_value = None
        self.frame_rules = None
        self.rules_labels=[]

    def create_layout(self):
        play_sound("intro",1)
        # Creating the main image
        main_image_path = "assets/bacchan.png"
        main_image = Image.open(main_image_path)
        height = self.root.winfo_screenheight() - 120
        width = int(0.37 * height)
        main_image = main_image.resize((width, height))
        main_image_tk = ImageTk.PhotoImage(main_image)
        self.image_label = Label(self.root, image=main_image_tk, background="#f0f0f0")
        self.image_label.image = main_image_tk
        self.image_label.pack(side=LEFT, fill=Y, expand=TRUE, pady=20, padx=(100, 0))

        # Creating the frame
        style = ttk.Style()
        # Configure the style for the frame
        style.configure("CustomFrame.TFrame", background="#fff")

        self.frame = ttk.Frame(self.root, padding=20, style="CustomFrame.TFrame")
        self.frame.pack(side=LEFT, expand=TRUE, pady=10, padx=10)

        self.frame_rules = ttk.Frame(self.root, padding=20, style="CustomFrame.TFrame")
        self.frame_rules.pack(side=LEFT, expand=TRUE,fill=Y, pady=100, padx=(0, 100))

        # Creating the frame image
        frame_image_path = "assets/kbclogo.png"
        frame_image = Image.open(frame_image_path)
        frame_image = frame_image.resize((300, 300))
        frame_image_tk = ImageTk.PhotoImage(frame_image)
        self.frame_image_label = Label(
            self.frame, image=frame_image_tk, background=bgColor
        )
        self.frame_image_label.image = frame_image_tk
        self.frame_image_label.pack(pady=(0, 50))

        # Creating labels, entry, and button inside the frame
        self.label1 = ttk.Label(
            self.frame,
            text="WELCOME TO",
            font=("Comic Sans", 20),
            foreground="#000",
            background=bgColor,
        )
        self.label1.pack(pady=(10, 0), anchor=CENTER)

        self.label2 = ttk.Label(
            self.frame,
            text="KBC",
            font=("Comic Sans", 64, "bold"),
            foreground="#000",
            background=bgColor,
        )
        self.label2.pack(pady=(0, 0), anchor=CENTER)

        self.button = CTkButton(
            self.frame,
            text="Let's Play !!!",
            font=("Arial", 18),
            command=lambda: start_btn_clicked(layout),
            
        )
        self.button.pack(fill=X, padx=5, pady=5)
# Rules frames 
        self.title_rules = Label(
            self.frame_rules,
            text="Rules:",
            font=("Comic Sans", 20,"bold"),
            foreground="#000",
            background=bgColor,
        ).pack(anchor="w",pady=(0,15))
        for i,rule in enumerate(queslib.rules_list):
            rule_item= Label(
                self.frame_rules,
                text=f"{i+1}. {rule}",
                font=("Roboto", 14),
                foreground="#000",
                background=bgColor,
                justify="left"
            ).pack(anchor="w",padx=10,pady=3)
            self.rules_labels.append(rule_item)

    # to destory the startscreen
    def destory_layout(self):
        self.frame.destroy()
        self.image_label.destroy()
        self.frame_image_label.destroy()
        self.label1.destroy()
        self.label2.destroy()
        self.entry = None
        self.button.destroy()
        self.frame_rules.destroy()

# Processes after start btn clicked
def start_btn_clicked(parent):
    play_sound("intro",3)
    parent.destory_layout()
    layout = QuestionLayout(root)
    layout.create_layout()
    layout.load_ques(0)
    


def end_game(index):
    play_sound("congrats",1)
    # warning line below
    if index == len(money_levels) - 1:
        money = money_levels[0]
    elif index > 0:
        money = money_levels[len(money_levels) - index]
    else:
        money = 0
        play_sound("congrats",3)
    layout = EndLayout(root)
    layout.create_layout(money)
    print("game end, You won", money)


root = Tk()
root.iconbitmap("assets/icon.ico")
root.title("KBC Quiz Game")
root.state("zoomed")

layout = StartLayout(root)
layout.create_layout()

root.mainloop()
