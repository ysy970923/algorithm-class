file = open("input.txt", 'r')
unsorted_list = file.read().split(' ')
# import time
# import random
# unsorted_list = [random.randint(-100, 100) for r in range(100000)]


# start_time = time.time()


def insertion_sort(unsorted_list):
    for j in range(1, len(unsorted_list)):
        key = unsorted_list[j]
        i = j - 1
        while i >= 0 and unsorted_list[i] > key:
            unsorted_list[i+1] = unsorted_list[i]
            i = i-1
        unsorted_list[i+1] = key
        print(unsorted_list);
    return unsorted_list


sorted_list = insertion_sort(unsorted_list)
# print("%s" % (time.time() - start_time))