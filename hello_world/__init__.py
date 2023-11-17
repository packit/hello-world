#!/usr/bin/python3

# Copyright Contributors to the Packit project.
# SPDX-License-Identifier: MIT

__version__ = "0.1.1"

import sys


def usage():
    print(
        "Usage: hello NAME\n"
    )
    sys.exit(3)


def main():
    args_n = len(sys.argv)
    if args_n <= 1 or args_n > 2:
        usage()
    print(f"Hello {sys.argv[1]}")


if __name__ == '__main__':
    main()
