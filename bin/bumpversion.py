import argparse
import fileinput
import re

SETUP_VERSION = re.compile(r'^(\s*version\s*=\s*")[^"]*("\s*,?\s*)$')
INIT_VERSION = re.compile(r'^(\s*__version__\s*=\s*")[^"]*("\s*)$')


FILES = (("setup.py", SETUP_VERSION), ("xero/__init__.py", INIT_VERSION))


def replace_in_file(path, pattern, replacement):
    with fileinput.input(path, inplace=True) as file:
        for line in file:
            print(re.sub(pattern, replacement, line), end="")


def main(version):
    replacement = r"\g<1>" + version + r"\g<2>"
    for path, pattern in FILES:
        replace_in_file(path, pattern, replacement)
        print("Bumped version in {!r} to {}".format(path, version))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="bumpversion")
    parser.add_argument("version", type=str, help="version string to bump version to")
    args = parser.parse_args()
    main(version=args.version)
