from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk
 
 
# Custom Radio buttons
class RadioButtonManager:
    def __init__(self, root):
        self.root = root
        self.radios = []
        self.variable = StringVar()
        self.variable.set(-1)

    # pass text_list and variable to get value
    def create_radio_button(self, text_list):

        for i,t in enumerate(text_list):
            radio = CTkRadioButton(
                self.root,
                text=t,
                variable=self.variable,
                value=t,
                # command=self.getValue,
                command=self.getValue,
                
                text_color="#000",
                 font=("Roboto",18, "bold"),
            ) 
            radio.grid(row=[i+7],column=2, columnspan=8, sticky="nsew")
            self.radios.append(radio)

    def getValue(self):
        # print(self.variable.get())
        return self.variable.get()
 
    def destroy_radio_buttons(self):
        for radio in self.radios:
            radio.destroy()
        self.radios = []
        self.variable = None

# new lines in questions
def insert_newlines(string):
    lines = []
    while len(string) > 48:
        if string[47] != " ":
            index = string[:48].rfind(" ")
            if index == -1:  # No space found
                index = 47
        else:
            index = 47
        lines.append(string[: index + 1])
        string = string[index + 1 :]
    lines.append(string)
    return "\n".join(lines)

