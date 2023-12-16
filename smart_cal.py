# Import necessary libraries
from tkinter import *
import math


# Function to handle button clicks and update display

def click(value):
    """
        This function takes a button value as input and performs the corresponding action:
        - Update the display with numbers and operators.
        - Evaluate expressions and display the result.
        - Handle special buttons like C, CE, and =.
        - Catch and ignore syntax errors silently.
        """

    ex = entryField.get()   # Get the current expression in the entry field
    answer = ''   # Initialize an empty string to store the result

    try:
        # Handle different button functionalities
                if value=='C':  # Delete the last character from the expression
                    ex=ex[0:len(ex)-1]
                    entryField.delete(0,END)
                    entryField.insert(0,ex)  # Update the entry field with the modified expression
                    return

#use evalution funtion to calculate a float to string and string to a float
                elif value == 'CE':
                    entryField.delete(0,END)    # Clear the entire entry field

                elif value == '√':  # Display the value of square root
                    answer = math.sqrt(eval(ex))

                elif value == 'π':  # Display the value of pi
                    answer = math.pi

                # Trigonometric functions with optional angle unit conversion
                elif value == 'cosθ':
                    answer = math.cos(math.radians(eval(ex)))  # Calculate cosine with radians

                elif value == 'tanθ':
                    answer = math.cos(math.radians(eval(ex)))   # Calculate tangent with radians

                elif value == 'sinθ':
                    answer = math.cos(math.radians(eval(ex)))       # Calculate sine with radians

                elif value == '2π':
                    answer = 2 * math.pi  # Display double the value of pi

                # Additional mathematical functions and notations
                elif value == 'cosh':
                    answer = math.cosh(eval(ex))   # Calculate hyperbolic cosine

                elif value == 'tanh':
                    answer = math.tanh(eval(ex))   # Calculate hyperbolic tangent

                elif value == 'sinh':
                    answer = math.sinh(eval(ex))    # Calculate hyperbolic sine

                elif value == chr(8731):    # Unicode character for cube root
                    answer = eval(ex) ** (1 / 3)   # Calculate cube root

                elif value == "x\u02bB":
                    entryField.insert(END,'**')  # Insert the double exponent symbol
                    return

                #more mathematical calculations
                elif value == "x\u00B3":   # Calculate cube
                    answer = eval(ex) ** 3

                elif value == 'x\u00B2':
                    answer = eval(ex) ** 2   # Calculate square

                elif value == 'in':
                    answer = math.log2(eval(ex))  # Calculate base-2 logarithm

                elif value == 'deg':
                    answer = math.degrees(eval(ex))  # Convert radians to degree

                elif value == 'rad':
                    answer = math.radians(eval(ex))  # Convert degrees to radians

                elif value == 'e':
                    answer = math.e  # Display the value of Euler's number

                elif value == 'log₁₀':
                    answer = math.log10(eval(ex))  # Calculate base-10 logarithm


                elif value == 'x!':
                    answer = math.factorial(eval(ex))  # Calculate factorial


                elif value == chr(247):
                    entryField.insert(END,"/")  # Insert the division symbol

                elif value == '=':
                    answer = eval(ex)  # Evaluate the entire expression


                else :
                    entryField.insert(END,value)    # Simply append the entered character
                    return


        # Update the entry field with the calculated result
                entryField.delete(0, END)
                entryField.insert(0, answer)
    except SyntaxError:
       pass   # To Ignore syntax errors silently

# Initialize the Tkinter window and graphical user interface
gui = Tk()
gui.title('SMART CALCULATOR AND VOICE CALCULATOR')  #To Set the window title
gui.config(bg='teal') # To the background color us the bg function
gui.geometry('680x486+100+100') # to determine the  geometry (width and height ) of the tkinter


# Add logo image and microphone button

logoImage = PhotoImage(file='logo.png')
logoLabel = Label(gui, image=logoImage, bg='teal')
logoLabel.grid(row=0, column=7)

#add microphone button

micImage = PhotoImage(file='microphone.png')
micButton = Button(gui, image=micImage,  bd=0, bg='teal')
micButton.grid(row=0, column=0)

#entry field properties
entryField = Entry(gui, font=('arial', 20, 'bold'), bg='teal', fg='white', bd=10, relief=SUNKEN, width=30)
entryField.grid(row=0, column=0, columnspan=8)
#create a list of functionality

button_text_list = ["C", "CE", "√","+", " π", "cosθ", "tanθ", "sinθ",
                    "1", "2", "3", "-","2π", "sin", "cosh", "tanh",
                    "4", "5", "6", "*", chr(8731), "x\u02bB", "x\u00B3", "x\u00B2",
                    "7", "8", "9", "/",    "ln", "deg", "rad", "e",
                    "0", ".", "%", "=",    "log₁₀", "(", ")", "x!"]
rowvalue = 1
columnvalue = 0
for i in button_text_list:

    button = Button(gui, width=5, height=2, bd=2, relief=SUNKEN, text=i, bg='teal', fg='white',
                    font=('arial', 18, 'bold'), activebackground='white', command=lambda button=i: click(button))
    button.grid(row=rowvalue, column=columnvalue, pady=1)
    columnvalue += 1
    if columnvalue > 7:
        rowvalue += 1
        columnvalue = 0
#gui.mainloop() It keeps the event loop running, listens for user actions, updates the UI, and ensures smooth responsiveness
gui.mainloop()
