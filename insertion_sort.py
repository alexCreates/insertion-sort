import random
global ten_thousand_list
ten_thousand_list = []
for i in range(10001):
    num = random.randint(-10000,10000)
    ten_thousand_list.append(num)

# ^ creates a list of 10,000 numbers that range between the two params given

def insertion_sort(arr):
    for y in range(1, len(arr)):
        value = arr[y]
        i = y - 1
        while i >= 0:
            if value < arr[i]:
                arr[i+1] = arr[i]
                arr[i] = value
                i = i - 1
            else:
                break
    print arr
insertion_sort(ten_thousand_list)
