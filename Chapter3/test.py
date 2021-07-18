import timeit
import random


def partition(L, p, r):
    x = L[r]
    i = p-1
    for j in range(p, r):
        if L[j] <= x:
            i += 1
            L[i], L[j] = L[j], L[i]
    L[i+1], L[r] = L[r], L[i+1]
    return i+1


def randomPartition(L, p, r):
    if p == r:
        return p
    i = random.randint(p, r)
    L[i], L[r] = L[r], L[i]
    return partition(L, p, r)


def randomizedSelect(L, p, r, i):
    if p == r:
        return L[p]
    q = randomPartition(L, p, r)
    k = q - p + 1
    if i == k:
        return L[q]
    elif i < k:
        return randomizedSelect(L, p, q-1, i)
    else:
        return randomizedSelect(L, q+1, r, i-k)


def kthMinLinear(L, k):
    """ Assumption: L is a list of numbers. k is the index to be found.
    time complexity: O(n) - expected linear time implementation
    randomizedSelect method finds the Kth elemenet by repeated partitioning
    the List around randomly chosen pivot.
    """
    if L is None:
        return None
    if k < 0 or k > len(L):
        return None
    value = randomizedSelect(L, 0, len(L)-1, k)
    return value


def kthMin(L, k):
    """ Assumption is L is a list, here we will sort the list and return the
    Kth index - time complexity: O(nlog(n)) """
    if L is None:
        return None
    if k < 0 or k > len(L):
        return None
    L.sort()
    return L[k-1]


def main():
    print(f"{'N':10s}{'NlogN':>10s}{'Linear':>10s}")
    for i in range(7):
        N = 10 ** i
        L = list(range(N))
        k = random.randrange(N)
        random.shuffle(L)
        nlogntimer = timeit.Timer(f"kthMin({L}, {k})", "from __main__ import kthMin")
        random.shuffle(L)
        kthVal = kthMinLinear(L, k)
        lineartimer = timeit.Timer(f"kthMinLinear({L}, {k})", "from __main__ import kthMinLinear")
        print(f"{N:<10.0f}{nlogntimer.timeit(number=1000):>10.4f}{lineartimer.timeit(number=1000):>10.4f}")


if __name__ == '__main__':
    main()


"""
Result:
timeit(number=1000)
N              NlogN    Linear
1             0.0002    0.0002
10            0.0004    0.0061
100           0.0045    0.0258
1000          0.1060    0.1935
10000         1.5963    2.3609
100000       22.2780   15.0098
1000000     388.6744  256.2814
"""