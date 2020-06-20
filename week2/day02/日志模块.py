#__author:gzc
#date:2020/6/20
# -- coding: utf-8 --
import logging
import os

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s)',
    datefmt='%a,%d %b %Y %H:%M:%S',
    filemode='a',
    filename=os.path.dirname(os.path.abspath(__file__))+'/log/log1.txt'
)
logger = logging.getLogger()

fh = logging.FileHandler(os.path.dirname(os.path.abspath(__file__))+'/log/log1.txt')


ch = logging.StreamHandler()
format = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s)')

fh.setFormatter(format)
ch.setFormatter(format)

logger.addHandler(ch)
logger.addHandler(fh)
logger.setLevel(logging.DEBUG)
logger.debug('debug logging')
logger.info('info logging')
logger.error('error logging')
logger.warning('warning logging')
logger.critical('critical logging')
