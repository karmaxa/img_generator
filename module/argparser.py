import argparse


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c", "--count",
        type=int,
        default=10,
    )
    parser.add_argument(
        "-l", "--language",
        type=str,
        default="ru",
    )
    parser.add_argument(
        "-s", "--size",
        type=int,
        default=128,
    )
    parser.add_argument(
        "-d", "--distorsion",
        type=int,
        default=3,
    )
    parser.add_argument(
        "-do", "--distorsion_orientation",
        type=int,
        default=2,
    )
    parser.add_argument(
        "-bl", "--blur",
        type=int,
        default=3,
    )
    parser.add_argument(
        "-norbl", "--no_random_blur",
        action="store_false",
    )
    parser.add_argument(
        "-b", "--background",
        type=int,
        default=3,
    )
    parser.add_argument(
        "-k", "--skewing_angle",
        type=int,
        default=0,
    )

    return parser
