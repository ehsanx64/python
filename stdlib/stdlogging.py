import logging


def demo_basic_usage():
    logging.basicConfig(level=logging.INFO)
    logging.info('This is an info log')
    logging.info('This is an info log')
    logging.warning('This is a warning log')
    logging.error('This is an error log')

def demo_custom_formatting():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    logging.info('This log uses the custom format')


demo_basic_usage()
demo_custom_formatting()

