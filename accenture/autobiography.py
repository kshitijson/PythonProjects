""" def autobio(str1):
     """

str1 = "1210"
main_arr = []
count_arr = []

for i in str1:
    main_arr.append(int(i))

for i in range(0, len(str1)):
    count_arr.append(0)

for ele in main_arr:
    count_arr[ele] += 1

if main_arr == count_arr:
    print("Autobio")
    count_arr.sort()
    i=0
    while i < len(main_arr)-1:
        if count_arr[i] == count_arr[i+1]:
            
        i += 1

print(count_arr)
            
