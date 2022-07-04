from matplotlib import pyplot as plt
import pandas as pd

kaggle_sample = []
def hash_sample(key, b):
  return (ord(key[-1]))%b

for line in kaggle_data:
  y = []
  if hash_sample(line[0],10) == 1:
    y.append(line[0])
    y.append(int(line[2].replace('\n','')))
    kaggle_sample.append(y)

d = {}
for line in kaggle_sample:
  if line[0] not in d.keys():
    d[line[0]] = line[1]
  else:
    d[line[0]] += line[1]
#ilu użytkowników odsłuchało jakąkolwiek piosenkę n razy
print(len(d.keys()))
plt.hist(d.values(),bins=[0,100,200,300,400,500])

plt.ylabel("liczba użytkowników")
plt.xlabel("liczba odłuchań")
plt.show()
