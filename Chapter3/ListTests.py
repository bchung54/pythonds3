"""
Programming Exercises 3.11:
1. Devise an experiment to verify that the list index operator is O(1)
2. Devise an experiment to verify that get item and set item are O(1) for dictionaries.
3. Devise an experiment that compares the performance of the del operator on lists and dictionaries.
4. Given a list of numbers in random order, write an algorithm that works in O(nlog(n)) to find the kth smallest number in the list.
5. Can you improve the algorithm from the previous problem to be linear? Explain.
"""

import timeit
import random



#1. Devise an experiment to verify that the list index operator is O(1)

"""
print(f"{'length':10s}{'index':>10s}{'time':>10s}")
for i in range(5):
    list_length = 100 * 10 ** i
    lst = list(range(list_length))
    for j in range(0, list_length, list_length // 5):
        t = timeit.Timer(f"lst[{j}]", "from __main__ import lst")
        print(f"{list_length:<10,}{j:>10.1f}{t.timeit(number=1000):>10.6f}")

Results:
length         index      time
100             0.00  0.000015
100            20.00  0.000015
100            40.00  0.000015
100            60.00  0.000015
100            80.00  0.000015
1000            0.00  0.000014
1000          200.00  0.000015
1000          400.00  0.000014
1000          600.00  0.000014
1000          800.00  0.000014
10000           0.00  0.000015
10000        2000.00  0.000014
10000        4000.00  0.000014
10000        6000.00  0.000014
10000        8000.00  0.000014
100000          0.00  0.000015
100000      20000.00  0.000014
100000      40000.00  0.000014
100000      60000.00  0.000014
100000      80000.00  0.000014
1000000         0.00  0.000015
1000000    200000.00  0.000015
1000000    400000.00  0.000015
1000000    600000.00  0.000015
1000000    800000.00  0.000015        
"""

#2. Devise an experiment to verify that get item and set item are O(1) for dictionaries.

"""
print(f"{'n':10s}{'get':>10s}{'set':>10s}")
for i in range(6):
    dict_length = 100 * 10 ** i
    x = {j: None for j in range(dict_length)}
    rand = random.randrange(dict_length)
    get = timeit.Timer(f"x.get(rand)", "from __main__ import x, rand")
    set = timeit.Timer(f"x[rand] = 1", "from __main__ import x, rand")
    get_time = get.timeit(number=1000)
    set_time = set.timeit(number=1000)
    print(f"{dict_length:<10,}{get_time:>10.5f}{set_time:>10.5f}")

Results
n                get       set
100          0.00005   0.00002
1,000        0.00006   0.00003
10,000       0.00006   0.00003
100,000      0.00006   0.00003
1,000,000    0.00006   0.00003
10,000,000   0.00006   0.00003
"""

#3. Devise an experiment that compares the performance of the del operator on lists and dictionaries.

"""
print(f"{'length':10s}{'dictionary':>10s}{'list':>10s}")
for i in range(7):
    length = 10 * 10 ** i
    d = {k: None for k in range(length)}
    l = list(range(length))
    rand = random.randrange(length)

    d_timer = timeit.Timer(f"del d[rand]", "from __main__ import d, rand")
    l_timer = timeit.Timer(f"del l[rand]", "from __main__ import l, rand")
    d_time = d_timer.timeit(number=1)
    l_time = l_timer.timeit(number=1)
    print(f"{length:<10,}{d_time:>10.6f}{l_time:>10.6f}")

Results:
length    dictionary      list
10          0.000001  0.000000
100         0.000000  0.000000
1,000       0.000001  0.000000
10,000      0.000001  0.000001
100,000     0.000002  0.000007
1,000,000   0.000002  0.000262
10,000,000  0.000002  0.004489
"""

#4. Given a list of numbers in random order, write an algorithm that works in O(nlog(n)) to find the kth smallest number in the list.

"""
def get_ksmall(lst, k):
    lst.sort()
    return lst[k-1]

print(f"{'Length':10s}{'Time (ms)':>15s}")
for i in range(7):
    length = 10 ** i
    lst = list(range(length))
    random.shuffle(lst)
    k = random.randrange(length)
    k_time = timeit.Timer(f"get_ksmall(lst, k)", "from __main__ import lst, k, get_ksmall")
    print(f"{length:<10.0f}{k_time.timeit(number=1000):>15.4f}")

Result:
Length          Time (ms)
1                  0.0001
10                 0.0002
100                0.0008
1000               0.0064
10000              0.0638
100000             0.6505
1000000            6.7588
"""

#5. Can you improve the algorithm from the previous problem to be linear? Explain.
"""
https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array/
Methods: RandomPartition, MinHeap, MaxHeap, Binary Search Tree
Main idea of methods is to improve sort by only sorting a small subset (usually k) and then comparing rest of data to the subset
Worst case: nlogn
Best case: n
Average: n + klogn
"""