#data from milion songs challenge

from numpy.ma.core import empty
from bitarray import bitarray
import pandas as pd
from random import randint
import mmh3

class BloomFilter:
  def __init__(self, N, K):
    self.S = bitarray(N)
    for _ in self.S:
      _ = 0
    self.N = N
    self.K = K
  def update(self, el):
    for i in range(self.K):
      self.S[mmh3.hash(el, i)%self.N]=1
  def check(self, el):
    for i in range(self.K):
      if not self.S[mmh3.hash(el, i) % self.N]:
        return 0
    return 1

artist_name = "Hudson Mohawke"
song_list = []
for i in range(10):
  if artistmxmid["Warren Zevon"][i] in songs:
    song_list.append(songs[artistmxmid["Warren Zevon"][i]])
    song_list[i] = song_list[i][0:10]
    print(song_list[i])
    print(artistmxmid["Warren Zevon"][i])
  else:
    i-=1

bf = BloomFilter(len(songs), 1000)
for s in song_list:
  for w in s:
    bf.update(w)

list_of_similar_songs = []
for s in songs:
  song_text = songs[s]
  f = 1
  #if len(song_text) < 5:
   # continue
  for w in song_text[0:10]:
    if bf.check(w) == 0:
      f = 0
      break
  if f == 1 and s not in artistmxmid["Warren Zevon"]:
    list_of_similar_songs.append(s)

print(len(list_of_similar_songs))
for f in list_of_similar_songs:
  print(f"id:{f} text:{songs[f][0:10]}")
