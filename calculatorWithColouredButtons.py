from tkinter import *
import parser

root = Tk()
root.title('Simple Calculator')


#adding the input field
display = Entry(root)
display.grid(row=1, columnspan=100, sticky=W + E)

#adding button in the calculator

Button(root, text="1",bg="black",fg="white").grid(row=2, column=0, sticky=W + E)
Button(root, text="2",bg="black",fg="white").grid(row=2, column=1, sticky=W + E)
Button(root, text="3",bg="black",fg="white").grid(row=2, column=2, sticky=W + E)

Button(root, text="4",bg="black",fg="white").grid(row=3, column=0, sticky=W + E)
Button(root, text="5",bg="black",fg="white").grid(row=3, column=1, sticky=W + E)
Button(root, text="6",bg="black",fg="white").grid(row=3, column=2, sticky=W + E)

Button(root, text="7",bg="black",fg="white").grid(row=4, column=0, sticky=W + E)
Button(root, text="8",bg="black",fg="white").grid(row=4, column=1, sticky=W + E)
Button(root, text="9",bg="black",fg="white").grid(row=4, column=2, sticky=W + E)

#adding other buttons to the calculator
Button(root, text="AC",bg="yellow",fg="red").grid(row=5, column=0, sticky=W + E)
Button(root, text="0",bg="yellow",fg="red").grid(row=5, column=1, sticky=W + E)
Button(root, text="=",bg="yellow",fg="red").grid(row=5, column=2, sticky=W + E)

Button(root, text="+",bg="green",fg="black").grid(row=2, column=3, sticky=W + E)
Button(root, text="-",bg="green",fg="black").grid(row=3, column=3, sticky=W + E)
Button(root, text="*",bg="green",fg="black").grid(row=4, column=3, sticky=W + E)
Button(root, text="/",bg="green",fg="black").grid(row=5, column=3, sticky=W + E)

#adding new operations
Button(root, text="pi",bg="black",fg="white").grid(row=2, column=4, sticky=W + E)
Button(root, text="%",bg="black",fg="white").grid(row=3, column=4, sticky=W + E)
Button(root, text="(",bg="black",fg="white").grid(row=4, column=4, sticky=W + E)
Button(root, text="exp",bg="black",fg="white").grid(row=5, column=4, sticky=W + E)

Button(root, text="<-",bg="pink",fg="white").grid(row=2, column=5, sticky=W + E)
Button(root, text="x!",bg="pink",fg="white").grid(row=3, column=5, sticky=W + E)
Button(root, text=")",bg="pink",fg="white").grid(row=4, column=5, sticky=W + E)
Button(root, text="^2",bg="pink",fg="white").grid(row=5, column=5, sticky=W + E)

root.mainloop()
