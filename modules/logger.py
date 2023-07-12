import logging

def write(message, level):
    logging.basicConfig(filename='./inventory.log', format='%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
    if level == 'debug':
        logging.debug(message)
    else:
        logging.info(message)