from enum import Enum

from typing import List
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Genre(Enum):
   ROCK = 1
   RAP = 2
   POP = 3
   Classical = 4

   def __str__(self):
      return self.name


class ElementNotFoundException(Exception):
   def __str__(self):
      return "Element not found"


class Album(object):
   def __init__(self, name: str, id: int, numberOfSongs: int):
      self.id = id
      self.name = name
      self.numberOfSongs = numberOfSongs




class Artist(object):
   def __init__(self, name: str, id: int, albums: List[Album], genre: Genre):
      self.id = id
      self.name = name
      self.albums = albums
      self.genre = genre



   def hasAlbum(self, album_: Album) -> bool:
      for album in self.albums:
         if album == album_:
            return True
      return False

   def removeAlbum(self, album: Album):
      self.albums.remove(album)
   def addAlbum(self, album: Album):
      self.albums.append(album)


