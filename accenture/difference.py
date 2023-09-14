def differneceofSum(m, n):

    divisible = 0
    not_divisible = 0
    for i in range(1, m+1):
        if i % n == 0:
            divisible += i
        else:
            not_divisible += i
    
    return not_divisible - divisible

compute = differneceofSum(20, 4)
print(compute)