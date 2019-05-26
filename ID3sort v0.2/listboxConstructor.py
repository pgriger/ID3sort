from mutagen.easyid3 import EasyID3
import re

class Song(object):

    def __init__(self, file):
        mp3 = EasyID3(file)
        self.path = file
        self.artist = mp3['artist']
        self.album = mp3['album']
        self.title = mp3['title']
        try: self.titlenr = mp3['tracknumber']
        except: self.titlenr='01'
        try: self.year = mp3['date']
        except: self.year='2000'

    def __str__(self):
        return str('''Instance of song class. I am {} from {}.''').format(self.title, self.artist)

    def data(self):
        song_data = [self.path.replace('/','\\')] + [tag[0] for tag in[self.artist, self.title, self.album, self.titlenr, self.year]]
        song_data[5] = re.findall(r'\d{4}|$',song_data[5])[0]
        song_data[5] = song_data[5].zfill(2)
        return song_data

    def kill(self):
        del self


class Book(object):
    def __init__(self, files):
        self.book = list()
        for f in files:
            self.book.append(Song(f))

    def __str__(self):
        return str('''Book of song objects. Contains {} songs.'''.format(len(self.book)))

    def data(self, sort='Artist'):
        sort_opt = {'Path':0, 'Artist': 1, 'Title': 2, 'Album': 3, 'Track Nr.': 4, 'Year': 5}
        songs = list()
        for song in self.book:
            songs.append(song.data())
        songs.sort(key=lambda x: x[sort_opt.get(sort)])
        return songs