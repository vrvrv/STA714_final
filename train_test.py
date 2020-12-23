from generate_missing import ampute
import pandas as pd
from sklearn.model_selection import train_test_split

def train_test_ampute():
    data = pd.read_csv("./data/boston_transform.csv",
                           index_col = 'original_idx')
    train, test = train_test_split(data, test_size=0.33)
    return train, test


if __name__ == '__main__':
    path = './data/train_test'
    train, test = train_test_ampute()

    test.to_csv(path + '/test.csv')

    for i in range(1, 1+100):
        ampute(train, i, path)