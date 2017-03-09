n = int(input("\n Enter number of values "))
a = []

count = 0
for i in range(n):
    t = int(input(" Enter Value "))
    a.append(t)

print("\n Unsorted data input ",a)

def mergesort( a ):
  _mergesort( a, 0, len( a ) - 1 )
 

def _mergesort( a, first, last ):
  global count = 0
  # break problem into smaller structurally identical pieces
  mid = ( first + last ) // 2

  if first < last:
    _mergesort( a, first, mid )
    _mergesort( a, mid + 1, last )
 
  # merge solved pieces to get solution to original problem
  p, f, l = 0, first, mid + 1
  tmp = [None] * ( last - first + 1 )
 
  while f <= mid and l <= last:
    
    if a[f] < a[l] :
      tmp[p] = a[f]
      f =f+1
      
    else:
      tmp[p] = a[l]
      l=l+1
      
    p =p+1
    
    count=count+1
 
  if f <= mid :
    tmp[p:] = a[f:mid + 1]
   
 
  if l <= last:
    tmp[p:] = a[l:last + 1]
    
  print("\n Merge sort sorted output:",tmp)
  p = 0
  while first <= last:
    a[first] = tmp[p]
    first =first+1
    p =p+1
   

mergesort(a)
print("\n Merge Sort sorted output:",a)

print("\n Actual Count :",count)
