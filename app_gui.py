""" 
UI for entering data, searching data stored, and presenting graph

maintainer: Matthew Moroge
"""

import tkinter as tk
from tkinter import messagebox
import csv
import datetime
import os

def entry_window():
    """ 
    Creates a new window for user to enter data
    """

    def add_to_csv():
        """ 
        Storing entry data to csv 
        """
        filename = "artifacts/metrics.csv"
        csv_list = []
        entry_list = [
            week_start_entry.get(),
            week_end_entry.get(),
            new_projects_entry.get(),
            reopend_projects_entry.get(),
            closed_projects_entry.get()
        ]

        csv_list.append(entry_list)

        if os.path.isfile(filename):
            with open(filename, "a", newline='') as file:
                write_to_csv = csv.writer(file)
                write_to_csv.writerows(csv_list)
        else:
            with open(filename, "w", newline='') as file:
                write_to_csv = csv.writer(file)
                write_to_csv.writerow(["weekstart", "weekend", "new", "reopend", "closed"])
                write_to_csv.writerows(csv_list)
        new_window.withdraw()

    new_window = tk.Toplevel()
    new_window.title("Report Metrics")
    # adjusting grid for re-sizing of window
    tk.Grid.rowconfigure(new_window, (0,1,2,3,4), weight=1)
    tk.Grid.columnconfigure(new_window, (0,1), weight=1)

    # labels
    week_start_label = tk.Label(new_window, text="Enter beginng of week: ")
    week_end_label = tk.Label(new_window, text="Enter end of week: ")
    new_projects_label = tk.Label(new_window, text="Enter number of new projects: ")
    reopend_projects_label = tk.Label(new_window, text="Enter number of reopend projects: ")
    closed_projects_label = tk.Label(new_window, text="Enter the number of closed projects: ")

    # User input entries for labels
    week_start_entry = tk.Entry(new_window)
    week_end_entry = tk.Entry(new_window)
    new_projects_entry = tk.Entry(new_window)
    reopend_projects_entry = tk.Entry(new_window)
    closed_projects_entry = tk.Entry(new_window)

    # buttons
    save_button = tk.Button(
        new_window,
        text="Save",
        command=add_to_csv
    )


    """
    UI layout
    """
    # labels
    week_start_label.grid(row=0, column=0, sticky= "nsew", pady= 2)
    week_end_label.grid(row=1, column=0, sticky= "nsew", pady= 2)
    new_projects_label.grid(row=2, column=0, sticky= "nsew", pady= 2)
    reopend_projects_label.grid(row=3, column=0, sticky= "nsew", pady= 2)
    closed_projects_label.grid(row=4, column=0, sticky= "nsew", pady= 2)

    # Entries
    week_start_entry.grid(row=0, column=1, sticky= tk.W, pady= 2)
    week_end_entry.grid(row=1, column=1, sticky= tk.W, pady= 2)
    new_projects_entry.grid(row=2, column=1, sticky= tk.W, pady= 2)
    reopend_projects_entry.grid(row=3, column=1, sticky= tk.W, pady= 2)
    closed_projects_entry.grid(row=4, column=1, sticky= tk.W, pady= 2)

    # Buttons
    save_button.grid(row=5, column=1, sticky="nsew", pady=2)

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
    text="Open entry field",
    command=entry_window
)


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
create_button.grid(row=0, column=1, sticky= tk.W, pady= 2)
week_entry.grid(row=1, column=1, sticky= tk.W, pady= 2)
range_entry.grid(row=2, column=1, sticky= tk.W, pady= 2)
quartely_entry.grid(row=3, column=1, sticky= tk.W, pady= 2)
year_entry.grid(row=4, column=1, sticky= tk.W, pady= 2)

# Buttons



""" 
closes window, using it for testing right now, but should create a button to close window 
"""
window.after(30000,lambda:window.destroy())


window.mainloop()