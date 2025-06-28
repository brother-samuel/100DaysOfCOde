from tkinter import *

window = Tk()
window.title("GUI")
window.minsize(width=500,height=300)
window.config(padx=20, pady=20)

#Label
my_label = Label(text="I am a Label", font=("Arial", 18, "bold"))
my_label['text'] = "New Text"
my_label.config(text="Even Newer Text")
my_label.grid(column=0, row=0)

#Button
def button_clicked():
    my_label.config(text=f"{input.get()}")

button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

button2 = Button(text="New Button", command=button_clicked)
button2.grid(column=2, row=0)
# Entry

input = Entry(width=12)
input.get()
input.grid(column=3, row=2)


window.mainloop()