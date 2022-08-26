# Tkinter guide  
  
## Creates instance of tkinter class that will create the application main window.  
```
window = tk.Tk()
```  
## Running instance -- method that keeps the window visible and running (till closed) on the screen. Typically placed as last statement of program 
### ```window.destroy()``` will close the window for me 
```
window.mainloop()
```
## Labels -- (adding a widget(a control in tkinter; i.e buttons, labels, scrollbars, etc) labels are used to display text and messages and customiziable (colors can be name/hex/RGB)  
```
greeting = tk.Label(
    text="hello world",
    foreground="red",
    background="white",
    width=10,
    height=10
    )
```  
## Buttons -- buttons are used to display clickable buttons, can be configured to call a function when clicked  
```
button = tk.Button(
    text="click me",
    foreground="white",
    background="black",
    width=25,
    height=5
)
```  
## Entry -- entry displays a small text box to get user input  
**three main operations for entry to get user input:**  
- Retrieving text with .get()
- Deleting text with .delete()
- Inserting text with .insert()  
```
entry = tk.Entry(
    foreground="yellow",
    background="blue",
    width=50
)
```  
## Text box -- Text opens a text box for user input. I can recieve the text from user input with .get(), but takes at least one argument to retreive n characters to receive all the characters use .get("1.0", tk.END)  
```
text_box = tk.Text()
```  
## Frame -- A Frame is for organizing the layout of your widgets, thought of as containers you assign other widgets to a Frame frames size the window as small as possible to encompass the frame  
**frames allow for the following customization: (to apply these, borderwidth must be set to > 1)**
- tk.FLAT has no border effect (default value)
- tk.SUNKEN creates a sunken effect
- tk.RAISED creates a raised effect
- tk.GROOVE creates a grooved border effect
- tk.RIDGE creats a ridged effect  
```
frame = tk.Frame(relief=tk.GROOVE, borderwidth=5)
frame_label = tk.Label(
    master=frame,
    text="I'm a framed label",
    foreground="orange",
    background="pink",
    width=25,
    height=10
)
frame_label.pack()
```  
## Packing -- ay to add widget to window, there are also several other ways to do this.  when packing a widget, tkinter sizes the window as small as possible to encompass the widget 
**Packing is a Geometry Manager (controls layout), there are three Geometry managers:**  
- .pack() places widgets in aframe or window in a specific order by placing them in a rectangle and centering them
- .place() controls precise location that a widget should occupy in a window or frame
- .grid() provides the power of pack but easier to maintain because it uses rows and columns 
```
greeting.pack()
button.pack()
entry.pack()
frame.pack()
```
