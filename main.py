from board import Board
import utils as u
import time
import itertools

if __name__ == '__main__':
    print("Hello World")

    example_list = [1]*3 + [2]*2 + [0]*4

    t1_1 = time.time()
    perms = u.perms4(example_list)
    t1_2 = time.time()
    print("Solution 1: {} elements".format(len(perms)))
    print("Took {} seconds".format(t1_2-t1_1))
    print()
