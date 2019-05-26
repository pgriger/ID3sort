#         File: editor.py
#         Name: Peter Griger
#        Email: p.griger@gmail.com
#         Date: 23.05.2019
#    Libraries: tkinter
#        Desc.: Editor window for ID3sort.
#               Allows editing and restoring of ID3 tags on double clicking table item in main GUI.

import tkinter as tk


class Editor:
    """Edit window class, only one allowed - grabs focus."""
    def __init__(self):
        self.top = tk.Toplevel()
    # setup of graphical layout of GUI  
        self.top.title("ID3sort Editor")
        try:
            self.top.iconbitmap('icon.ico')
        except:
            pass
        self.top.configure(background="#d9d9d9")
        self.top.minsize(width=400, height=210)
        self.top.columnconfigure(1, weight=1)

        font11 = "-family Arial -size 9 -weight normal -slant roman -underline 0 -overstrike 0"
        font10 = "-family Arial -size 10 -weight normal -slant roman -underline 0 -overstrike 0"
        font9 = "-family Arial -size 10 -weight bold -slant roman -underline 0 -overstrike 0"

        # label 'Artist'
        self.label_artist = tk.Label(self.top)
        self.label_artist.grid(column=0,
                               row=0,
                               padx=(10, 0),    # pad 10 from left, 0 from right
                               pady=(10, 5),    # pad 10 from top, 5 from bot
                               sticky='we')
        self.label_artist.configure(background="#d9d9d9",
                                    text='''Artist:''',
                                    font=font10,
                                    anchor='e')

        # label 'Title'
        self.label_title = tk.Label(self.top)
        self.label_title.grid(column=0,
                              row=1,
                              padx=(10, 0),
                              pady=5,
                              sticky='we')
        self.label_title.configure(background="#d9d9d9",
                                   text='''Title:''',
                                   font=font10,
                                   anchor='e')

        # label 'Album'
        self.label_album = tk.Label(self.top)
        self.label_album.grid(column=0,
                              row=2,
                              padx=(10, 0),
                              pady=5,
                              sticky='we')
        self.label_album.configure(background="#d9d9d9",
                                   text='''Album:''',
                                   font=font10,
                                   anchor='e')

        # label 'Title number'
        self.label_number = tk.Label(self.top)
        self.label_number.grid(column=0,
                               row=3,
                               padx=(10, 0),
                               pady=5,
                               sticky='we')
        self.label_number.configure(background="#d9d9d9",
                                    text='''Title nr.:''',
                                    font=font10,
                                    anchor='e')

        # label 'Year'
        self.label_year = tk.Label(self.top)
        self.label_year.grid(column=0,
                             row=4,
                             padx=(10, 0),
                             pady=5,
                             sticky='we')
        self.label_year.configure(background="#d9d9d9",
                                  text='''Year:''',
                                  font=font10,
                                  anchor='e')

        # entry field for artist
        self.entry_artist = tk.Entry(self.top)
        self.entry_artist.grid(column=1,
                               row=0,
                               columnspan=3,
                               pady=(10, 0),
                               padx=(5, 10),
                               sticky='we')
        self.entry_artist.configure(background="white",
                                    font=font11,
                                    selectbackground="#c4c4c4",
                                    selectforeground="black")

        # entry field for title
        self.entry_title = tk.Entry(self.top)
        self.entry_title.grid(column=1,
                              row=1,
                              columnspan=3,
                              padx=(5, 10),
                              sticky='we')
        self.entry_title.configure(background="white",
                                   font=font11,
                                   selectbackground="#c4c4c4",
                                   selectforeground="black")

        # entry field for album
        self.entry_album = tk.Entry(self.top)
        self.entry_album.grid(column=1,
                              row=2,
                              columnspan=3,
                              padx=(5, 10),
                              sticky='we')
        self.entry_album.configure(background="white",
                                   font=font11,
                                   selectbackground="#c4c4c4",
                                   selectforeground="black")

        # entry field for title number
        self.entry_number = tk.Entry(self.top)
        self.entry_number.grid(column=1,
                               row=3,
                               columnspan=3,
                               padx=(5, 10),
                               sticky='we')
        self.entry_number.configure(background="white",
                                    font=font11,
                                    selectbackground="#c4c4c4",
                                    selectforeground="black")

        # entry field for year
        self.entry_year = tk.Entry(self.top)
        self.entry_year.grid(column=1,
                             row=4,
                             columnspan=3,
                             padx=(5, 10),
                             sticky='we')
        self.entry_year.configure(background="white",
                                  font=font11,
                                  selectbackground="#c4c4c4",
                                  selectforeground="black")

        # button 'Restore' for restoring original ID3 tags
        self.button_restore = tk.Button(self.top)
        self.button_restore.grid(column=2,
                                 row=5,
                                 padx=7,
                                 sticky='ew')
        self.button_restore.configure(background="#d9d9d9",
                                      font=font9,
                                      width=9,
                                      text='''Restore''')

        # button 'Save', save current ID3 tags from entry fields
        self.button_save = tk.Button(self.top)
        self.button_save.grid(column=3,
                              row=5,
                              padx=7,
                              pady=10,
                              sticky='ew')
        self.button_save.configure(background="#d9d9d9",
                                   font=font9,
                                   width=9,
                                   text='''Save''')
    # END of setup of graphical layout of GUI

        # empty string var to be filled with load function
        self.artist = tk.StringVar()
        self.title = tk.StringVar()
        self.album = tk.StringVar()
        self.number = tk.StringVar()
        self.year = tk.StringVar()

        # assign text vars to entry fields
        self.entry_artist.configure(textvariable=self.artist)
        self.entry_title.configure(textvariable=self.title)
        self.entry_album.configure(textvariable=self.album)
        self.entry_number.configure(textvariable=self.number)
        self.entry_year.configure(textvariable=self.year)

        # buttons commands
        self.button_restore.configure(command=self.restore)
        self.button_save.configure(command=self.save)

        self.top.withdraw()    # editor window always runs but it is hidden when not needed

    def load(self, path, artist, title, album, number, year):
        """Sets current item values to entry fields and returns new values."""
        # set text variables to display current file values
        self.artist.set(artist)
        self.title.set(title)
        self.album.set(album)
        self.number.set(number)
        self.year.set(year)
        # show window and grab focus and freeze main win
        self.top.deiconify()
        self.top.grab_set()
        self.top.wait_window()
        # returns new values to be incorporated into Book obj
        return [path, self.artist.get(), self.title.get(), self.album.get(), self.number.get(), self.year.get()]

    def save(self):
        """Release set and destroy window"""
        self.top.grab_release()
        self.top.destroy()

    def restore(self):
        """Release set and destroy window. Set flag for restoring ID3 in Book obj"""
        self.artist.set('code 01: restore default')
        self.top.grab_release()
        self.top.destroy()
