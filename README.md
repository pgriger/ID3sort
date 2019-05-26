ID3sort is a utility for organizing audio files and editing ID3 tags. Currently, program support mp3 files and following ID3 tag categories: author, title, album, title number, year of release. On further instructions and information refer to Help section inside program GUI. ID3sort was developed on Windows 10 under Python 3.7.
 
Basic concept is creating Song object out of every loaded file and then grouping created objects into Book object. Book object, as a collection (list) of all loaded Song then directly feeds GUI and takes care of sorting, deleting, editing actions. Files are output from Book object and renamed, copied, moved based on user settings.


Version description:
 - ID3sort v0.1:
 First draft of application. Getting to know Tkinter module. v0.1 can load, sort, show/hide files in it's core widget, Listbox, but other features are not implemented. It was create with GUI layout interface PAGE. Sparsely commented since it was abandoned early.
 
 - ID3sort v0.2:
 New cleaner version of application, less buttons and clutter. Used Treeview (table) widget as a core. Sort, show/hide options of Treeview were all grouped under separate View window. Core of program is functional, but there may be various bugs present. PAGE GUI generator uses .place layout manager for widgets. I encountered various problems with correctly moving widgets on window resize action.
 
 - ID3sort - Current build:
 Further streamlining, less buttons, abandoned View window and moved functionality to keybindings. Moved away from using PAGE generator and written GUI myself with .grid layout manager, what facilitated easy resize actions. Implemented editor of ID3 tags and Help section.
 
 - ID3sort executable:
 Executable version of current build. If run without icon.ico in root, window icon will fail to load, but program will work correctly.
