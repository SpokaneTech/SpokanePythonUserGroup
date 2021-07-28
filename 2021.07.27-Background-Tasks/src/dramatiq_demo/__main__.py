import sys

from dramatiq import Message, pipeline

from . import dramatiq_demo


if __name__ == '__main__':
    # Example 1
    result: Message = dramatiq_demo.count_to.send(4)
    print(result.message_id)

    # Example 2
    # uri = sys.argv[1]
    # pipe = pipeline([
    #     dramatiq_demo.get_uri_contents.message(uri),
    #     dramatiq_demo.count_words.message(uri),
    # ]).run()
