import tkinter as tk
from turtle import back

# creates instance of tkinter class that will create the application main window.
window = tk.Tk()

# adding a widget(a control in tkinter; i.e buttons, labels, scrollbars, etc)
# labels are used to display text and messages and customiziable (colors can be name/hex/RGB)
greeting = tk.Label(
    text="hello world",
    foreground="red",
    background="white",
    width=10,
    height=10
    )

# buttons are used to display clickable buttons, can be configured to call a function when clicked
button = tk.Button(
    text="click me",
    foreground="white",
    background="black",
    width=25,
    height=5
)

# entry displays a small text box to get user input
# three main operations for entry to get user input:
# Retrieving text with .get()
# Deleting text with .delete()
# Inserting text with .insert()
entry = tk.Entry(
    foreground="yellow",
    background="blue",
    width=50
)

# Text opens a text box for user input
# I can recieve the text from user input with .get(), but takes at least one argument to retreive n characters
# to receive all the characters use .get("1.0", tk.END)
text_box = tk.Text()

# way to add widget to window, there are also several other ways to do this. 
# when packing a widget, tkinter sizes the window as small as possible to encompass the widget
greeting.pack()
button.pack()
entry.pack()


# grabbing user input from entry and assigning it to my program
name = entry.get()
print(name)

# method that keeps the window visible and running (till closed) on the screen. Typically placed as last statement of program
window.mainloop()
# window.destroy() will close the window for me

