import sys

if sys.argv is not None:
    for arg in sys.argv[::-1]:
        print(arg[::-1].replace(sys.argv[0][::-1], '').swapcase(), end='')

print ()
