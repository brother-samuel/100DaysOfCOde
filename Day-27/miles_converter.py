from tkinter import *


window = Tk()
window.title("Mile to km converter")
window.minsize(300,200)
window.config(padx=40, pady=40)

def calculate():
    kilometers = float(input.get()) * 1.609344
    result.config(text=f"{kilometers:.2f}")
    input.delete(0, END)


#input
input = Entry()
input.grid(column=1, row=0)
input.focus()
input.bind('<Return>', lambda event:calculate())

# miles label
miles = Label(text="Miles")
miles.grid(column=2, row=0)


# equal label
equal = Label(text="is equal to")
equal.grid(column=0, row=1)

# result label
result = Label(text="0")
result.grid(column=1, row=1)

# km label
km = Label(text="km")
km.grid(column=2, row=1)

# calculate button
calc_button = Button(text="Calculate", command=calculate)
calc_button.grid(column=1, row=2)

window.mainloop()