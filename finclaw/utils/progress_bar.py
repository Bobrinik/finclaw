from tqdm import tqdm
from finclaw.config import settings, logger


def simple_progress_bar(iterable):
    counter = 0
    for i in iterable:
        if counter % 55 == 0:
            logger.info(counter)
        counter += 1
        yield i


def get_progress_bar():
    if settings.USE_TQDM:
        return lambda x: tqdm(x)
    else:
        return simple_progress_bar


progress_bar = get_progress_bar()
