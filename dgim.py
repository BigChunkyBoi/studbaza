import random

class Bucket(object):
  def __init__(self, timestamp, sumofones):
    self.ts = timestamp
    self.sfo = sumofones

  def updateTimeStamp(self):
    self.ts += 1

  def timeStampExpired(self, N):
    if self.ts > N:
      return 1
    else:
      return 0

  def merge(self):
    self.sfo = self.sfo*2

  def getNumberOfOnes(self):
    return self.sfo

def DGIM(n,N):
  print(f"Ilosc bitow: {n}")
  print(f"Dlugosc okna: {N}")
  buckets = []
  stream = []
  for i in range(n):
    #current state of the stream
    s = random.randrange(0,9)
    if len(stream) == 0:
      stream.append(1)
    elif s % 2 == 1:
      stream.append(0)
    else:
      stream.append(1)
    #New bit arrives
    for _ in buckets:
      _.updateTimeStamp();
    if stream[i] == 1:
      b = Bucket(0,1)
      buckets.append(b)
    #check for merge
    index = 0;
    numberOfBuckets = len(buckets)
    while index < numberOfBuckets-2:
      if buckets[index].getNumberOfOnes() == buckets[index+1].getNumberOfOnes() == buckets[index+2].getNumberOfOnes():
        buckets[index+1].merge()
        buckets.pop(index)
        numberOfBuckets = len(buckets)
      else:
        index += 1
    if buckets[0].timeStampExpired(N)==1:
      buckets.pop(0)
  #print(stream)
  print(f"Liczba blokow: {len(buckets)}")
  #print(f"Maksymalny blad: {buckets[0].sfo/2} (TEORETYCZNIE)")
  #print(f"Mozliwe jedynki po za zakresem: {buckets[0].sfo-(N-buckets[0].ts)}")
  for _ in buckets:
    print(f"Suma jedynek:   {_.sfo}   czas:   {_.ts}")

DGIM(20000, 728)
DGIM(100000,1024)
DGIM(100, 32)
