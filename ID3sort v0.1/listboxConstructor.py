from mutagen.easyid3 import EasyID3

class Song(object):
    def __init__(self, file):
        mp3 = EasyID3(file)
        self.path = file
        self.artist = mp3['artist']
        self.album = mp3['album']
        self.title = mp3['title']
        self.titlenr = mp3['tracknumber']
        self.year = mp3['date']

    def __str__(self):
        return str('''Instance of song class. I am {} from {}.''').format(self.title, self.artist)

    def lookup(self, flag='path'):
        ifs = {
                'artist': self.artist,
                'album': self.album,
                'title': self.title,
                'titlenr': self.titlenr,
                'year': self.year,
                'path': self.path
                }
        return ifs.get(flag)

    def kill(self):
        del self


class Book(object):
    book = list()

    def __init__(self, files):
        for f in files:
            self.book.append(Song(f))

    def __str__(self):
        return str('''Book of song objects. Contains {} songs.'''.format(len(self.book)))

    def give_files(self):
        files=list()
        for song in self.book:
            files.append(song.lookup('path'))
        return files

    def construct_list(self, view='path', show=[1, 1, 1, 1, 1], sort='artist'):
        ifs = {
            'artist': 0,
            'album': 1,
            'title': 2,
            'titlenr': 3,
            'year': 4,
        }

        if view == 'path':
            return self.give_files()

        elif view == 'id3view':
            files = list()

            for song in self.book:
                string = [song.artist[0], song.album[0], song.title[0], int(song.titlenr[0]), song.year[0]]
                files.append(string)

            files.insert(0, ['ALBUM', 'ARTIST', 'TITLE', 'TRACK NR.', 'YEAR'])

            column_width = [
                max(len(file[0]) for file in files),
                max(len(file[1]) for file in files),
                max(len(file[2]) for file in files),
                max(len(str(file[3])) for file in files),
                max(len(file[4]) for file in files)
                ]

            files[1:] = sorted(files[1:], key=lambda x: x[ifs.get(sort, 0)])

            for file in files:
                file[0]='{str: <{width}}'.format(str=file[0], width=column_width[0])
                file[1]='{str: <{width}}'.format(str=file[1], width=column_width[1])
                file[2]='{str: <{width}}'.format(str=file[2], width=column_width[2])
                file[3]='{str: <{width}}'.format(str='{0:0>2}'.format(file[3]), width=column_width[3])
                file[4]='{str: <{width}}'.format(str=file[4], width=column_width[4])

            files = [[item for sh,item in zip(show,file) if sh] for file in files]
            return [' | '.join(file) for file in files]