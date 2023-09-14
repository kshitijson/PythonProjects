def operation(str1):
    if len(str1) == 0:
        return -1
    
    result = int(str1[0])

    i = 1
    while i < len(str1):

        if str1[i] == "A":
            result &= int(str1[i+1])
        elif str1[i] == "B":
            result |= int(str1[i+1])
        elif str1[i] == "C":
            result ^= int(str1[i+1])

        i += 2
    
    return result

compute = operation("")
print(compute)

    