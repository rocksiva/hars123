def largest(arr,t): 
    max = arr[0] 
    for i in range(1, t): 
        if arr[i] > max: 
            max = arr[i] 
    return max
arr = [10, 324, 45, 90, 9808] 
t= len(arr) 
Ans = largest(arr,t) 
print ("Largest in given array is",Ans) 
