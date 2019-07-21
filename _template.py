import os
import argparse
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
matplotlib.style.use('ggplot')
from logging import StreamHandler, DEBUG, Formatter, FileHandler, getLogger

logger = getLogger(__name__)

def main(args):
    # Create directories if not exist.
    logger.debug('start')
    logger.debug('end')

    return

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='description of this program')
    parser.add_argument('--verbose', type=int, default=0, help='verbose')
    parser.add_argument('--seed', type=int, default=42, help='Numpy Random State')
    parser.add_argument('--batch_size', type=int, default=16, help='mini-batch size')
    parser.add_argument('--mode', type=str, default='train', choices=['train', 'test'])
    parser.add_argument('--result_dir', type=str, default='results')
    parser.add_argument('--foobar', action='store_true')    # default -> False, --foobar  -> True
    parser.add_argument('--foonley', action='store_false')  # default -> True,  --foonley -> False
    args = parser.parse_args()

    if not os.path.exists(args.result_dir):
        os.makedirs(args.result_dir)

    log_fmt = Formatter('%(asctime)s %(name)s %(lineno)d [%(levelname)s][%(funcName)s] %(message)s ')
    handler = StreamHandler()
    handler.setLevel('INFO')
    handler.setFormatter(log_fmt)
    logger.addHandler(handler)

    handler = FileHandler(os.path.join(args.result_dir, '_template.py.log'), 'a')
    handler.setLevel(DEBUG)
    handler.setFormatter(log_fmt)
    logger.setLevel(DEBUG)
    logger.addHandler(handler)

    logger.info('start')
    logger.debug(args)

    np.random.seed(args.seed)
    logger.debug('np.random.seed: {}'.format(args.seed))

    main(args)

    logger.info('end')
