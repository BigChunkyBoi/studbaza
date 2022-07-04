import math
import csv
path = '/content/drive/MyDrive/coolabdata/tags.csv'
users = {}
users_tag = {}
users_movies_jac = {}
movies = {}
movies_tag = {}
tags = {}
treshhold = 1
i = 0
frequent_tags = []
#zebranie tagów oraz ilości ich wystąpień

def jaccard(l1,l2):
  if type(l1) != set:
    l1 = set(l1)
    l2 = set(l2)
  return len(l1.intersection(l2))/len(l1.union(l2))

with open(path) as file:
  heading = next(file)
  reader_obj = csv.reader(file)
  for row in reader_obj:
    if row[2] not in tags.keys():
      tags[row[2]] = 0
    tags[row[2]] += 1
#stworzenie tablicy zawierającej tagi powyżej 2000 wystąpień
for t in tags:
  if tags[t] > 2000:
    frequent_tags.append(t)


user_watched = {} #lista filmów obejrzanych przez użytkownika
#pętla w której sprawdzamy tagi dane przez użytkownika oraz tagi filmu

with open(path) as file:
  heading = next(file)
  reader_obj = csv.reader(file)
  for row in reader_obj:
    if row[0] not in users.keys():
      users[row[0]] = []
      users_tag[row[0]] = {}
      user_watched[row[0]] = {}
      for f in frequent_tags:
          users[row[0]].append(0) #storzenie wektora user:[0,0,0,0,0....0] w ilosci rozmiaru frequent_tags
    if row[1] not in movies.keys():
      movies[row[1]] = []
      movies_tag[row[1]] = {}
      for f in frequent_tags:
          movies[row[1]].append(0) #to samo co wyżej dla filmów
    if row[2] in frequent_tags:
      for f in frequent_tags:
        if f == row[2]:
          users_tag[row[0]][row[2]] = 1
          movies_tag[row[1]][row[2]] = 1
          user_watched[row[0]][row[1]] = 1


j = 0
n = len(frequent_tags)
#for u in users.keys():

def forUser(us):
  u = users[us]
  #print(u)
  users_movies_jac[us] = {}
  for m in movies.keys():
    users_movies_jac[us][m] = jaccard(users_tag[us].keys(), movies_tag[m].keys())
  #print(users_movies_index)

  film_list = []
  u_watched = user_watched[us].keys()
  print(u_watched)
  print(f"Tagi uzytkownika: {users_tag[us].keys()}")
  for i in range(0,5):
    max = 0
    film = ''
    for l in users_movies_jac[us]:
      #print(l)
      if l not in film_list and l not in u_watched:
        if max < users_movies_jac[us][l]:
          max = users_movies_jac[us][l]
          film = l
    film_list.append(film)
    print(f"film: {film} jaccard: {users_movies_jac[us][film]} tagi: {movies_tag[film].keys()}")

forUser("17348")
forUser("3")
