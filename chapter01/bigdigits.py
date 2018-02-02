#!/usr/bin/env python3

import sys
from operator import add
from functools import reduce

# 7 by 7 matrices representing 'printable' digits
# Digits are mapped to their corresponding indices
encoded_digits = [
    ["  ***  ", " *   * ", "*     *", "*     *", "*     *", " *   * ", "  ***  "],
    ["   *   ", "  **   ", " * *   ", "   *   ", "   *   ", "   *   ", " ***** "],
    ["  ***  ", " *   * ", " *  *  ", "   *   ", "  *    ", " *     ", " ***** "],
    ["  ***  ", " *   * ", "     * ", "   **  ", "     * ", " *   * ", "  ***  "],
    ["     * ", "    ** ", "   * * ", "  *  * ", " ******", "     * ", "     * "],
    [" ***** ", "*      ", "*      ", " ***** ", "      *", "      *", " ***** "],
    ["  ***  ", " *     ", " *     ", " ****  ", " *   * ", " *   * ", "  ***  "],
    [" ******", "      *", "     * ", "    *  ", "   *   ", "  *    ", " *     "],
    ["  ***  ", " *   * ", " *   * ", "  ***  ", " *   * ", " *   * ", "  ***  "],
    ["  **** ", " *    *", " *    *", "  **** ", "     * ", "    *  ", "  **   "]
]

if len(sys.argv) != 2:
    sys.stderr.write("Usage:\n{} <number>\n".format(sys.argv[0]))
    sys.exit(1)

# List of 'encoded' digits according to program arguments
# '*' replaced by corresponding digit
raw_digits = [[ch.replace('*', d) for ch in encoded_digits[int(d)]] for d in sys.argv[1]]

# Join columns a.k.a. rows of transponsed
colled_digits = [reduce(add, col) for col in zip(*raw_digits)]

# Join rows with '\n'
rowed_digits = "\n".join(colled_digits)

print(rowed_digits)
