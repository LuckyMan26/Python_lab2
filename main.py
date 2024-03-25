# This is a sample Python script.
from musicstoredb import MusicStoreDB
from utils import Album, Artist, Genre

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   db_file = 'musicstore.db'
   music_store_db = MusicStoreDB(db_file)

   artist = Artist("Eminem", 1, [], Genre.RAP)
   music_store_db.add_artist(artist)

   album = Album("The Marshall Mathers LP", 1, 18)
   album.artist = artist
   music_store_db.add_album(album)

   retrieved_artist = music_store_db.get_artist_by_id(1)
   retrieved_album = music_store_db.get_album_by_id(1)


   music_store_db.update_artist(1, "Eminem Updated")
   music_store_db.update_album(1, "The Marshall Mathers LP Updated", 20)
   music_store_db.get_artist_by_id(1)
   music_store_db.get_album_by_id(1)


   music_store_db.delete_artist(1)
   music_store_db.delete_album(1)

   music_store_db.close()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
