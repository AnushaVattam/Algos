def maxSubArray(ls):
    count1 = 0
    count2 = 0
    if len(ls) == 0:
       raise Exception("Array empty") # should be non-empty
      
    runSum = maxSum = ls[0]
    i = 0
    start = finish = 0

    for j in range(1, len(ls)):
        if ls[j] > (runSum + ls[j]):
            runSum = ls[j]
            i = j
        else:
            runSum += ls[j]
            
        count1 = count1 + 1

        if runSum > maxSum:
            maxSum = runSum
            start = i
            finish = j
            count2 = count2 + 1
            
    print ("Original Array :=> ", ls)
    print ("maxSum of the sub_array :=> ", maxSum)
    print ("starting interval of the max sub array => ", start, "; Ending interval of the max sub array => ", finish)
    print ("Actual Count time complexity: ", count1+count2)
    print ("\n")
    
print ("These are the values form Stocks analysis which is Text referenced")    
maxSubArray([13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7])

print ("Remaining inputs:")
print ("\n")

import random

ls = []
ls_count =0

while ls_count < 21:
  number=random.randint(-100,100)
  if number not in ls:
     ls.append(number)
     ls_count += 1


#print(ls)
maxSubArray(ls)


import random

ls = []
ls_count =0

while ls_count < 26:
  number=random.randint(-100,100)
  if number not in ls:
     ls.append(number)
     ls_count += 1


#print(ls)
maxSubArray(ls)

import random

ls = []
ls_count =0

while ls_count < 36:
  number=random.randint(-100,100)
  if number not in ls:
     ls.append(number)
     ls_count += 1


#print(ls)
maxSubArray(ls)

import random

ls = []
ls_count =0

while ls_count < 46:
  number=random.randint(-100,100)
  if number not in ls:
     ls.append(number)
     ls_count += 1



#print(ls)
maxSubArray(ls)

import random

ls = []
ls_count =0

while ls_count < 56:
  number=random.randint(-100,100)
  if number not in ls:
     ls.append(number)
     ls_count += 1



#print(ls)
maxSubArray(ls)
