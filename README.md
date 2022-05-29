# Entropy

Calculate the information entropy of a string, file, etc.

## Installation

Install with `pip`

## Usage

### Command Line

Basic usage: `entropy [-h] [-f FILE | -t TEXT | -p] [-b BASE] [-s] [-m]`.

Requires one of `--shannon` (to calculate the Shannon entropy)
or `--metric` (to calculate the Shannon entropy normalised by input size).

Takes input fdom stdin by default, but can read from a file with `--file`
or from the `--text` argument.

Entropy is calculated in base 2 by default, but this can be changed with `--base`.

See `--help` for extended command line usage.

### Module

Importing provides an `Entropy` class which takes bytes and a base (both optional)
and exposes methods `shannon` and `metric` to calculate the Shannon and normalised entropy.
The data can be updated with the `update` method.
