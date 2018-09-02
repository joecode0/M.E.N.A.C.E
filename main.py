from board import Board
import utils as u
import time

if __name__ == '__main__':
    print("Hello World")
    my_list = [1]*3 + [2]*2 + [0]*4
    print(my_list)
    perms = u.perms(my_list)
    print(perms)
