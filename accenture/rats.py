def rats(r, unit, arr, n):
    consumption = r * unit
    no_of_houses = 0
    house_food = 0

    if len(arr) == 0 or len(arr) != n:
        return -1
    
    i = 0
    while i < n:

        if house_food < consumption:
            house_food += arr[i]
            no_of_houses += 1
        if house_food >= consumption:
            return no_of_houses
        
        i += 1

    return 0


compute = rats(7, 2, [], 3)
print(compute)