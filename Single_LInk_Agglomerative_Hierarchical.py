nums = [2, 1, 4, 10, 21, 3, 9, 14, 7]

start = 1
for i in range(0, len(nums)):
    for j in range(start, len(nums)):
        print(j)
        if nums[j] < nums[i]:
            nums[i], nums[j] = nums[j], nums[i]
            start += 1
    print('---------------------')
print(nums)



