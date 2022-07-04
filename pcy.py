#Our goal here is to reduce number of pairs to feed our apriori algorithm
#TO DO//EXPLANATION

from itertools import combinations
def read_dataset(fname):
  file_iter = open(fname, 'r')
  data = []
  for line in file_iter:
    data.append(line.strip().strip(',').split(','))
  return data

def hash(p): #first hash function
  sum = 0
  for i in p:
    sum += ord(i[0])*ord(i[2])
  return sum%99
def hash2(p): #second hash function
  sum = 0
  for i in p:
    sum += ord(i[0])*ord(i[1])
  return sum%67

data = read_dataset('/content/drive/MyDrive/coolabdata/groceriesbig (1).csv') #our dataset, google drive + google colab
#just replace that with your baskets
#mine's like that cuz I've stolen it from internet. Gonna add source soon


#So you're giving file with baskets and support. k is unused
def pcy(data, k, support):
  #Counter, hash and bitmap
  supposed = {}
  map = []
  hashmap = {}
  hashmap2 = {}
  pairs = []
  c2 = {}
  for row in data: # first 'loop'
    for entry in row: #Count every item
      if entry not in supposed.keys():
        supposed[entry] = 0
      supposed[entry] += 1
    pairs = list(combinations(row,2)) #pairs
    for p in pairs: #hash
      h = hash(p)
      if h not in hashmap.keys():
        hashmap[h] = 0
      hashmap[h] += 1
  for h in hashmap: #bitmap for firsh hashmap
    if hashmap[h] > support: #treshhold
      hashmap[h] = True
    else:
      hashmap[h] = False
  #print(hashmap)
  frequentitems = [[] for _ in range(k)] #list for our frequent items sets
  #it goes like this
  #frequentitems[0] <- every item above our support
  #frequentitems[1] <- every pair above our support
  #frequentitems[2] <- every triple above our support
  #basicaly, it's L
  for entry in supposed.keys():
    if supposed[entry] >= support:
      frequentitems[0].append(set([entry]))
  for row in data: #second loop
    pairs = list(combinations(row,2))
    for p in pairs:
      h = hash(p)
      #so if every item from pair is in frequentitems[0] AND
      #value under hashmap['hash from that pair'] is above support,
      #we're doing another hashmap
      if {p[0]} in frequentitems[0] and {p[1]} in frequentitems[0]:
        if hashmap[h] == True:
          h2 = hash2(p)
          if h2 not in hashmap2.keys():
            hashmap2[h2] = 0
          hashmap2[h2]+=1
  #and another bitmap
  for h in hashmap2:
    if hashmap2[h] > support:
      hashmap2[h] = True
    else:
      hashmap2[h] = False
  #print(hashmap2)
  for row in data:
    pairs = list(combinations(row,2))
    for p in pairs:
      h = hash(p)
      h2 = hash2(p)
      #If pair in frequentitems[0] and
      #hashmap['hash1 from pair'] == 1 AND
      #hashmap2['hash2 from pair'] == 1
      if {p[0]} in frequentitems[0] and {p[1]} in frequentitems[0]:
        if hashmap[h] == True:
          if hashmap2[h2] == True: #Count pair
            if p not in c2.keys():
              c2[p]=0
            c2[p] += 1
  print(c2)
  print(len(c2))
  for c in c2:
    if c2[c] > support:
      frequentitems[1].append(c)
  print(frequentitems[1]) #replace that print with return or do your apriori below
#C2 -> L2
#bitarray

pcy(data,3,50)
