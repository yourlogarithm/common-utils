import logging


class Logger:
    def __init__(self, name: str, level: str = 'INFO'):
        logging.basicConfig(
            level=level,
            format="%(asctime)s [%(levelname)s] %(message)s",
            handlers=[
                logging.FileHandler('debug.log'),
                logging.StreamHandler()
            ]
        )
        self._inner = logging.getLogger(name)

    def __getattr__(self, item):
        return getattr(self._inner, item)
