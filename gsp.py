from collections import Counter
from itertools import combinations
from collections import defaultdict
import numpy as np

tdb = [[['a', 'b'], ['c'], ['f', 'g'], ['g'], ['e']],
       [['a', 'd'], ['c'], ['b'], ['a', 'b', 'e', 'f']],
       [['a'], ['b'], ['f', 'g'], ['e']],
       [['b'], ['f', 'g']]]

min_sup = 2
n = 0

lst_items = []
for i in tdb:
  for j in i:
      for k in j:
          if(k not in lst_items):
              lst_items.append(k)
lst_items = sorted(lst_items)
print(lst_items)

c = Counter()
for i in lst_items:
    for d in tdb:
        for item in d:
            if(set(i).issubset(set(item))):
                c[tuple(i)]+=1
                break
print(c)

l = Counter()
lst_items = []
for i in c:
  if(c[i] >= min_sup):
    l[i]=c[i]
    lst_items.append(i)
print(lst_items)
print(l)

poss = defaultdict(list)
for i in range(0, len(lst_items)):
  poss[lst_items[i][0:n]].append(lst_items[i][n])
print(poss)

lst_items=[]
for i in poss:
  temp_C = combinations(poss[i], 2)
  temp_lst_items = list(temp_C)
  if temp_lst_items:
    for j in temp_lst_items:
      lst_j = list(j)
      lst_j.extend(list(i))
      lst_items.append(sorted(lst_j))
print(lst_items)

m1 = Counter()
m2 = Counter()
m1_bool = False
m2_bool = False
for i in lst_items:
    for d in tdb:
        for item in d:
            if (set(i).issubset(set(item))):
                m1[tuple(i)]+=1
            if (set(i[0]).issubset(item)):
                m1_bool = True
            if (set(i[1]).issubset(item)):
                m2_bool = True
            if (m1_bool and set(i[1]).issubset(item) and not set(i[0]).issubset(item)):
                m2[tuple(i)]+=1
                m1_bool = False
            if (m2_bool and set(i[0]).issubset(item) and not set(i[1]).issubset(item)):
                j = i[::-1]
                m2[tuple(j)]+=1
                m2_bool = False
        m1_bool = False
        m2_bool = False
print(m1)
print(m2)

l = Counter()
lst_items = []
for i in m1:
  if(m1[i] >= min_sup):
    l[i]=m1[i]
    lst_items.append(list([i]))
for i in m2:
  if(m2[i] >= min_sup):
    l[i]=m2[i]
    lst_items.append(i)
print(l)
print(lst_items)

n = n+1
cnt_lst = 0
for i in range(0, len(lst_items)):
    if (type(lst_items[i])==list):
        cnt_lst +=1
        
new_list = []
for i in range(0, len(lst_items)):
    if (type(lst_items[i])==list):
        for j in range(cnt_lst, len(lst_items)):
            if(str(lst_items[i][0][1:n+1])==str(lst_items[j][:-1])):
                tmp_lst = list([lst_items[i][0]])
                char = list(lst_items[j][n])
                tmp_lst.append(char)
                new_list.append(tmp_lst)
    elif (type(lst_items[i])==tuple):
        for j in range(i+1, len(lst_items)):
            if(str(lst_items[i][1:n+1])==str(lst_items[j][:-1])):
                tmp_lst = list(lst_items[i])
                char = lst_items[j][n]
                tmp_lst.append(char)
                new_list.append(tmp_lst)
        for j in range(0, cnt_lst):
            if(str(lst_items[i][1:n+1])==str(lst_items[j][0][:-1])):
                char = list(list(lst_items[i][0]))
                tmp_lst = list(lst_items[j][0])
                char.append(tmp_lst)
                new_list.append(char)
print(new_list)

