file = open("input.txt", 'r')
unsorted_list = file.read().split(' ')

# import time
# import random
# unsorted_list = [random.randint(-100, 100) for r in range(100000)]
# start_time = time.time()



def get_min_index(list):
    minVal = list[0]
    minIndex = 0
    for i in range(len(list)):
        if(list[i] < minVal):
            minVal = list[i]
            minIndex = i
    return minIndex


def selection_sort(unsorted_list):
    for i in range(len(unsorted_list) - 1):
        minIndex = get_min_index(unsorted_list[i:len(unsorted_list)])
        temp = unsorted_list[i]
        unsorted_list[i] = unsorted_list[i+minIndex]
        unsorted_list[i+minIndex] = temp
        print(unsorted_list)

    return unsorted_list


sorted_list = selection_sort(unsorted_list)
# print("%s" % (time.time() - start_time))

