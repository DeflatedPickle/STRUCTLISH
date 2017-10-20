#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""""

import sys
import re

__title__ = "Interpreter"
__author__ = "DeflatedPickle"
__version__ = "1.0.0"


class Interpreter(object):
    def __init__(self, file, debugging: bool=False):
        self.file = file

        self.deugging = debugging

        tokens = self.lexer(file)
        self.parse(tokens)

    def lexer(self, file):
        return ""

    def parse(self, tokens):
        pass


def run(file):
    if file.endswith((".structlish", ".struct", ".structlang")):
        data = open(file, "r").read()
        data += "<EOF>"
        Interpreter(data)


if __name__ == "__main__":
    try:
        run(sys.argv[1])
    except IndexError:
        run("../tests/print.structlish")
