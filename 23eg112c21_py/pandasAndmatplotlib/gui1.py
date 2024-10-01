import tkinter as tk

root = tk.Tk()
root.title("My first gui")
root.geometry("400x400")

# making calculator
def add():
    a = int(entry1.get())
    b = int(entry2.get())
    result = a+b
    label_result.config(text="Result: "+str(result))

label1 = tk.Label(root,text="Enter first number")
label1.pack()

entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root,text="Enter second number")
label2.pack()

entry2 = tk.Entry(root)
entry2.pack()

button = tk.Button(root,text="Add",command=add)
button.pack()

label_result = tk.Label(root,text="Result: ")
label_result.pack()



root.mainloop()