import os

import pandas as pd

ABSPATH_DIRECTORY = os.path.dirname(__file__)
ABSPATH_TRAIN     = os.path.join(ABSPATH_DIRECTORY, 'train')
ABSPATH_TEST      = os.path.join(ABSPATH_DIRECTORY, 'test')

def main():
    train = load_dataset(ABSPATH_TRAIN)
    path  = os.path.join(ABSPATH_DIRECTORY, 'train.csv')
    train.to_csv(path)

    test  = load_dataset(ABSPATH_TEST)
    path  = os.path.join(ABSPATH_DIRECTORY, 'test.csv')
    test.to_csv(path)

if __name__ == '__main__':
    main()
