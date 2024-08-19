import logging
import inspect


class custlogger :

    def custlogger(loglevel=logging.DEBUG):
        # logging.basicConfig(filename='..\\Logs\\Automation.log', format='%(asctime)s:%(levelname)s:%(message)s',
        #                     datefmt='%m/%d/%Y %I:%M:%S %p')
        # logging.debug('This message should appear on the console')
        # logging.info('So should this')
        # logging.warning('And this, too')
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        logger.setLevel(loglevel)
        fh = logging.FileHandler("automation.log", mode='w')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s -  %(name)s : %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        return logger