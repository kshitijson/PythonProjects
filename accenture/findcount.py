def find_count(arr, n, num, diff):

    no_of_eles = 0
    i=0
    while i < n:
        if abs(num - arr[i]) <= diff:
            no_of_eles += 1

        i += 1
        
    if no_of_eles == 0:
        return -1
    else:
        return no_of_eles
    
arr = [12, 3, 14, 56, 77, 13]
compute = find_count(arr, len(arr), 13, 2)
print(compute)