import string
count = 0
d =dict()
d1=dict()
fil1 = open("58820-0.txt")
for line in fil1:
    line = line.strip()
    line = line.lower()
    line = line.split()
    for word in line:
       print(word.strip(string.punctuation))
       count = count +1
       if word not in d:
         d[word] = 1
       else:
         d[word] += 1
print(count)
fil2 = open("58809-0.txt")
for line in fil2:
    line = line.strip()
    line = line.lower()
    line = line.split()
    for word in line:
       print(word.strip(string.punctuation))
       count = count +1
       if word not in d1:
          d1[word] = 1
       else:
          d1[word] += 1
print(count)
print(len(d))
print(len(d1))
if len(d)>len(d1):
   print("first book is extensive")
else:
   print("second book is extensive")
for k in d.keys():
  if d[k]>20:
    print(k)
for k in d1.keys():
  if d1[k]>20:
    print(k)

