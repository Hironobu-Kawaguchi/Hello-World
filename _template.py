import os
import argparse
import numpy as np
random_state=42
np.random.seed(random_state)
import pandas as pd
# pd.set_option('display.max_columns', None)  # 常に全ての列（カラム）を表示
# pd.set_option('display.max_rows', None)     # 常に全ての行を表示
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
matplotlib.style.use('ggplot')


def main(args):
    # Create directories if not exist.
    if not os.path.exists(args.result_dir):
        os.makedirs(args.result_dir)

    return

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='description of this program')
    parser.add_argument('--verbose', type=int, default=0, help='verbose')
    parser.add_argument('--batch_size', type=int, default=16, help='mini-batch size')
    parser.add_argument('--mode', type=str, default='train', choices=['train', 'test'])
    parser.add_argument('--result_dir', type=str, default='results')
    parser.add_argument('--foobar', action='store_true')    # default -> False, --foobar  -> True
    parser.add_argument('--foonley', action='store_false')  # default -> True,  --foonley -> False

    args = parser.parse_args()
    if args.verbose:
        print(args)
    main(args)
