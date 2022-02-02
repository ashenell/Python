from cmath import exp
from tkinter import *
from tkinter.tix import Tree
from turtle import title


LARGE_FONT_STYLE = ('Arial', 40, 'bold')
SMALL_FONT_STYLE = ('Arial', 16)
DIGITS_FONT_STYLE = ('Arial', 24, 'bold')
DEFAUL_FONT_STYLE = ('Arial', 20)

OFF_WHITE = '#F8FAFF'
WHITE = '#FFFFFF'
LIGHT_BLUE = '#CCEDFF'
LIGHT_GRAY = '#F5F5F5'
LABEL_COLOR = '#25265E'

class Calculator:
    'Class named Clalculator'
    def __init__(self):
        self.window = Tk()
        self.window.geometry('375x667') #Resulution for a window
        self.window.resizable(False, False) #Resulution size is not allowed to change
        self.window.title('Calculator')
        
        self.total_result = '0' #Whole number bigger
        self.current_result = '0' #Current number smaller
        self.display_frame = self.create_display_frame()
        self.total_lable, self.current_lable = self.create_display_labels()
        
        #Numbrs lists with location
        self.digits = {
            7:(1,1), 8:(1,2), 9:(1,3),
            4:(2,1), 5:(2,2), 6:(2,3),
            1:(3,1), 2:(3,2), 3:(3,3),
            0:(4,1), '.':(4,2) 
        }
    
    def create_button_frame(self):
        frame = Frame(self.window)
        frame.pack(expand=True, fill=BOTH)
        return frame
        
    def create_display_frame(self):
        frame = Frame(self.window, height=221,bg=LIGHT_GRAY)
        frame.pack(expand=True, fill=BOTH)
        return frame

    def create_display_labels(self):
        total_label = Label(self.display_frame, text=self.total_result, anchor=E, bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill=BOTH)
        
        current_label = Label(self.display_frame, text=self.current_result, anchor=E, bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)
        current_label.pack(expand=True, fill=BOTH)
        return total_label, current_label
        
        
    def run(self):
        self.window.mainloop()