test = {
    'list': [1],
    'rotated_list': [1],
    'output': 0
}

def min_num(num_list, rotated_list):
    lo, hi = 0, len(num_list) - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        print(f'lo: {lo}, hi: {hi}, mid: {mid}')

        if num_list[mid] == rotated_list[0]:
            if num_list[0] == rotated_list[0]:
                return mid
            else:
                return len(num_list) - mid
        elif num_list[mid] < rotated_list[0]:
            lo = mid + 1
        else:
            hi = mid - 1

res = min_num(test['list'], test['rotated_list'])
print(res)
print(res == test['output'])