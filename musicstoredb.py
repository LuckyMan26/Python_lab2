import sqlite3

from utils import ElementNotFoundException, Artist, Genre


class MusicStoreDB:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cur = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS Artist (
                            id INTEGER PRIMARY KEY,
                            name TEXT,
                            genre TEXT
                            )''')
        self.cur.execute('''CREATE TABLE IF NOT EXISTS Album (
                            id INTEGER PRIMARY KEY,
                            name TEXT,
                            numberOfSongs INTEGER,
                            artist_id INTEGER,
                            FOREIGN KEY(artist_id) REFERENCES Artist(id)
                            )''')
        self.conn.commit()

    def add_artist(self, artist):
        self.cur.execute('''INSERT INTO Artist (name, genre) VALUES (?, ?)''',
                         (artist.name, artist.genre.name))
        self.conn.commit()

    def add_album(self, album):
        print(album.name, album.numberOfSongs, album.artist.id)
        self.cur.execute('''INSERT INTO Album (name, numberOfSongs, artist_id) VALUES (?, ?, ?)''',
                         (album.name, album.numberOfSongs, album.artist.id))
        self.conn.commit()

    def get_artist_by_id(self, artist_id):
        art = None
        self.cur.execute('''
              SELECT * FROM Artist WHERE id = ?
          ''', (artist_id,))
        artist = self.cur.fetchone()
        if artist:
            artist_id, name, genre = artist
            print(f"Artist ID: {artist_id}")
            print(f"Name: {name}")
            print(f"Genre: {(genre)}")

            # Fetch albums of the artist
            self.cur.execute('''
                  SELECT * FROM Album WHERE artist_id = ?
              ''', (artist_id,))
            albums = self.cur.fetchall()
            if albums:
                print("Albums:")
                for album in albums:
                    id, name, number_of_songs, artist_id = album
                    print(f"  - {name} (ID: {id}, Number of Songs: {number_of_songs})")

            else:
                print("This artist has no albums.")
            art = Artist(name, artist_id, albums, genre)
        else:
            print("Artist not found.")

        return art

    def get_album_by_id(self, album_id):
        self.cur.execute('''SELECT * FROM Album WHERE id=?''', (album_id,))
        album = self.cur.fetchone()

        if album:
            id, name, number_of_songs, artist_id = album
            print(f"Name: {name}")
            print(f"Number of songs: {(number_of_songs)}")
        else:
            raise ElementNotFoundException("Album not found")

    def update_artist(self, id, name):
        self.cur.execute('''UPDATE Artist SET name=? WHERE id=?''', (name, id))
        self.conn.commit()

    def update_album(self, id, name, numberOfSongs):
        self.cur.execute('''UPDATE Album SET name=?, numberOfSongs=? WHERE id=?''', (name, numberOfSongs, id))
        self.conn.commit()

    def delete_artist(self, id):
        self.cur.execute('''
                  SELECT id FROM albums WHERE artist_id = ?
              ''', (id,))
        albums_to_delete = self.cursor.fetchall()


        for album_id in albums_to_delete:
            self.delete_album(album_id[0])

        # Delete the artist
        self.cur.execute('''
                  DELETE FROM artists WHERE id = ?
              ''', (id,))
        self.conn.commit()
        print("Artist and associated albums deleted successfully.")

    def delete_album(self, id):
        self.cur.execute('''DELETE FROM Album WHERE id=?''', (id,))
        self.conn.commit()




    def close(self):
        self.conn.close()
