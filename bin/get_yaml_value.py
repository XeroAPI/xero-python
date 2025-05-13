import argparse

from yaml import load

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


def read_value(file, key, default=None):
    data = load(file, Loader=Loader)
    return data.get(key, default)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="get_yaml_file")
    parser.add_argument(
        "yaml_file", type=argparse.FileType("r"), help="Path to configuration yaml file"
    )
    parser.add_argument(
        "yaml_key", type=str, help="Key for value in configuration yaml file"
    )
    args = parser.parse_args()
    try:
        print(read_value(args.yaml_file, args.yaml_key))
    finally:
        args.yaml_file.close()
