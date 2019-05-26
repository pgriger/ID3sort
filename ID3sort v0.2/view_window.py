import sys
import tkinter as tk
import tkinter.ttk as ttk


class View:

    def __init__(self):
        '''Class of view window. Instantiated at start of MainWin and then hidden.
        Show/hide by method of View button.'''

        #create window self.toplevel
        self.top = tk.Toplevel()

        #variable definition
        self.sort_option = tk.StringVar(value='Path')
        self.show_option = [tk.IntVar(value=1) for _ in range(6)]
        self.visibility = 'visible'

        #graphic layout definition
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'

        self.top.geometry("202x116+1286+45")
        self.top.title("View")
        self.top.configure(background="#d9d9d9")
        self.top.configure(highlightbackground="#d9d9d9")
        self.top.configure(highlightcolor="black")

        self.label_show = tk.Label(self.top)
        self.label_show.place(relx=0.05, rely=0.086, height=21, width=48)
        self.label_show.configure(activebackground="#f9f9f9")
        self.label_show.configure(activeforeground="black")
        self.label_show.configure(anchor='e')
        self.label_show.configure(background="#d9d9d9")
        self.label_show.configure(disabledforeground="#a3a3a3")
        self.label_show.configure(foreground="#000000")
        self.label_show.configure(highlightbackground="#d9d9d9")
        self.label_show.configure(highlightcolor="black")
        self.label_show.configure(text='''Show:''')

        self.check_path = tk.Checkbutton(self.top)
        self.check_path.place(relx=0.297, rely=0.086, relheight=0.216
                , relwidth=0.277)
        self.check_path.configure(activebackground="#ececec")
        self.check_path.configure(activeforeground="#000000")
        self.check_path.configure(anchor='w')
        self.check_path.configure(background="#d9d9d9")
        self.check_path.configure(disabledforeground="#a3a3a3")
        self.check_path.configure(foreground="#000000")
        self.check_path.configure(highlightbackground="#d9d9d9")
        self.check_path.configure(highlightcolor="black")
        self.check_path.configure(justify='left')
        self.check_path.configure(text='''Path''')

        self.check_artist = tk.Checkbutton(self.top)
        self.check_artist.place(relx=0.297, rely=0.259, relheight=0.216
                                , relwidth=0.277)
        self.check_artist.configure(activebackground="#ececec")
        self.check_artist.configure(activeforeground="#000000")
        self.check_artist.configure(anchor='w')
        self.check_artist.configure(background="#d9d9d9")
        self.check_artist.configure(disabledforeground="#a3a3a3")
        self.check_artist.configure(foreground="#000000")
        self.check_artist.configure(highlightbackground="#d9d9d9")
        self.check_artist.configure(highlightcolor="black")
        self.check_artist.configure(justify='left')
        self.check_artist.configure(text='''Artist''')

        self.check_title = tk.Checkbutton(self.top)
        self.check_title.place(relx=0.297, rely=0.431, relheight=0.216
                               , relwidth=0.302)
        self.check_title.configure(activebackground="#ececec")
        self.check_title.configure(activeforeground="#000000")
        self.check_title.configure(anchor='w')
        self.check_title.configure(background="#d9d9d9")
        self.check_title.configure(disabledforeground="#a3a3a3")
        self.check_title.configure(foreground="#000000")
        self.check_title.configure(highlightbackground="#d9d9d9")
        self.check_title.configure(highlightcolor="black")
        self.check_title.configure(justify='left')
        self.check_title.configure(text='''Title''')

        self.check_number = tk.Checkbutton(self.top)
        self.check_number.place(relx=0.594, rely=0.259, relheight=0.216
                                , relwidth=0.401)
        self.check_number.configure(activebackground="#ececec")
        self.check_number.configure(activeforeground="#000000")
        self.check_number.configure(anchor='w')
        self.check_number.configure(background="#d9d9d9")
        self.check_number.configure(disabledforeground="#a3a3a3")
        self.check_number.configure(foreground="#000000")
        self.check_number.configure(highlightbackground="#d9d9d9")
        self.check_number.configure(highlightcolor="black")
        self.check_number.configure(justify='left')
        self.check_number.configure(text='''Track Nr.''')

        self.check_album = tk.Checkbutton(self.top)
        self.check_album.place(relx=0.594, rely=0.086, relheight=0.216
                               , relwidth=0.302)
        self.check_album.configure(activebackground="#ececec")
        self.check_album.configure(activeforeground="#000000")
        self.check_album.configure(anchor='w')
        self.check_album.configure(background="#d9d9d9")
        self.check_album.configure(disabledforeground="#a3a3a3")
        self.check_album.configure(foreground="#000000")
        self.check_album.configure(highlightbackground="#d9d9d9")
        self.check_album.configure(highlightcolor="black")
        self.check_album.configure(justify='left')
        self.check_album.configure(text='''Album''')

        self.check_year = tk.Checkbutton(self.top)
        self.check_year.place(relx=0.594, rely=0.431, relheight=0.216
                              , relwidth=0.302)
        self.check_year.configure(activebackground="#ececec")
        self.check_year.configure(activeforeground="#000000")
        self.check_year.configure(anchor='w')
        self.check_year.configure(background="#d9d9d9")
        self.check_year.configure(disabledforeground="#a3a3a3")
        self.check_year.configure(foreground="#000000")
        self.check_year.configure(highlightbackground="#d9d9d9")
        self.check_year.configure(highlightcolor="black")
        self.check_year.configure(justify='left')
        self.check_year.configure(text='''Year''')

        self.label_sort = tk.Label(self.top)
        self.label_sort.place(relx=0.05, rely=0.69, height=21, width=48)
        self.label_sort.configure(activebackground="#f9f9f9")
        self.label_sort.configure(activeforeground="black")
        self.label_sort.configure(anchor='e')
        self.label_sort.configure(background="#d9d9d9")
        self.label_sort.configure(disabledforeground="#a3a3a3")
        self.label_sort.configure(foreground="#000000")
        self.label_sort.configure(highlightbackground="#d9d9d9")
        self.label_sort.configure(highlightcolor="black")
        self.label_sort.configure(text='''Sort by:''')

        #OptionMenu lacks configure method. Modification possible only at __init__.
        #__init__(master,variable,option1,option2,option3...,command=func) <-master,variable,options positional, command called
        self.menu_sort = tk.OptionMenu(self.top, self.sort_option, 'Path', 'Artist', 'Title', 'Album', 'Track Nr.', 'Year')
        self.menu_sort.place(relx=0.347, rely=0.69, height=24, width=87)
        self.menu_sort.configure(activebackground="#ececec")
        self.menu_sort.configure(activeforeground="#000000")
        self.menu_sort.configure(background="#d9d9d9")
        self.menu_sort.configure(disabledforeground="#a3a3a3")
        self.menu_sort.configure(foreground="#000000")
        self.menu_sort.configure(highlightbackground="#d9d9d9")
        self.menu_sort.configure(highlightcolor="black")
        self.menu_sort.configure(width=120)


        #checkbuttons to chose what to show
        self.check_path.configure(variable=self.show_option[0])
        self.check_artist.configure(variable=self.show_option[1])
        self.check_title.configure(variable=self.show_option[2])
        self.check_album.configure(variable=self.show_option[3])
        self.check_number.configure(variable=self.show_option[4])
        self.check_year.configure(variable=self.show_option[5])

    def hide_show(self):
        if self.visibility is 'hidden':
            self.top.deiconify()
            self.visibility = 'visible'
        elif self.visibility is 'visible':
            self.top.withdraw()
            self.visibility = 'hidden'