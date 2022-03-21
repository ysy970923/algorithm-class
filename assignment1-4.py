file = open("input.txt", 'r')
unsorted_list = file.read().split(' ')
# import random
# unsorted_list = [random.randint(-100, 100) for r in range(100000)]

print(unsorted_list)


def merge(start, middle, end):
    i = start
    j = middle + 1
    sorted_list = []
    while((i <= middle) & (j <= end)):
        if(unsorted_list[i] <= unsorted_list[j]):
            sorted_list.append(unsorted_list[i])
            i += 1
        else:
            sorted_list.append(unsorted_list[j])
            j += 1
    if(i > middle):
        while(j <= end):
            sorted_list.append(unsorted_list[j])
            j += 1
    elif(j > end):
        while(i <= middle):
            sorted_list.append(unsorted_list[i])
            i += 1
    unsorted_list[start:end+1] = sorted_list


def merge_sort(start, end):
    if(start != end):
        middle = int((start + end) / 2)
        merge_sort(start, middle)
        merge_sort(middle + 1, end)
        merge(start, middle, end)

    return unsorted_list

# import time
# start_time = time.time()
sorted_list = merge_sort(0, len(unsorted_list) - 1)
# print("%s" % (time.time() - start_time))

print(sorted_list)
