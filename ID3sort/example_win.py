#         File: example_win.py
#         Name: Peter Griger
#        Email: p.griger@gmail.com
#         Date: 23.05.2019
#    Libraries: tkinter
#        Desc.: Window explaining how to write control string for ID3sort with example.

import tkinter as tk


class Example:
    """Example window class, only one instance allowed."""
    exists = False    # flag if window exists, closed default

    def __init__(self):
        """Example window for output format."""
        if not Example.exists:
            self.top = tk.Toplevel()
            self.top.title("Example")
            try:
                self.top.iconbitmap('icon.ico')
            except:
                pass
            self.top.configure(background="#d9d9d9")

            self.Message1 = tk.Message(self.top)
            self.Message1.grid(column=0, row=0, pady=5, padx=5, sticky='nwe')
            self.Message1.configure(background="#d9d9d9")
            self.Message1.configure(text='''Take the 4th track from Daft Punk's album Random Access Memories from 2013 called Within.

Following control string: 'artist/album (year)/artist - album - number - title'

Results in following structure:
- Output Folder
    - 'Daft Punk'
        - 'Random Access Memories (2013)'
            - 'Daft Punk - Random Access Memories - 04 - Within.mp3\'''')
            self.Message1.configure(width=510)
            Example.exists = True    # flag that win exists
            self.top.protocol("WM_DELETE_WINDOW", self.on_close)    # closing window will run on_close fn

    def on_close(self):
        Example.exists = False    # flag that win closed
        self.top.destroy()
