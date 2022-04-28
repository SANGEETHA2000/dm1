from collections import Counter
from itertools import combinations
from collections import defaultdict
import numpy as np

def genC(lst_items, tdb):
    c = Counter()
    for i in lst_items:
        for d in tdb:
            if(set(i).issubset(set(d))):
                c[tuple(i)]+=1
    return c
      
def genL(c, min_sup):
    l = Counter()
    lst_items = []
    for i in c:
      if(c[i] >= min_sup):
        l[i]=c[i]
        lst_items.append(i)
    return lst_items, l

if __name__ == "__main__":
    tdb = [['1', '2', '5'], ['2', '4'], ['2', '3'], ['1', '2', '4'], ['1', '3'], ['2', '3'], ['1', '3'], ['1', '2', '3', '5'], ['1', '2', '3']]
    #tdb = [['A', 'C', 'D'], ['B', 'C', 'E'], ['A', 'B', 'C', 'E'], ['B', 'E']]
    min_sup = 2
    n=0
    mn=0
    
    lst_items = []
    for i in tdb:
      for j in i:
        if(j not in lst_items):
          lst_items.append(j)
    lst_items = sorted(lst_items)
    
    while(len(lst_items)>=1):
        c = genC(lst_items, tdb)
        print("C"+str(n+1)+": ")
        for i in c:
            print(str([i])+": "+str(c[i]))
        
        lst_items = []
        lst_items, l = genL(c, min_sup)
        if len(l)!=0:
            prev_l = l
            mn = n
        print("L"+str(n+1)+": ")
        for i in l:
            print(str([i])+": "+str(l[i]))

        print(lst_items)
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
        n = n+1
        
    print("\n"+str(mn+1)+"-frequent item set:")
    for i in prev_l:
        print("\n" + str([i])+": "+str(prev_l[i]))
        for j in range(0, mn+1):
            lst_A = list(i[j])
            lst_B = np.setdiff1d(list(i),lst_A)
            cnt_lst_A = genC(lst_A, tdb)
            for k in cnt_lst_A:
                print(str(lst_A)+ "=>" + str(lst_B) + ": " + str(prev_l[i]/cnt_lst_A[k]))
            cnt_lst_B = genC(list([lst_B]), tdb)
            for k in cnt_lst_B:
                print(str(lst_B)+ "=>" + str(lst_A) + ": " + str(prev_l[i]/cnt_lst_B[k]))
        