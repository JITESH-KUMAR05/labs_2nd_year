import tkinter as tk

root = tk.Tk()
root.title("JK's Calculator")
root.geometry("500x500")

# this is a fully functional calculator with all the numbers on the botton in a grid of 3x3 and other options like clear, delete, and equals with all oprations like +,-,*,/ and also a decimal point
# making calculator
def add():
    a = float(entry1.get())
    b = float(entry2.get())
    result = a + b
    label_result.config(text="Result: " + str(result))

def subtract():
    a = float(entry1.get())
    b = float(entry2.get())
    result = a - b
    label_result.config(text="Result: " + str(result))

def multiply():
    a = float(entry1.get())
    b = float(entry2.get())
    result = a * b
    label_result.config(text="Result: " + str(result))

def divide():
    a = float(entry1.get())
    b = float(entry2.get())
    result = a / b
    label_result.config(text="Result: " + str(result))

def clear():
    entry.delete(0, tk.END)
    label_result.config(text="Result: ")

def delete():
    entry.delete(0, tk.END)

def decimal():
    entry.insert(tk.END, ".")

def equals():
    # this function should show the result on the basis of the operation selected and numbers entered in the entry boxes
    if operation.get() == "+":
        add()
    elif operation.get() == "-":
        subtract()
    elif operation.get() == "*":
        multiply()
    elif operation.get() == "/":
        divide()
    else:
        label_result.config(text="Invalid operation")
    

label1 = tk.Label(root,text="Enter first number")
label1.pack()

entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root,text="Enter second number")
label2 = tk.Label(root,text="Enter second number")
label2.pack()

entry2 = tk.Entry(root)
entry2.pack()

label3 = tk.Label(root,text="Select operation")
label3.pack()

operation = tk.StringVar(root)
options = tk.OptionMenu(root, operation, "+", "-", "*", "/")
options.pack()

# Create a frame for the buttons
button_frame = tk.Frame(root)
button_frame.pack(fill=tk.BOTH, expand=True)

# Configure the grid layout to have 4 columns and make them expand equally
for i in range(4):
    button_frame.columnconfigure(i, weight=1)
    button_frame.rowconfigure(i, weight=1)

# Add buttons to the frame in a 4x4 grid layout
button1 = tk.Button(button_frame, text="Add", command=add)
button1.grid(row=0, column=0)

button2 = tk.Button(button_frame, text="Subtract", command=subtract)
button2.grid(row=0, column=1)

button3 = tk.Button(button_frame, text="Multiply", command=multiply)
button3.grid(row=0, column=2)

button4 = tk.Button(button_frame, text="Divide", command=divide)
button4.grid(row=0, column=3)

button5 = tk.Button(button_frame, text="Clear", command=clear)
button5.grid(row=1, column=0)

button6 = tk.Button(button_frame, text="Delete", command=delete)
button6.grid(row=1, column=1)

button7 = tk.Button(button_frame, text="Decimal", command=decimal)
button7.grid(row=1, column=2)

button8 = tk.Button(button_frame, text="Equals", command=equals)
button8.grid(row=1, column=3)

label_result = tk.Label(root,text="Result: ")
label_result.pack()

root.mainloop()
