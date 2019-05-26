import tkinter as tk
import tkinter.ttk as ttk

class Example:

    def __init__(self):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        #create new toplevel
        self.top = tk.Toplevel()

        self.top.geometry("508x188+556+366")
        self.top.title("Example")
        self.top.configure(background="#d9d9d9")

        self.Message1 = tk.Message(self.top)
        self.Message1.place(relx=0.0, rely=0.053, relheight=0.761
                , relwidth=1.004)
        self.Message1.configure(background="#d9d9d9")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''Take the 4th track from Daft Punk's album Random Access Memories from 2013 called Within.

Following control string: '*artist//*album (*year)//*artist - *album - *number - *title'

Results in following structure:
- Output Directory
    - 'Daft Punk'
        - 'Random Access Memories (2013)'
            - 'Daft Punk - Random Access Memories - 04 - Within.mp3\'''')
        self.Message1.configure(width=510)

        self.bt_ok = tk.Button(self.top)
        self.bt_ok.place(relx=0.846, rely=0.798, height=24, width=57)
        self.bt_ok.configure(activebackground="#ececec")
        self.bt_ok.configure(activeforeground="#000000")
        self.bt_ok.configure(background="#d9d9d9")
        self.bt_ok.configure(disabledforeground="#a3a3a3")
        self.bt_ok.configure(foreground="#000000")
        self.bt_ok.configure(highlightbackground="#d9d9d9")
        self.bt_ok.configure(highlightcolor="black")
        self.bt_ok.configure(pady="0")
        self.bt_ok.configure(text='''OK''')
        self.bt_ok.configure(width=57)
        self.bt_ok.configure(command=lambda: self.quit())

    def quit(self):
        self.top.grab_release()
        self.top.destroy()