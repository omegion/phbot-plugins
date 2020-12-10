import logging

logger = logging.getLogger('phbot')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('fileLog.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)


class Logger(object):
    def __init__(self):
        self.log = self.get_logger()
        self.logFile = logger.log

    def get_logger(self):
        try:
            from phBot import log
            return log
        except ImportError:
            import logging
            logger = logging.getLogger()
            return logger.debug
