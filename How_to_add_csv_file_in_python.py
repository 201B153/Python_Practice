#direct method

import csv
filename = "std_record.csv"

with open(filename, "r") as data:
  for line in csv.reader(data):
      print(line)


# another method:


from pandas import *
df = read_csv('std_record.csv')
df.head(4)      
df.tail(4)
