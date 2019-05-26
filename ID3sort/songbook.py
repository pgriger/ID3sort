#         File: songbook.py
#         Name: Peter Griger
#        Email: p.griger@gmail.com
#         Date: 23.05.2019
#    Libraries: mutagen.easyid3, re
# Dependencies: editor.py
#        Desc.: Objects managing file ID3 tags and currently loaded collection of files.

from mutagen.easyid3 import EasyID3
import re
import editor as e


class Song:
    """Stores data of single mp3 file. Can rewrite ID3 tags."""
    def __init__(self, file):
        """Load ID3 tags from file."""
        self.mp3 = EasyID3(file)
        self.path = file
        self.artist = self.mp3['artist']
        self.album = self.mp3['album']
        self.title = self.mp3['title']
        try:
            self.titlenr = self.mp3['tracknumber']
        except:
            self.titlenr = '01'   # if no track number assign 01
        try:
            self.year = self.mp3['date']
        except:
            self.year = '2000'    # if no year of release assign 2000

        self.edit_flag = False    # edit flag
        self.song_data = None   # data structure list
        self.id3_data()    # get original ID3 tags on init
        # data struct = [file path, artist, title, album, title number, year of release]

    def __str__(self):
        return str('''song object {} from {}''').format(*self.title, *self.artist)

    def change_file(self, target_file):
        """Change target file while preserving data so write fn targets newly moved/copied file."""
        self.mp3 = EasyID3(target_file)

    def id3_data(self):
        """Get original ID3 tags. Run on init."""
        song_data = [self.path] + [tag[0] for tag in [self.artist, self.title, self.album, self.titlenr, self.year]]
        song_data[5] = re.findall(r'\d{4}|$', song_data[5])[0]  # keep only year from possible date
        song_data[5] = song_data[5].zfill(2)    # track number is always 2 digit - 01, 05, 25
        self.song_data = song_data

    def id3_write(self):
        """Write new ID3 tags."""
        self.mp3['artist'] = self.song_data[1]
        self.mp3['title'] = self.song_data[2]
        self.mp3['album'] = self.song_data[3]
        self.mp3['tracknumber'] = self.song_data[4]
        self.mp3['date'] = self.song_data[5]
        self.mp3.save(v2_version=3)

    def data(self):
        """Returns current ID3 tag data structure (may be edited)."""
        return self.song_data


class Book:
    """List of Song objects created from input files. Can return data, delete instances, edit."""
    sort_opt = {'path': 0, 'artist': 1, 'title': 2, 'album': 3, 'tracknr': 4, 'year': 5}

    def __init__(self):
        """Clean list on init."""
        self.book = list()

    def add_songs(self, files):
        """Append Song object create from files."""
        for f in files:
            self.book.append(Song(f))

    def __str__(self):
        return str('''Book of song objects. Contains {} songs.'''.format(len(self.book)))

    def data(self, sort='artist', flag=False):
        """Returns list of Song data structs. Sorted by 'sort' column and in fwd or rev 'flag'.
           Returns directly in treeview widget."""
        songs = list()
        for song in self.book:
            songs.append(song.data())
        songs.sort(key=lambda x: x[Book.sort_opt.get(sort)], reverse=flag)
        return songs

    def longest_string(self, option='path'):
        """Returns length of longest string in column to fit column width."""
        longest = max(len(x[Book.sort_opt.get(option)]) for x in self.data())
        return longest+5

    def delete_songs(self, songs_to_kill):
        """Deletes song with values same as song_to_kill. songs_to_kill is list of Song obj data structs.
           Path is always unique - used as condition."""
        songs_to_kill = [s[0] for s in songs_to_kill]
        self.book = [song for song in self.book if song.data()[0] not in songs_to_kill]

    def edit(self, path):
        """Edits Song obj with path."""
        song = [song for song in self.book if song.data()[0] == path][0]    # find obj
        editor = e.Editor()    # create editor window
        new_data = editor.load(*song.data())    # returned data from editor
        if new_data[1] == 'code 01: restore default':
            # 'Restore' pressed in editor
            song.id3_data()
        else:
            # 'Save' pressed in editor
            song.song_data = new_data
            song.edit_flag = True   # flag that obj edited
