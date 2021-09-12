def highest_rank(arr):
    highest = 0
    highest_key = None
    num_map = {}
    for val in arr:
        if val in num_map:
            num_map[val] = int(num_map[val]) + 1
        else:
            num_map[val] = 1
    print(num_map)
    for key, num in num_map.items():
        print(highest_key, key, num)
        if num >= highest:
            if int(key) > int(highest_key):
                highest = num
                highest_key = key
            else: pass
    return highest_key



# tests
print(highest_rank([12, 10, 8, 7, 6, 4, 12, 12, 10, 8, 10, 12, 7, 6, 4, 8, 12, 7, 6, 4, 10, 10, 12, 12, 12, 10, 8, 12, 7, 6, 4, 10, 10, 12, 10, 8, 12, 7, 6, 4, 10, 10, 8, 12, 7, 6, 4, 10, 10, 12, 12, 10]))
print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 10, 12]))