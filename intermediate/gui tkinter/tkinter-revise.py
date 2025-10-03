import tkinter

window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

my_label = tkinter.Label(text='I am a Label', font=("Arial",24,"bold"))
# my_label.pack()
# my_label.place(x=150, y=200)
my_label.grid(column=0, row=0)

# Padding
my_label.config(padx=50, pady=50)

# my_label.pack(side="left")
# my_label['text'] = "Something New"
# my_label.config(text="Something New")

# Button
def clicked():
    print(entry.get())
    # print(text.get("1.0", tkinter.END))
    # my_label.config(text=entry.get())

button = tkinter.Button(text="Click me", command=clicked)
# button.pack()
button.grid(column=1, row=1)

# Input
entry = tkinter.Entry(width=30)
entry.insert(tkinter.END, string="something to do with python")
# entry.pack() 
# # if grid is used then we cannot use pack
entry.grid(column=2, row=2)

# # Text
# text = tkinter.Text(height=5, width=30)
# text.insert(tkinter.END,chars="Something")
# text.pack()

# # SpinBox
# def spinbox_used():
#     print(spinbox.get())

# spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()

# # Scale
# def scale_used(value):
#     print(value)

# scale = tkinter.Scale(from_=0, to=10, width=10, command=scale_used)
# scale.pack()

# # Checkbox
# def checkbox_used():
#     print(checked_state.get())

# checked_state = tkinter.IntVar()
# checkbox = tkinter.Checkbutton(text="Is On?", variable=checked_state, command=checkbox_used)
# checkbox.pack()

# # Radio button
# def radio_used():
#     print(radio_state.get())

# radio_state = tkinter.IntVar()

# radio_btn1 = tkinter.Radiobutton(text="Option 1", value=1, variable=radio_state, command=radio_used)

# radio_btn2 = tkinter.Radiobutton(text="Option 2", value=2, variable=radio_state, command=radio_used)

# radio_btn3 = tkinter.Radiobutton(text="Option 3", value=3, variable=radio_state, command=radio_used)

# radio_btn1.pack()
# radio_btn2.pack()
# radio_btn3.pack()

# # Listbox
# def listbox_used(event):
#     print(listbox.get(listbox.curselection()))

# listbox = tkinter.Listbox(height=4)
# fruits = ['Apple', 'Orange', 'Mango', 'Lichi']
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()
window.mainloop()