import numpy as np


def split_tags(list_of_tags, ratio=0.2):
    train_tags = {}
    test_tags = {}

    for t in list_of_tags:
        if np.random.randint(100) / 100 > ratio:
            train_tags[len(train_tags)] = list_of_tags[t]
        else:
            test_tags[len(test_tags)] = list_of_tags[t]

    return train_tags, test_tags
