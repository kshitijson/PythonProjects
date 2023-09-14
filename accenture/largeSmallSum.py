def large_small_sum(arr):

    if len(arr) <= 3:
        return 0
    
    even_arr = []
    odd_arr = []

    
    for i in range(0, len(arr)):
        if i % 2 == 0:
            even_arr.append(arr[i])
        else:
            odd_arr.append(arr[i])
    
    even_arr.sort()
    odd_arr.sort()

    return even_arr[-2] + odd_arr[1]

compute = large_small_sum([])
print(compute)

#3, 1, 5 ----> 1 3 5
##2, 7, 4 ----> 2 4 7  ----------------> 7



# 1 2 5 7 2 3 5