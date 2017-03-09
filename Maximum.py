def maxSubArray(a):
    a = []
    n = int(input("\n Enter number of values : "))
    import random
    a = [ x for x in range(n) ]
    x = print(random.randint(-30,-20))
    
    
    if len(a) == 0:
        raise Exception("Array empty") # should be non-empty

    runSum = maxSum = a[0]
    i = 0
    start = finish = 0

    for j in range(1, len(a)):
        if a[j] > (runSum + a[j]):
            runSum = a[j]
            i = j
        else:
            runSum += a[j]

        if runSum > maxSum:
            maxSum = runSum
            start = i
            finish = j
            
    print ("Original Array", a)
    print ("start =>", start)
    print ("finish =>", finish)
    print ("maxSum =>", maxSum)
    
#maxSubArray([a])
#maxSubArray([-2, 0, -4, 13, -5, 2])
#maxSubArray([-15, 0, -36, 3, -22, 11, 19, -5])
#maxSubArray([-15, 29, -36, 3, -22, 11, 19, -5])
maxSubArray([-15, 29, -36, 3, -22, 11, 19, -5, -20 ,10,-15])

