#         File: main.py
#         Name: Peter Griger
#        Email: p.griger@gmail.com
#         Date: 23.05.2019
#    Libraries: shutil, os, sys, re, tkinter, tkinter.tkk, tkinter messagebox, tkinter filedialog
# Dependencies: songbook.py, example_win.py, help_win.py
#        Desc.: Program edits ID3 tags of mp3 files and organizes files based on user input.
#               Input and control is facilitated trough GUI.

import shutil
import os
import sys
import re
import tkinter as tk
import tkinter.ttk as ttk
import songbook
import example_win
import help_win
from tkinter import messagebox
from tkinter import filedialog


class MainWin:
    """Sets up graphic of GUI and respective functions."""
    def __init__(self, top=None):
        """Configures and populates main window of app."""
    # Following sets up  layout of GUI.
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        font10 = "-family Arial -size 10 -weight normal -slant roman " \
                 "-underline 0 -overstrike 0"
        font11 = "-family Arial -size 9 -weight normal -slant roman " \
                 "-underline 0 -overstrike 0"
        font9 = "-family Arial -size 10 -weight bold -slant roman " \
                "-underline 0 -overstrike 0"
        self.style = ttk.Style()
        self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=[('selected', _compcolor), ('active', _ana2color)])

        # create and setup window
        top.title("ID3sort")
        try:
            top.iconbitmap('icon.ico')
        except:
            pass
        top.minsize(width=555, height=250)
        top.columnconfigure(0, weight=1)
        top.rowconfigure(0, weight=1)

        # create notebook widget with two tabs
        self.tabs = ttk.Notebook(top)
        self.tabs.grid(column=0, row=0, sticky='snwe')
        self.frame_main = tk.Frame(self.tabs)
        self.frame_setup = tk.Frame(self.tabs)
        self.tabs.add(self.frame_main, padding=3)
        self.tabs.add(self.frame_setup, padding=3)
        self.tabs.tab(0, text="Sort      ")
        self.tabs.tab(1, text="Setup     ")

        # setup frame on tab 'Sort'
        self.frame_main.configure(background="#d9d9d9")
        self.frame_main.rowconfigure(1, weight=1)
        self.frame_main.columnconfigure(4, weight=1)

        # create scrolled treeview (table) widget with 6 named columns
        self.style.configure('Treeview.Heading', font=font10)
        self.treeview = ScrolledTreeView(self.frame_main)
        self.treeview.grid(column=0,
                           row=1,
                           columnspan=5,
                           sticky='snwe')
        self.treeview.configure(columns=('path', 'artist', 'title', 'album', 'tracknr', 'year'),
                                displaycolumns=[0, 1, 2, 3, 4, 5])
        self.treeview.column("#0", stretch=0, width=0, minwidth=0)
        self.treeview.heading("path", text="Path", anchor=tk.W)
        self.treeview.heading("artist", text="Artist", anchor=tk.W)
        self.treeview.heading("title", text="Title", anchor=tk.W)
        self.treeview.heading("album", text="Album", anchor=tk.W)
        self.treeview.heading("tracknr", text="#", anchor=tk.W)
        self.treeview.heading("year", text="Year", anchor=tk.W)
        self.treeview.column("tracknr", stretch=False, width=23, minwidth=23)
        self.treeview.column("year", stretch=False, width=40, minwidth=40)

        # button 'Sort' running organizing function on files in table
        self.button_sort = tk.Button(self.frame_main)
        self.button_sort.grid(column=0,
                              row=0,
                              padx=7,
                              pady=8,
                              sticky='we')
        self.button_sort.configure(background="#d9d9d9",
                                   font=font9,
                                   width=9,
                                   text='''Sort''')

        # button 'Load', loading files into table
        self.button_load = tk.Button(self.frame_main)
        self.button_load.grid(column=1,
                              row=0,
                              padx=7,
                              pady=8,
                              sticky='we')
        self.button_load.configure(background="#d9d9d9",
                                   font=font9,
                                   width=9,
                                   text='''Load''')

        # button 'Help' opens new window with instructions
        self.button_help = tk.Button(self.frame_main)
        self.button_help.grid(column=4,
                              row=0,
                              padx=7,
                              pady=8,
                              sticky='e')
        self.button_help.configure(background="#d9d9d9",
                                   font=font10,
                                   width=9,
                                   text='''Help''')

        # setup frame on tab 'Setup'
        self.frame_setup.columnconfigure(0, weight=1)
        self.frame_setup.configure(background="#d9d9d9")

        # create sub frame for grouping output directory control elements
        self.label_output_dir = tk.LabelFrame(self.frame_setup)
        self.label_output_dir.columnconfigure(1, weight=1)
        self.label_output_dir.grid(padx=5,
                                   pady=5,
                                   sticky='nwe')
        self.label_output_dir.configure(background="#d9d9d9",
                                        font=font10,
                                        text='''Output directory''')

        # label 'Current'
        self.label_current_dir = tk.Label(self.label_output_dir)
        self.label_current_dir.grid(column=0,
                                    row=0,
                                    padx=20,
                                    pady=10,
                                    sticky='e')
        self.label_current_dir.configure(background="#d9d9d9",
                                         font=font10,
                                         text='''Current:''')

        # entry field showing currently set directory
        self.entry_out_dir = tk.Entry(self.label_output_dir)
        self.entry_out_dir.grid(column=1,
                                row=0,
                                pady=10,
                                sticky='we')
        self.entry_out_dir.configure(background="white",
                                     selectbackground="#c4c4c4",
                                     selectforeground="black",
                                     font=font11)

        # button 'Change' for choosing output directory
        self.button_change_dir = tk.Button(self.label_output_dir)
        self.button_change_dir.grid(column=3,
                                    row=0,
                                    padx=10)
        self.button_change_dir.configure(background="#d9d9d9",
                                         font=font9,
                                         width=9,
                                         text='''Change''')

        # button 'Clean' removing all empty folders
        self.button_clean = tk.Button(self.label_output_dir)
        self.button_clean.grid(column=4,
                               row=0,
                               padx=(0, 10))    # pad from (left, right)
        self.button_clean.configure(background="#d9d9d9",
                                    font=font9,
                                    width=9,
                                    text='''Clean''')

        # create sub frame for grouping output format control elements
        self.label_output_format = tk.LabelFrame(self.frame_setup)
        self.label_output_format.columnconfigure(3, weight=1)
        self.label_output_format.grid(padx=5,
                                      pady=5,
                                      sticky='nwe')
        self.label_output_format.configure(background="#d9d9d9",
                                           font=font10,
                                           text='''Output format''')

        # text displaying keywords
        self.msg_format = tk.Message(self.label_output_format)
        self.msg_format.grid(column=0,
                             row=0,
                             columnspan=4,
                             padx=15,
                             pady=10,
                             sticky='we')
        self.msg_format.configure(anchor='nw',
                                  background="#d9d9d9",
                                  font=font11,
                                  width=800,
                                  text="Key words: 'artist', 'album', 'title', 'number' and 'year'. "
                                       "To indicate new subdirectory, enter '/'.")

        # button 'Example' opening window with format setup example
        self.button_example_format = tk.Button(self.label_output_format)
        self.button_example_format.grid(column=5,
                                        row=0,
                                        padx=10,
                                        pady=10,
                                        sticky='w')
        self.button_example_format.configure(background="#d9d9d9",
                                             font=font10,
                                             width=9,
                                             text='''Example''')

        # label 'Control string'
        self.label_control_str = tk.Label(self.label_output_format)
        self.label_control_str.grid(column=0,
                                    row=1)
        self.label_control_str.configure(background="#d9d9d9",
                                         font=font10,
                                         anchor='w',
                                         text='''Control string:''')

        # entry field for format control string
        self.entry_format = tk.Entry(self.label_output_format)
        self.entry_format.grid(column=1,
                               row=1,
                               columnspan=3,
                               sticky='we')
        self.entry_format.configure(background="white",
                                    selectbackground="#c4c4c4",
                                    selectforeground="black",
                                    font=font11)

        # button 'Default' reverting control string to default
        self.button_default_format = tk.Button(self.label_output_format)
        self.button_default_format.grid(column=5,
                                        row=1,
                                        padx=10)
        self.button_default_format.configure(background="#d9d9d9",
                                             font=font9,
                                             width=9,
                                             text='''Default''')

        # label 'Move or copy'
        self.label_move_copy = tk.Label(self.label_output_format)
        self.label_move_copy.grid(column=0,
                                  row=2,
                                  pady=10,
                                  padx=20)
        self.label_move_copy.configure(anchor='e',
                                       background="#d9d9d9",
                                       font=font10,
                                       text='''Move or copy files?''')

        # radio button 'Move', if selected 'Sort' move files
        self.radio_move_file = tk.Radiobutton(self.label_output_format)
        self.radio_move_file.grid(column=1,
                                  row=2,
                                  pady=10)
        self.radio_move_file.configure(background="#d9d9d9",
                                       justify='left',
                                       text='''Move''')

        # radio button 'Copy', if selected 'Sort' copy files
        self.radio_copy_file = tk.Radiobutton(self.label_output_format)
        self.radio_copy_file.grid(column=2,
                                  row=2,
                                  padx=30,
                                  pady=10)
        self.radio_copy_file.configure(background="#d9d9d9",
                                       justify='left',
                                       text='''Copy''')
    # END of setting up GUI layout

        # variables definition
        self.sort_option = {'sort': 'path', 'flag': False}    # sort by 'sort', reverse if flag
        self.show_option = [0, 1, 2, 3, 4, 5]    # what collumns to show in table
        self.book = songbook.Book()    # empty Book object - collection of files, from songbook.py
        self.files = None    # files to be loaded into table, PEP8 def

        # output path variable and text field assignment
        self.output_path = tk.StringVar(value='C:/MP3sort')
        self.entry_out_dir.configure(textvariable=self.output_path)

        # format variable and entry field assignment
        self.format = tk.StringVar(value='artist/album (year)/artist - album - number - title')
        self.entry_format.configure(textvariable=self.format)
        self.button_default_format.configure(command=lambda: self.format.set('artist/album (year)/artist - album - number - title'))

        # copy/move variable in format subframe and radiobutton assignment
        self.copy_move = tk.StringVar(value='copy')
        self.radio_copy_file.configure(variable=self.copy_move, value='copy')
        self.radio_move_file.configure(variable=self.copy_move, value='move')

        # command setup for every button
        self.button_change_dir.configure(command=lambda: self.output_path_button_callback())
        self.button_load.configure(command=lambda: self.load_files())
        self.button_example_format.configure(command=lambda: example_win.Example())    # see class Example example_win.py
        self.button_sort.configure(command=lambda: self.sort())
        self.button_clean.configure(command=lambda: self.clean_output_root())
        self.button_help.configure(command=lambda: help_win.Help())    # see class Help in help_win.py

        # key bindings
        self.treeview.bind("<Button-1>", self.header_left_click)
        self.treeview.bind("<Button-3>", self.header_right_click)
        self.treeview.bind("<Double-Button-3>", self.header_double_right_click)
        self.treeview.bind("<Double-Button-1>", self.double_left_click)
        self.treeview.bind("<Delete>", self.delete_callback)
        self.treeview.bind("<Control-a>", self.ctrl_a_callback)
        self.treeview.bind("<Control-A>", self.ctrl_a_callback)
        self.button_load.bind("<Control-ButtonRelease-1>", self.load_partial)

        # tooltips for some widgets
        self.button_load_ttp = CreateTooltip(self.button_load, "Load new set of files.\nCtrl+Click add to current files.")
        self.button_change_dir_ttp = CreateTooltip(self.button_change_dir, "Choose output folder.")
        self.button_clean_tpp = CreateTooltip(self.button_clean, "Delete all empty folders from output folder hierarchy.")
        self.button_default_format_tt = CreateTooltip(self.button_default_format, 'Restore default control string.')

    def clean_output_root(self):
        """Traverse output directory hierarchy and deletes every empty folder found"""
        # check if ok/nok in case of miss click
        if messagebox.askokcancel("Clean output directory",
                                  "Would you like to remove all empty folders from output directory hierarchy?"):
            # iterate over hierarchy, walk returns folder, subfodlers, filenames
            for folder, _, _ in os.walk(self.output_path.get(), topdown=False):
                try:
                    os.rmdir(folder)    # try deleting folder
                except OSError as e:
                    if e.args[0] != 145:
                        pass    # pass if E145 - folder is not empty

    def ctrl_a_callback(self, _):
        """Select all item in table on Ctrl - A press"""
        self.treeview.selection_set(*self.treeview.get_children())

    def delete_callback(self, _):
        """Delete selected items from table"""
        selected_itms = self.treeview.selection()     # returns items as "ITEM2, ITEM5"
        selected = ([self.treeview.item(sel)['values'] for sel in selected_itms])     # get values of selected files from item names
        self.book.delete_songs(selected)     # call Book function, see class Book in songbook.py
        self.refresh_treeview()

    def double_left_click(self, event):
        """Item click: Creates editor window for selected files, edits values based on input.
           Separator click: Approximates width of column based on longest value present."""
        region = self.treeview.identify("region", event.x, event.y)
        if region == 'separator':
            # separator click
            column = self.treeview.identify("column", event.x, event.y)
            column = self.treeview.column(column)['id']
            if column in ['path', 'artist', 'title', 'album']:
                self.treeview.column(column, width=int(self.book.longest_string(option=column)*6.5))
        elif region == 'cell':
            # item click
            item = self.treeview.identify("item", event.x, event.y)
            self.book.edit(self.treeview.item(item)['values'][0])    # call edit from Book from songbook.py
            self.refresh_treeview()

    def header_left_click(self, event):
        """Sorts table by column on column header click.
           Set sort option and reverse option and call for refresh of table."""
        region = self.treeview.identify("region", event.x, event.y)
        column = self.treeview.identify("column", event.x, event.y)
        if region == 'heading':
            sort = self.treeview.column(column)['id']
            if sort == self.sort_option['sort']:
                self.sort_option['flag'] = not(self.sort_option['flag'])
            self.sort_option['sort'] = sort
            self.refresh_treeview(**self.sort_option)

    def header_right_click(self, event):
        """Hides column if clicked on column header. Sets show option list and reconf treeview widged"""
        region = self.treeview.identify("region", event.x, event.y)
        column = self.treeview.identify_column(event.x)
        if region == 'heading':
            column = self.treeview.heading(column)['text']    # get clicked column text name
            show_opt = {'path': 0, 'artist': 1, 'title': 2, 'album': 3, '#': 4, 'year': 5}    # mask name to number
            self.show_option.remove(show_opt.get(column.lower()))
            if not self.show_option:
                self.show_option = [0, 1, 2, 3, 4, 5]    # show all if all hidden
            self.treeview.configure(displaycolumns=self.show_option)

    def header_double_right_click(self, _):
        """RBT double click shows all columns"""
        self.show_option = [0, 1, 2, 3, 4, 5]
        self.treeview.configure(displaycolumns=self.show_option)

    def sort(self):
        """Takes copy/move, output directory, control string and file values and organizes accordingly.
           Modifies ID3 tag if they been edited."""
        self.treeview.delete(*self.treeview.get_children())
        output_root = self.output_path.get() + '/'
        os.makedirs(output_root, exist_ok=True)

        # iterate over every file in table
        for song in self.book.book:
            song_data = song.data()
            filename = self.format.get() + '.mp3'
            filename = ''.join(['' if ch in '\\"<>%:?*|' else ch for ch in filename])
            filename = re.sub(r' *([/]) *', r'\1', filename)
            # exclude windows name incompatibile characters
            song_data[1:] = [''.join(['' if ch in '\\/"<>%:?*|' else ch for ch in item]) for item in song_data[1:]]
            # replace keywords in control string with real value
            if 'artist' in filename:
                filename = filename.replace('artist', song_data[1])
            if 'title' in filename:
                filename = filename.replace('title', song_data[2])
            if 'album' in filename:
                filename = filename.replace('album', song_data[3])
            if 'number' in filename:
                filename = filename.replace('number', song_data[4])
            if 'year' in filename:
                filename = filename.replace('year', song_data[5])
            if '/' in filename:
                folders = filename.rsplit('/', 1)[0]
                os.makedirs(output_root + folders, exist_ok=True)

            # copy or move file
            if self.copy_move.get() == 'copy':
                shutil.copy(song_data[0], output_root + filename)
            else:
                shutil.move(song_data[0], output_root + filename)

            # change Book paths to new files and rewrite ID3 if edited
            song.change_file(output_root + filename)
            if song.edit_flag:
                song.id3_write()
            self.book = songbook.Book()     # create clean book instance

    def refresh_treeview(self, **sort_options):
        """Refresh table to always mirror only what is in the book instance."""
        body_font = "-family Curier -size 10 -weight normal -slant roman -underline 0 -overstrike 0"
        self.treeview.delete(*self.treeview.get_children())
        # iterate over files in book, book returns column:value pairs
        for song in self.book.data(**sort_options):
            self.treeview.insert("", tk.END, values=song, tag='monospace')
        self.treeview.tag_configure('monospace', font=body_font)    # monospace font for width calculation

    def load_files(self):
        """Select files in dialog window which will be added and create book obj."""
        self.treeview.delete(*self.treeview.get_children())
        self.files = filedialog.askopenfilenames(filetypes=[("MP3 files", ".mp3")])
        self.book = songbook.Book()     # create new clean book
        self.book.add_songs(self.files)
        self.refresh_treeview()

    def load_partial(self, _):
        """Select files in dialog window which will be added to existing book obj."""
        self.files = filedialog.askopenfilenames(filetypes=[("MP3 files", ".mp3")])
        loaded_files = [data[0] for data in self.book.data()]    # what is currently loaded
        self.files = [file for file in self.files if file not in loaded_files]    # remove already loaded from que
        self.book.add_songs(self.files)    # load
        self.refresh_treeview()

    def output_path_button_callback(self):
        """Open dialog and choose output folder"""
        self.output_path.set(value=filedialog.askdirectory())


class TreeviewScrollBar:
    """Configure scrollbars for a ttk treeview widget."""
    def __init__(self, master):
        vertical_scroll_bar = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        self.configure(yscrollcommand=self._autoscroll(vertical_scroll_bar))

        horizontal_scroll_bar = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        self.configure(xscrollcommand=self._autoscroll(horizontal_scroll_bar))

        self.grid(column=0, row=0, sticky='nsew')
        vertical_scroll_bar.grid(column=1, row=0, sticky='ns')
        horizontal_scroll_bar.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() | tk.Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        """Hide and show scrollbar as needed."""
        def wrapper(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapper


class ScrolledTreeView(TreeviewScrollBar, ttk.Treeview):
    """Standard ttk Treeview widget with scrollbars that will automatically show/hide as needed."""
    def __init__(self, master, **kw):
        container = ttk.Frame(master)
        ttk.Treeview.__init__(self, container, **kw)
        TreeviewScrollBar.__init__(self, container)


class CreateTooltip:
    """Create a tooltip for a given widget"""
    def __init__(self, widget, text='widget info'):
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.close)
        self.top = None    # window var, PEP8

    def enter(self, _):
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20

        self.top = tk.Toplevel(self.widget)
        self.top.wm_overrideredirect(True)
        self.top.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self.top)
        label.configure(text=self.text,
                        justify='left',
                        background='white',
                        relief='solid',
                        borderwidth=1,
                        font=("ariel", "8", "normal"))
        label.after(0)     # delay for tooltip, BUG: also delays function call
        label.grid()

    def close(self, _):
        if self.top:
            self.top.destroy()


if __name__ == '__main__':
    root = tk.Tk()
    MainWin(root)
    root.mainloop()
