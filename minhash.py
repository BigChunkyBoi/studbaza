import numpy as np
import random

def chs(a,b,p,N,x):
  return ((a*x + b)%p)%N

alist = []
blist = []
for i in range(0,100):
  a = random.randint(1,10000)
  b = random.randint(1,10000)
  while a in alist:
    a = random.randint(1,10000)
  while b in blist:
    b = random.randint(1,10000)
  alist.append(a)
  blist.append(b)

shinglet_size = 2
songs_shinglets = {}
shingles_x_documents = {}
test = 0
for s in songs.keys():
  shinglet = []
  for j in range(len(songs[s])-shinglet_size):
    x = ''.join(songs[s][j:j+shinglet_size])
    shinglet.append(x)
    if x in shingles_x_documents:
      shingles_x_documents[x].append(s)
    else:
      shingles_x_documents[x] = []
      shingles_x_documents[x].append(s)
  songs_shinglets[s] = shinglet


signatures = {}
NN = len(shingles_x_documents)
for i in range(100):
  signatures[i] = [15000067 for i in range(len(songs_shinglets))]
h_i = [0 for _ in range(100)]
row = 0
songs_s = {}
index = 0
for s in songs_shinglets:
  songs_s[s]=index
  index+=1

for w in shingles_x_documents:
  #print(row)
  for i in range(100):
      h_i[i]=chs(a=alist[i], b=blist[i], p=15000067, N=NN, x=row+1)
  for s in shingles_x_documents[w]:
    for i in range(100):
      if signatures[i][songs_s[s]] > h_i[i]:
        signatures[i][songs_s[s]] = h_i[i]
  row += 1

songxsignature = {}
index = 0
for s in songs_shinglets:
  songs_s[s]=index
  index+=1
for s in songs_s:
  songxsignature[s] = []
  for i in range(100):
    songxsignature[s].append(signatures[i][songs_s[s]])
print(songxsignature["4623710"])

hashforoursong = {}
r = 5
b = 20
i = 0
j = 0
while i < 100:
  x = songxsignature['1485485'][i:i+r]
  z = ''
  for w in x:
    z+=str(w)
  hashforoursong[z] = j
  i+=r
  j+=1
print(hashforoursong)
inbucketwithoursong = []
print(len(songxsignature))
for s in songxsignature:
  i = 0
  while i < 100:
    x = songxsignature[s][i:i+r]
    z = ''
    for w in x:
      z+=str(w)
    if z in hashforoursong:
      inbucketwithoursong.append(s)
      break
    i+=r

print(len(inbucketwithoursong))
