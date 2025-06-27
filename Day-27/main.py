from tkinter import *

window = Tk()
window.title("GUI")
window.minsize(width=500,height=300)

my_label = Label(text="I am a Label", font=("Arial", 18, "bold"))
my_label.pack()

my_label['text'] = "New Text"
my_label.config(text="Even Newer Text")


#Button
def button_clicked():
    my_label.config(text=f"{input.get()}")

button = Button(text="Click Me", command=button_clicked)
button.pack()


# Entry

input = Entry(width=12)
input.pack()
input.get()


window.mainloop()