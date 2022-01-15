

import time
import sys


def s_print(s,t):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(t)
    print()

s_print("hello world",.15)
s_print("hello world",.08)
s_print("hello world",.02)