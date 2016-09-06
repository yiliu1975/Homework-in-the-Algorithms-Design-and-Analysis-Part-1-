# mergesortt algorithm
# Yi Liu, 09/2016

#array = [3,5,6,9,1,2,7,4,8]
array = []
# read from mergesort.txt
file = open('mergesort.txt')
for line in file.read().split():
    array.append(int(line))
file.close()
    
inv = 0 # inversion number    
    
# merge left and right arrays
def merge(left, right):  
   i = 0
   j = 0
   global inv
   combined = []   # merged results
   while i < len(left) and j < len(right): # iterate until merge is complete
       if left[i] < right [j]:
           combined.append(left[i])
           i +=1
       else:
           combined.append(right[j])
           j +=1
           inv += len(left)-i 
   combined.extend(left[i:])  #add all remaining element to the list
   combined.extend(right[j:])
   return combined

# break array   
def divide(lst):
    if len(lst) > 1:
        left = divide(lst[:len(lst)/2])
        right = divide(lst[len(lst)/2:])
        return merge(left, right)
    else: return lst

print divide(array)
print 'Inversion number =', inv