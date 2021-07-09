
from tkinter import *

# The parser module provides an interface to python's internal parser
# https://docs.python.org/3.0/library/parser.html
import parser

# creating a window for our calculator app
window = Tk()
window.title('Simple Calculator')

# adding the input field where our digits & operations will be dispalyed
display = Entry(window)
display.grid(row = 1, columnspan = 6, sticky = W + E)

# adding buttons in calculator the graphical form of digits & operations 
Button(window, text = "MC").grid(row = 2, column = 0, sticky = W + E)
Button(window, text = "MR").grid(row = 2, column = 1, sticky = W + E)
Button(window, text = "M+").grid(row = 2, column = 2, sticky = W + E)
Button(window, text = "M-").grid(row = 2, column = 3, sticky = W + E)



Button(window, text = "%").grid(row = 3, column = 0, sticky = W + E)
Button(window, text = "CE").grid(row = 3, column = 1, sticky = W + E)
Button(window, text = "C").grid(row = 3, column = 2, sticky = W + E)
Button(window, text = "<-").grid(row = 3, column = 3, sticky = W + E)


Button(window, text = "1/x").grid(row = 4, column = 0, sticky = W + E)
Button(window, text = "x^2").grid(row = 4, column = 1, sticky = W + E)
Button(window, text = "√x").grid(row = 4, column = 2, sticky = W + E)
Button(window, text = "÷").grid(row = 4, column = 3, sticky = W + E)



Button(window, text = "7").grid(row = 5, column = 0, sticky = W + E)
Button(window, text = "8").grid(row = 5, column = 1, sticky = W + E)
Button(window, text = "9").grid(row = 5, column = 2, sticky = W + E)
Button(window, text = "×").grid(row = 5, column = 3, sticky = W + E)


Button(window, text = "4").grid(row = 6, column = 0, sticky = W + E)
Button(window, text = "5").grid(row = 6, column = 1, sticky = W + E)
Button(window, text = "6").grid(row = 6, column = 2, sticky = W + E)
Button(window, text = "-").grid(row = 6, column = 3, sticky = W + E)


Button(window, text = "1").grid(row = 7, column = 0, sticky = W + E)
Button(window, text = "2").grid(row = 7, column = 1, sticky = W + E)
Button(window, text = "3").grid(row = 7, column = 2, sticky = W + E)
Button(window, text = "+").grid(row = 7, column = 3, sticky = W + E)


Button(window, text = "+/-").grid(row = 8, column = 0, sticky = W + E)
Button(window, text = "0").grid(row = 8, column = 1, sticky = W + E)
Button(window, text = ".").grid(row = 8, column = 2, sticky = W + E)
Button(window, text = "=").grid(row = 8, column = 3, sticky = W + E)



# enter the mainloop
window.mainloop()














# Button(window, text = "").grid(row = , column = 0)
# Button(window, text = "").grid(row = , column = 1)
# Button(window, text = "").grid(row = , column = 2)
# Button(window, text = "").grid(row = , column = 3)