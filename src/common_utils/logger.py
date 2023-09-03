import logging


class Logger:
    def __init__(self, name: str, level: str = 'INFO'):
        logging.basicConfig(
            level=logging.WARNING,
            format="%(asctime)s [%(levelname)s] %(message)s",
            handlers=[
                logging.FileHandler('debug.log'),
                logging.StreamHandler()
            ]
        )
        self._inner = logging.getLogger(name)
        self._inner.setLevel(level.upper())

    def __getattr__(self, item):
        return getattr(self._inner, item)
