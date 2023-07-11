import tkinter as tk
from tkinter import *
from tkinter import ttk
from customtkinter import *
class EndLayout:
    def __init__(self, root):
        self.root = root
        self.frame = None

    def create_layout(self ,money):      
        style = ttk.Style()
        # Configure the style for the frame
        style.configure("CustomFrame.TFrame", background="#fff")
        self.frame = ttk.Frame(self.root,padding=40,style="CustomFrame.TFrame")
        self.frame.pack()
        # Create and place the "Congrats" label
        self.congrats_label = ttk.Label(self.frame, text="Congratulations!!!", font=("Arial", 18),background="#fff")
        self.congrats_label.pack(pady=10)

        # Create and place the "You won" label
        self.won_label = ttk.Label(self.frame, text="You won", font=("Arial", 18),background="#fff")
        self.won_label.pack(pady=10)

        # Create and place the label with the text "10000"
        self.score_label = ttk.Label(self.frame, text=f"{money}", font=("Arial", 48),background="#fff")
        self.score_label.pack(pady=10)

        # Create and place the exit button
        self.exit_button = CTkButton(self.frame, text="Exit", command=self.root.destroy)
        self.exit_button.pack(pady=10)
    
    def destroy_layout(self):
        if self.frame:
            self.frame.destroy()
            self.frame = None
 