"""
Initial UI for user to decide to either create new data or search for past metrics

maintainer: Matthew Moroge
"""

import tkinter as tk
from tkinter import messagebox
import csv
import datetime

""" 
Functionality/variables/methods
"""
# creating window instance
window = tk.Tk()
# setting ui title
window.title("Report Metrics")

# create should be a button not a label
create_label = tk.Label(window, text="Create new entry data: ")
week_label = tk.Label(window, text="Enter start date of week wanted: ")
range_label = tk.Label(window, text="Enter range of dates for metrics: ")
quartely_label = tk.Label(window, text="Enter quarter(s) of metrics wanted: ")
year_label = tk.Label(window, text="Enter year for total metrics of that year: ")

# User input entries for labels
create_entry = tk.Entry(window)
week_entry = tk.Entry(window)
range_entry = tk.Entry(window)
quartely_entry = tk.Entry(window)
year_entry = tk.Entry(window)

# buttons
create_button = tk.Button(
    window,
    text="Save",
    # command= * PUT entry_ui class here
)

# this button will take start new window for entry_id.py. TODO just need to create the class in entry_id.py and use in the 
# "command" argument in the tk.Button method.
#new_window_button = tk.Button(master, text="Create new entry data", command=new_window)

""" 
UI Layout
"""
# labels
create_label.grid(row=0, column=0, sticky= "nsew", pady= 2)
week_label.grid(row=1, column=0, sticky= "nsew", pady= 2)
range_label.grid(row=2, column=0, sticky= "nsew", pady= 2)
quartely_label.grid(row=3, column=0, sticky= "nsew", pady= 2)
year_label .grid(row=4, column=0, sticky= "nsew", pady= 2)

# Entries
create_entry.grid(row=0, column=1, sticky= tk.W, pady= 2)
week_entry.grid(row=1, column=1, sticky= tk.W, pady= 2)
range_entry.grid(row=2, column=1, sticky= tk.W, pady= 2)
quartely_entry.grid(row=3, column=1, sticky= tk.W, pady= 2)
year_entry.grid(row=4, column=1, sticky= tk.W, pady= 2)

# Buttons
create_button.grid(row=5, column=1, sticky="nsew", pady=2)



""" 
closes window, using it for testing right now, but should create a button to close window 
"""
window.after(30000,lambda:window.destroy())


window.mainloop()