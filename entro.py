#!/usr/bin/env python3

from math import log
import argparse
import getpass
from typing import Union, Any

class Entropy:

    def __init__(self, array=None, base: Union[float, int] = 2) -> None:
        if array:
            self.array = bytes(array)
        else:
            self.array = b""
        self._base = base

    def update(self, array: Any) -> None:
        self.array = bytes(self.array)
        self.array += bytes(array)

    def _p(self, i: int) -> float:
        return self.array.count(i) / len(self.array)

    def shannon(self) -> float:
        """Calculates Shannon entropy"""
        H = 0.0
        for i in set(self.array):
            H -= self._p(i) * log(self._p(i), self._base)
        return H

    def metric(self) -> float:
        """Calculates normalised Shannon entropy"""
        return self.shannon() / len(self.array)

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

    if args.base is not None:
        log_base = args.base
    else:
        log_base = 2
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

