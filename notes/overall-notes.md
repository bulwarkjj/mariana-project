# Notes for what I need to work on so I'm not flooding code with comments
## entry_ui.py
- add an intial UI that asks if user wants to enter data or if user wants to pull data (i.e week, quarter, range of dates, year, etc). These two functions add the entries to a CSV file but appending the data creates a new header row. Need to figure out how to just append the data not header to CSVThought maybe use a temp dir to store recent data and access it, than store it on to the main artifacts of the folderI will create to hold all data on host desktop  

## intial_ui.py  
-  need to create a class for entry_ui and use it here, along with classes for the following data searching

- Create - this will take the entry_ui.py class and start it up, make sure to close this UI when that starts....Which means I need to 
        add a way to come back to this UI :(
- Quaterly search - will have to hard code what a quarter is than dynamicly use magic to find it in the CSV
- Year - Should be easy enough to find all the data within the specified year if I use the year as a key (maybe I should use JSON instead of CSV)
- Range - Yeah, that is gonna be a pain, I will have to regulate the user input field, do something if input is wrong, than find everything within that date range use DATETIME!!! that will standarize the input on my end
- Week - Easy enough to find the week specified