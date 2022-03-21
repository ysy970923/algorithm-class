file = open("input.txt", 'r')
unsorted_list = file.read().split(' ')
# import random
# unsorted_list = [random.randint(-100, 100) for r in range(100000)]



def partition(start, end):
    left = []
    right = []
    pivot = unsorted_list[end]
    i = start
    while (i < end):
        if (unsorted_list[i] <= pivot):
            left.append(unsorted_list[i])
        else:
            right.append(unsorted_list[i])
        i += 1
    unsorted_list[start:end + 1] = left + [pivot] + right
    return start + len(left)


def quick_sort(start, end):

    if(start < end):
        pivotIndex = partition(start, end)
        quick_sort(start, pivotIndex - 1)
        quick_sort(pivotIndex+1, end)
    return unsorted_list

# import time
# start_time = time.time()
sorted_list = quick_sort(0, len(unsorted_list) - 1)
# print("%s" % (time.time() - start_time))

