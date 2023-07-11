#!/usr/bin/python3

# Copyright Contributors to the Packit project.
# SPDX-License-Identifier: MIT

__version__ = "0.1.0"

import sys


def usage():
    print(
        "Usage: world GREETING\n"
    )
    sys.exit(3)


def main():
    args_n = len(sys.argv)
    if args_n <= 1 or args_n > 2:
        usage()
    print(f"{sys.argv[1]} world!")


if __name__ == '__main__':
    main()
