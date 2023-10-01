import argparse
from handcrafted_image_representations.machine_learning import BestOfBagOfWords

from test_image_classifier import test
from handcrafted_image_representations.utils.utils import load_dict


class Config:
    def __init__(self, model_folder):
        self.down_sample = 0.0

        self.class_mapping = None
        self.mf = model_folder

        self.opt = {
            "data_split_mode": "random",
            "aggregator": ["vlad"],
            "complexity": [16, 32, 64],
            "type": ["mlp"],
            "feature": ["hsv-sift"],
            "sampling_method": ["dense"],
            "image_size": [
                {
                    "width": None,
                    "height": None,
                }
            ]
        }


def start_training(args_, cfg):
    df = args_.dataset_folder
    mf = cfg.mf

    bob = BestOfBagOfWords(cfg.opt, cfg.class_mapping)
    bob.fit(mf, df, args_.dataset_type, load_all=False)
    if args_.test_folder is not None:
        test(mf, args_.test_folder, load_all=False, dt=args_.dataset_type)


def main(args_):
    cfg = Config(args_.model_folder)
    cfg.class_mapping = load_dict(args_.class_mapping)
    start_training(args_, cfg)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--dataset_folder",
        "-df",
        help="Path to directory with dataset",
    )
    parser.add_argument(
        "--test_folder",
        "-tf",
        default=None,
        help="Path to directory with test dataset",
    )
    parser.add_argument(
        "--dataset_type",
        "-dtype",
        default="cls",
        help="Choose Dataset Annotation Bounding-Boxes [box] or Image Labels [cls]",
    )
    parser.add_argument(
        "--model_folder",
        "-model",
        help="Path to model",
    )
    parser.add_argument(
        "--class_mapping",
        "-clmp",
        help="Path to class mapping JSON",
    )
    parser.add_argument(
        "--use_cache",
        "-cache",
        type=bool,
        default=False,
        help="Save the Calculated Features in _cache folder",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    main(args)
