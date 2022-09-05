""" 
UI for entering data, searching data stored, and presenting graph

maintainer: Matthew Moroge
"""
import tkinter as tk
from datetime import datetime
import os
import yaml

from entry_class import EntryWithPlaceholder

def entry_window():
    """ 
    Creates a new window for user to enter data
    """

    def add_to_yaml():
        """ 
        Storing entry data to csv 
        """
        date = datetime.now()
        cur_year = date.year
        filename = "data.yaml"
        yaml_file_path = os.path.join(os.getcwd(), f"artifacts/{filename}")
        
        
        entry_dict= {
            f"{week_start_entry.get()}-{week_end_entry.get()}":{

            "weekstart": week_start_entry.get(),
            "weekend": week_end_entry.get(),
            "new": new_projects_entry.get(),
            "reopened": reopened_projects_entry.get(),
            "closed": closed_projects_entry.get()
            }
        }

        new_dict= {
            cur_year: {
                f"{week_start_entry.get()}-{week_end_entry.get()}":{

                    "weekstart": week_start_entry.get(),
                    "weekend": week_end_entry.get(),
                    "new": new_projects_entry.get(),
                    "reopened": reopened_projects_entry.get(),
                    "closed": closed_projects_entry.get()
                }
            }
        }


        

        if os.path.isfile(yaml_file_path):
            with open(yaml_file_path, "r") as yamlfile:
                cur_yaml = yaml.safe_load(yamlfile)
                cur_yaml[cur_year].update(entry_dict)
            if cur_yaml:
                with open(yaml_file_path, "w") as yamlfile:
                    yaml.safe_dump(cur_yaml, yamlfile)
        else:
            with open(yaml_file_path, "w") as yamlfile:
                yaml.safe_dump(new_dict, yamlfile)
        new_window.withdraw()

    new_window = tk.Toplevel()
    new_window.title("Report Metrics")

    # adjusting grid for re-sizing of window
    tk.Grid.rowconfigure(new_window, (0,1,2,3,4,5), weight=1)
    tk.Grid.columnconfigure(new_window, (0,1), weight=1)

    # labels
    
    week_start_label = tk.Label(new_window, text="Enter beginng of week: ")
    week_end_label = tk.Label(new_window, text="Enter end of week: ")
    new_projects_label = tk.Label(new_window, text="Enter number of new projects: ")
    active_projects_label = tk.Label(new_window, text="Enter number of active projects: ")
    closed_projects_label = tk.Label(new_window, text="Enter the number of closed projects: ")
    reopened_projects_label = tk.Label(new_window, text="Enter number of re-opened projects")

    # User input entries for labels
    
    week_start_entry = EntryWithPlaceholder(new_window, "01/01/2022")
    week_end_entry = EntryWithPlaceholder(new_window, "01/30/2022")
    new_projects_entry = EntryWithPlaceholder(new_window, "42")
    active_projects_entry = EntryWithPlaceholder(new_window, "42")
    closed_projects_entry = EntryWithPlaceholder(new_window, "42")
    reopened_projects_entry = EntryWithPlaceholder(new_window, "42")

    # buttons
    save_button = tk.Button(
        new_window,
        text="Save",
        command=add_to_yaml
    )


    """
    UI layout
    """
    # labels
    week_start_label.grid(row=0, column=0, sticky= "nsew", pady= 2)
    week_end_label.grid(row=1, column=0, sticky= "nsew", pady= 2)
    new_projects_label.grid(row=2, column=0, sticky= "nsew", pady= 2)
    active_projects_label.grid(row=3, column=0, sticky= "nsew", pady= 2)
    reopened_projects_label.grid(row=4, column=0, sticky="nsew", pady=2)
    closed_projects_label.grid(row=5, column=0, sticky= "nsew", pady= 2)

    # Entries
    week_start_entry.grid(row=0, column=1, sticky= tk.W, pady= 2)
    week_end_entry.grid(row=1, column=1, sticky= tk.W, pady= 2)
    new_projects_entry.grid(row=2, column=1, sticky= tk.W, pady= 2)
    active_projects_entry.grid(row=3, column=1, sticky= tk.W, pady= 2)
    reopened_projects_entry.grid(row=4, column=1, sticky=tk.W, pady=2)
    closed_projects_entry.grid(row=5, column=1, sticky= tk.W, pady= 2)

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
week_entry = EntryWithPlaceholder(window, "07/22/2022")
range_entry = EntryWithPlaceholder(window, "01/01/2022-08/08/2022")
quartely_entry = EntryWithPlaceholder(window, "q1")
year_entry = EntryWithPlaceholder(window, "2022")

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
window.after(300000,lambda:window.destroy())


window.mainloop()