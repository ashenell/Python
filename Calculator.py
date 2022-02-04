from ast import While
from cgitb import text
from cmath import exp
from tkinter import *
from tkinter.tix import Tree
from turtle import st, title, update
from venv import create


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
        
        self.total_result = '' #Total number
        self.current_result = '' #Current number bigger
        self.display_frame = self.create_display_frame()
        self.total_lable, self.current_lable = self.create_display_labels()
        
        #Numbrs lists with location
        self.digits = {
            7:(1,1), 8:(1,2), 9:(1,3),
            4:(2,1), 5:(2,2), 6:(2,3),
            1:(3,1), 2:(3,2), 3:(3,3),
            0:(4,1), '.':(4,2) 
        }

        #Buttons +,-,*,/
        self.operations ={'/':'\u00F7', '*':'\u00D7', '-':'-', '+':'+'}
        

        
        self.buttons_frame = self.create_button_frame()
        
        #Expand row and columns 
        for x in range(1,5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)
   
        self.create_digit_buttons() #Creates numbers buttons
        self.create_operator_buttons() # + - * /
        self.create_special_buttons() #Creates all 4 special buttons
        self.bind_keys() #Keyboard numbers and operations

#To use keyboard functions

    def clear_last(self, event):
        self.current_result = self.current_result[:-1]
        self.update_current_label()
          
    def bind_keys(self):
        self.window.bind('<Return>', lambda event:self.evaluate())
        self.window.bind('<Escape>', lambda event:self.clear())
        self.window.bind('<Delete>', lambda event:self.clear())
        self.window.bind('<BackSpace>', self.clear_last)
        
        for key in self.digits:
            self.window.bind(key, lambda event, digit=key: self.add_to_expression(digit))
        for key in self.operations:
            self.window.bind(key, lambda event, operator=key: self.append_operator(operator))
    
        
    def create_button_frame(self):
        frame = Frame(self.window)
        frame.pack(expand=True, fill=BOTH)
        return frame
#Call out buttons    
    def create_special_buttons(self): #Special buttons

        self.create_clear_button() #Clear all
        self.create_square_button() #Square buton
        self.create_sqrt_button() 
        self.create_equal_button() # Equal button
        
#Buttons and functions for math

    def clear(self):
        self.current_result = ''
        self.total_result = ''
        self.update_current_label()
        self.update_total_label()

    def create_clear_button(self):
        button =Button(self.buttons_frame, text='C', bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAUL_FONT_STYLE, 
                       command=self.clear, borderwidth=0)
        button.grid(row=0, column=1, sticky=NSEW)
    
    def square(self):
        self.current_result = str(eval(f'{self.current_result}**2'))
        self.update_current_label()
    
    def create_square_button(self):
        button = Button(self.buttons_frame, text='x\u00b2', bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAUL_FONT_STYLE, 
                        command=self.square, borderwidth=0)
        button.grid(row=0, column=2, sticky=NSEW)
    
    def sqrt(self):
        self.current_result = str(eval(f'{self.current_result}**0.5'))
        self.update_current_label()
    
    def create_sqrt_button(self):
        button = Button(self.buttons_frame, text='\u221ax', bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAUL_FONT_STYLE, 
                        command=self.sqrt, borderwidth=0)
        button.grid(row=0, column=3, sticky=NSEW)

#Calculate and update also handling error
    
    def evaluate(self):
        self.total_result += self.current_result
        self.update_total_label()
        try:
            self.current_result = str(eval(self.total_result))
            self.total_result = ''
        except Exception as e:
            self.current_result = 'Error'

        finally:
            self.update_current_label()
    
    def create_equal_button(self):
        button = Button(self.buttons_frame, text='=', bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAUL_FONT_STYLE, command=self.evaluate)
        button.grid(row=4, column=3, columnspan=2, sticky=NSEW)

#Function for buttons    
    def add_to_expression(self, value):
        if self.current_result == 'Error':
            self.clear() 
        if value == '.':
            if self.current_result.find('.') == -1:
                self.current_result += str(value)
        else:
            self.current_result += str(value)
        self.update_current_label()
    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = Button(self.buttons_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE, 
                            command=lambda x=digit: self.add_to_expression(x), borderwidth=0)
            button.grid(row=grid_value[0], column=grid_value[1], sticky=NSEW)
#Function fot buttons to map in right place  

    def append_operator(self, operator):
        self.current_result += operator
        self.total_result += self.current_result
        self.current_result = ''
        self.update_current_label()
        self.update_total_label()
  
    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = Button(self.buttons_frame, text=symbol, bg=OFF_WHITE, fg=LABEL_COLOR,font=DEFAUL_FONT_STYLE, 
                            command=lambda x=operator: self.append_operator(x), borderwidth=0)
            button.grid(row=i, column=4, sticky=NSEW)
            i += 1
    
        
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
        
    
    def update_current_label(self):
        self.current_lable.config(text=self.current_result[:11])
    
    
    def update_total_label(self):
        expression = self.total_result
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.total_lable.config(text=expression)
            
    def run(self):
        self.window.mainloop()
   
