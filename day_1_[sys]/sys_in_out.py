import sys
import time
from random import choice
# import os


secs = [0.1, 0.3, 0.01, 0.2, 0.5]

bar = ['-' for i in range(50)]


def do(total):
    # sys.stdout.write('[')
    for i in range(total):
        time.sleep(choice(secs))
        # sys.stdout.flush()
        bar[i] = '#'
        print(f'\r|{"".join(bar)}|', end='\r')
    # sys.stdout.write(']')
    print()


do(50)
