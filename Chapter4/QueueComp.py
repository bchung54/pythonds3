from Queue import Queue, QueueEnd
from QueueDLList import QueueDLL
import timeit
"""
Programming Exercise 4.27.6
Design and implement an experiment to do benchmark comparisons of the two queue implementations. 
"""

print(f"{'size':20s}{'Q Time':>10s}{'QE Time':>10s}{'QDLL Time':>10s}")
q = Queue()
qe = QueueEnd()
qd = QueueDLL()
sizes = 7
for i in range(sizes):
    N = 100 ** i


    qt = timeit.Timer(f"q.enqueue(N)", "from __main__ import q, N")
    qet = timeit.Timer(f"qe.enqueue(N)", "from __main__ import qe, N")
    qdt = timeit.Timer(f"qd.enqueue(N)", "from __main__ import qd, N")
    print(f"{N:<20,}{qt.timeit(number=1000):>10.6f}{qet.timeit(number=1000):>10.6f}{qdt.timeit(number=1000):>10.6f}")

print('*' * 8, "Dequeue Times", '*' * 8)
print(f"{'size':20s}{'Q Time':>10s}{'QE Time':>10s}{'QDLL Time':>10s}")
for i in range(sizes):
    N = 100 ** i


    qdt = timeit.Timer(f"q.dequeue()", "from __main__ import q, N")
    qedt = timeit.Timer(f"qe.dequeue()", "from __main__ import qe, N")
    qddt = timeit.Timer(f"qd.dequeue()", "from __main__ import qd, N")
    print(f"{N:<20,}{qdt.timeit(number=1000):>10.6f}{qedt.timeit(number=1000):>10.6f}{qddt.timeit(number=1000):>10.6f}")
