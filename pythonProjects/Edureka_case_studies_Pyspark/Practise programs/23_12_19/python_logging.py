import logging

#logging.basicConfig(level=logging.DEBUG)
#logging.debug('This will get logged')

logging.basicConfig(filename='prac_prgs.log', format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This will get logged to a file')
