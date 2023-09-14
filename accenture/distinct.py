def distinct(arr, n):

    if len(arr) == 0:
        return -1
    
    arr.sort()
    recur_arr = []
    
    i = 0
    while i != n-1:
        if arr[i] == arr[i+1]:
            recur_arr.append(arr[i])
        
        i += 1
    return abs(len(arr) - len(recur_arr))

arr = []
compute = distinct(arr, len(arr))
print(compute)