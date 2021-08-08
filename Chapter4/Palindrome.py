from pythonds3.basic import Deque


def pal_checker(a_string):
    a_string = a_string.replace(" ",'')
    char_deque = Deque()

    for ch in a_string:
        print(ch)
        char_deque.add_rear(ch)

    while char_deque.size() > 1:
        first = char_deque.remove_front()
        last = char_deque.remove_rear()
        if first != last:
            return False

    return True

if __name__ == '__main__':
    print(pal_checker("I PREFER PI"))