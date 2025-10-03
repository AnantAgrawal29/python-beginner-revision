from tkinter import *
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

entry = Entry(width=10)
entry.grid(column=1, row=0)

miles = Label(text="Miles")
miles.grid(column=2, row=0)

equal = Label(text="is equal to")
equal.grid(column=0, row=1)

convert = Label(text=0)
convert.grid(column=1, row=1)

km = Label(text="Km")
km.grid(column=2, row=1)

def converter():
    miles = entry.get()
    kms = int(int(miles)*1.609344)
    convert.config(text=kms)

calculate = Button(text="Calculate", command=converter)
calculate.grid(row=2, column=1)

window.mainloop()