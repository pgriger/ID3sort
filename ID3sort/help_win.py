#         File: editor.py
#         Name: Peter Griger
#        Email: p.griger@gmail.com
#         Date: 23.05.2019
#    Libraries: tkinter, tkinter.ttk
#        Desc.: Help section of ID3sort program. Explains functionality, controls and short cuts.

import tkinter as tk
import tkinter.ttk as ttk


class Help:
    """Help window class. Only one instance allowed."""
    exist = False    # flag is window exists

    def __init__(self):
        """Create Help window"""
        if not Help.exist:
            font11 = "-family Arial -size 9 -weight normal -slant roman -underline 0 -overstrike 0"

            # create and configure new window
            self.top = tk.Toplevel()
            self.top.title("ID3sort Help")
            try:
                self.top.iconbitmap('icon.ico')
            except:
                pass
            self.top.minsize(width=200, height=200)
            self.top.columnconfigure(0, weight=1)
            self.top.rowconfigure(0, weight=1)

            # create notebook widged with 3 abs
            self.tabs = ttk.Notebook(self.top)
            self.tabs.grid(column=0, row=0, sticky='snwe')
            self.frame_general = tk.Frame(self.tabs)
            self.frame_sort = tk.Frame(self.tabs)
            self.frame_setup = tk.Frame(self.tabs)
            self.tabs.add(self.frame_general, padding=3)
            self.tabs.add(self.frame_sort, padding=3)
            self.tabs.add(self.frame_setup, padding=3)
            self.tabs.tab(0, text="General        ")
            self.tabs.tab(1, text="Sort mp3        ")
            self.tabs.tab(2, text="Setup program  ")

            # setup first tab
            self.frame_general.configure(background="#d9d9d9")
            self.frame_general.rowconfigure(0, weight=1)
            self.frame_general.columnconfigure(0, weight=1)

            # first tab text
            self.text1 = tk.Text(self.frame_general)
            self.text1.grid(sticky='nswe')
            self.text1.insert(tk.END, text1)
            self.text1.configure(state='disabled',
                                 font=font11,
                                 background='#d9d9d9',
                                 wrap=tk.WORD)

            # setup second tap
            self.frame_sort.configure(background="#d9d9d9")
            self.frame_sort.rowconfigure(0, weight=1)
            self.frame_sort.columnconfigure(0, weight=1)

            # second tab text
            self.text2 = tk.Text(self.frame_sort)
            self.text2.grid(sticky='nswe')
            self.text2.insert(tk.END, text2)
            self.text2.configure(state='disabled',
                                 font=font11,
                                 background='#d9d9d9',
                                 wrap=tk.WORD)

            # setup third tap
            self.frame_setup.configure(background="#d9d9d9")
            self.frame_setup.rowconfigure(0, weight=1)
            self.frame_setup.columnconfigure(0, weight=1)

            # third tab text
            self.text3 = tk.Text(self.frame_setup)
            self.text3.grid(sticky='nswe')
            self.text3.insert(tk.END, text3)
            self.text3.configure(state='disabled',
                                 font=font11,
                                 background='#d9d9d9',
                                 wrap=tk.WORD)

            Help.exist = True    # flag that win exists
            self.top.protocol("WM_DELETE_WINDOW", self.on_close)    # run fn on_close when closed

    def on_close(self):
        Help.exist = False    # on closing set flag to Flase
        self.top.destroy()


# first tab text
text1 = (
    'ID3sort is utility for creating directory structures based on ID3 tags of mp3 files. '
    'Manual editing of ID3 is also implemented. '
    'Program can process files only in mp3 format and works only with following '
    'ID3 categories: artist, title, album, title number, year of release. '
    'Program is separated into two tabs, first is main window and second is setup window.'
    '\n\nHelp section is separeted into three tabs. First tab is general description, '
    'second is explaining main part of program, \'Sort\' tab, third is describing how to setup program using \'Setup\' tab. '
    'Hoovering over some buttons brings out tooltip.'
    '\n\n\nTHANK YOU!'
    '\n\nFor further inquiry write to p.griger@gmail.com'
)

# second tab text
text2 = (
    'Sort screen consists of button panel and table. Button Sort will organize loaded mp3 files according to setup '
    'options and loaded or edited ID3 tags. Help button will open window with information about program.'
    '\n\nTable will display all information about currently loaded mp3 files in columns: '
    'path, artist, album, title, title number, year of release. To load a new set of of mp3 files click Load, '
    'to add files to currently loaded collection Ctrl+Click Load button. You can delete any '
    'number of loaded files from table by selecting and pressing Delete key.'
    '\n\nAdditional functions of table are all realized by clicking on various elements of table. '
    '\nLeft clicking the column header will alphabetically sort files in table according '
    'to clicked header, clicking again will reverse sort.'
    '\nRight clicking column header will hide respective column.'
    '\nDouble right click anywhere will show all columns.'
    '\nDouble left click on header separators will fit column width to text.'
    '\nDouble left click on mp3 file in table will open ID3 editor.'
    '\n\nYou can edit ID3 data in ID3 editor by typing new values into respective fields and pressing Save button. '
    'You can restore original ID3 data by pressing button Restore. Closing editor will have no effect on ID3 tags.'
)

# third tab text
text3 = (
    'Setup tab has two fields: Output directory and Output format.'
    '\n\nIn Output directory field, you can specify root directory for output files either by writing path or pressing '
    'Change and choosing desired root folder. If desired path does not exists, it will b created at Sort action.'
    '\nYou can delete all empty folders in whole hierarchy under root folder by pressing Clean button.'
    '\n\nIn Output format section you will need to set up a control string. Click Example button to see how to set up '
    'a control string. You can reset the control string to default by pressing Default button. Everything besides '
    'keywords, will be written to the folders and files names exactly as is specified in the control string. '
    'Choose if you want to move or copy mp3 files with radiobutton bellow control string.'
)
