"""
Initial UI for user to decide to either create new data or search for past metrics

maintainer: Matthew Moroge
"""

import tkinter as tk
from tkinter import messagebox
import csv
import datetime


# creating window instance
window = tk.Tk()
# setting ui title
window.title("Report Metrics")

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

# UI layout
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


window.mainloop()