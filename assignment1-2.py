file = open("input.txt", 'r')
unsorted_list = file.read().split(' ')

# import time
# import random
# unsorted_list = [random.randint(-100, 100) for r in range(100000)]
# start_time = time.time()


def bubble_sort(unsorted_list):
    for i in range(1, len(unsorted_list)):
        for j in range(len(unsorted_list) - i):
            if(unsorted_list[j] > unsorted_list[j+1]):
                temp = unsorted_list[j]
                unsorted_list[j] = unsorted_list[j+1]
                unsorted_list[j+1] = temp
                print(unsorted_list)

    return unsorted_list

sorted_list = bubble_sort(unsorted_list)
# print("%s" % (time.time() - start_time))
