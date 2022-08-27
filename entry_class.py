""" 
Creates temp text inside Entry field to display correct input order
on user click, erases temp text 
on user focus change, temp text comes back if no text was input

maintainter: Matthew Moroge
"""

import tkinter as tk

class EntryWithPlaceholder(tk.Entry):
    """ 
    Creates temp text inside Entry field to display correct input order
    """
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey'):
        super().__init__(master)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        """ 
        temp text to be displayed with option to change foreground color
        """
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        """ 
        When user clicks on field, text deletes and fg color change
        """
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        """ 
        When user leaves field and not text was input, temp text returns
        """
        if not self.get():
            self.put_placeholder()