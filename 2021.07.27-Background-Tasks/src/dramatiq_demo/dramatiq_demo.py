import sys

import dramatiq


@dramatiq.actor
def count_to(n):
    for i in range(n):
        print(i ** 2)


if __name__ == '__main__':
    n = int(sys.argv[1])
    sys.exit(count_to.send(n))
