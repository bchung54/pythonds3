from pythonds3.basic import Queue
import random


def hot_potato(name_list, num):
    sim_queue = Queue()

    #Removed due to Programming Exercise 4.27.9
    #for name in name_list:
    #    sim_queue.enqueue(name)
    
    #Programming Exercise 4.27.9
    for _ in range(len(name_list)):
        #Randomizes order of player queue
        next_pick = name_list[random.randrange(0,len(name_list))]
        sim_queue.enqueue(next_pick)
        name_list.remove(next_pick)
    
    while sim_queue.size() > 1:
        for i in range(num):
            sim_queue.enqueue(sim_queue.dequeue())

        sim_queue.dequeue()

    return sim_queue.dequeue()


print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))
