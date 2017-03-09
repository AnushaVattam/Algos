n = int(input("\n Enter number of values "))

count =0
a = []
for i in range(n):
    t = int(input("\n Enter Value "))
    a.append(t)

print("\n MergeSort Unsorted data input :",a)


def merge_sort(a):
    merge_sort1(a,0,len(a)-1)


def merge_sort1(a,first,last):
 if first < last:
    middle = (first+last)//2
    merge_sort1(a, first, middle)
    merge_sort1(a, middle+1, last)
    merge(a,first, middle, last)

def merge(a, first, middle, last):
     global count
     
     l = a[first:middle]
     r = a[middle+1:last+1]
     l.append(99999999999)
     r.append(99999999999)
     i = 0
     j = 0
     k = first
     while k <= last:
      if l[i] <= r[j]:
        a[k] = l[i]
        i =i+1
      else:
        a[k] = r[j]
        j =j+1
                
        k =k+1
		
                
                        
merge_sort(a)               
print("\n Mergesort sorted output :",a)

print("\n Actual count:", count)
                    
