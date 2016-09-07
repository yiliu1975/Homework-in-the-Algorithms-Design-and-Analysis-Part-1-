# mergesortt algorithm
# Yi Liu, 09/2016
# random select pivot element

import random  # import random.py


array = []
# read from mergesort.txt
file = open('quicksort.txt')
for line in file.read().split():
    array.append(int(line))
file.close()

# array = [5,3,2,4,1,9,6,7,8,10,11]

counter = 0 # comparison number
    
comparison = 0 # comparison number    
    
def quicksort(lst): 
   if len(lst) < 2:
       return lst
   return partition(lst)


def partition(lst):  
   global counter 
   left = []
   right = []
   global comparison #comparison number
   sortedarray = []   
   k = random.randint(0,len(lst)-1) #pivot number
   i = 0
   j = k+1
   
   while i < k:
       if lst[i]<lst[k]:
          left.append(lst[i])
       else: right.append(lst[i])
       i += 1
    
   while k < j <len(lst):
       if lst[j]<lst[k]:
          left.append(lst[j])
       else: right.append(lst[j])
       j += 1
       
   counter += len(left) + len(right)
       
   leftsorted = quicksort(left)
   rightsorted = quicksort(right)
   
   sortedarray = leftsorted
   
   sortedarray.append(lst[k])
   sortedarray.extend(rightsorted)
       
   return sortedarray
   
print quicksort(array)
print 'counter = ', counter