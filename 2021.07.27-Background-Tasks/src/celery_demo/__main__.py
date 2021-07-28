import sys

import celery

from . import celery_demo


if __name__ == '__main__':
    # Example 1
    result = celery_demo.count_to.delay(4)
    print(result)

    # Example 2
    uri = sys.argv[1]

    pipe = celery.chain(
        celery_demo.get_uri_contents.s(uri),
        celery_demo.count_words.s(uri),
    ).apply_async()
