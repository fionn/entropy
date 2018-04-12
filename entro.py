#!/usr/bin/env python3

from math import log
import argparse
import getpass
from typing import Union, Any

class Entropy:

    def __init__(self, string=None, base: Union[float, int] = 2) -> None:
        self.string = string or b""
        self._base = base

    def update(self, string: Any) -> None:
        self.string = bytes(self.string)
        self.string += bytes(string)

    def _p(self, i: bytes) -> float:
        return self.string.count(i) / len(self.string)

    def shannon(self) -> float:
        """Calculates Shannon entropy"""
        H = 0.0
        for i in set(self.string):
            H -= self._p(i) * log(self._p(i), self._base)
        return H

    def metric(self) -> float:
        """Calculates normalised Shannon entropy"""
        return self.shannon() / len(self.string)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate entropy")
    parser.add_argument("-f", "--file")
    parser.add_argument("-t", "--text")
    parser.add_argument("-b", "--base", type=float)
    parser.add_argument("-p", "--password", action="store_true")
    parser.add_argument("-s", "--shannon", action="store_true")
    parser.add_argument("-m", "--metric", action="store_true")
    args = parser.parse_args()

    if not args.shannon or args.metric:
        parser.print_usage()
        exit(1)

    log_base = args.base or 2
    entropy = Entropy(base=log_base)

    if args.file:
        with open(args.file, "rb") as f:
            entropy.update(f.read())
    elif args.text:
        entropy.update(args.text)
    elif args.password:
        entropy.update(getpass.getpass())
    else:
        entropy.update(input("Enter text: "))

    if args.shannon:
        print(entropy.shannon())
    if args.metric:
        print(entropy.metric())

