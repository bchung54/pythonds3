import Queue
import random


def radix_sort(lst):
    #Takes a list of strings that represent numbers with the same length and radix sorts them

    main_queue = Queue.Queue()
    bin_list = [Queue.Queue() for i in range(10)]
    digits = len(lst[0])

    #initialize queue
    for num in lst:
        main_queue.enqueue(num)

    for digits_place in range(digits):
        while not main_queue.is_empty():
            current = main_queue.dequeue()
            bin_list[int(current[-digits_place - 1])].enqueue(current)
        for bin in bin_list:
            while not bin.is_empty():
                main_queue.enqueue(bin.dequeue())
    
    return main_queue

if __name__ == '__main__':
    list_to_sort = [str(random.randrange(1000, 10000)) for i in range(10)]
    sorted = radix_sort(list_to_sort)
    while not sorted.is_empty():
        print(sorted.dequeue())