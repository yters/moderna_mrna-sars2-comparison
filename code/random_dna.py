import sys
from random import randint

print(''.join(['gatc'[randint(0, 3)] for _ in range(int(sys.argv[1]))]))
