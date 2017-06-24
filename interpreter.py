#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

__title__ = "Interpreter"
__author__ = "DeflatedPickle"
__version__ = "1.0.0"


class Interpreter(object):
    def __init__(self, file):
        self.open = open(file)

        self.read_lines = self.open.readlines()
        self.read_lines_stripped = [line.strip("\n") for line in self.read_lines]

        self.read_lines_enum = enumerate(self.read_lines_stripped)

        self.flag_start = False

        self.metadata = {"name": None}

        self.main_loop()

    def main_loop(self):
        self.metadata["name"] = self.read_lines_stripped[0]

        for count, item in self.read_lines_enum:
            self.syntax(item, count)
            # print(count + 1, item)

    def syntax(self, line, number):
        if not self.flag_start:
            self.flag_start = True
            print("Interpreting: {}.".format(self.metadata["name"]))

        if line.endswith(""):
            print("")

        if "COMMENT" in line:
            self.quick_print("COMMENT", number)

        if line.startswith("EXIT"):
            self.quick_print("EXIT", number)

        elif "PRINT" in line:
            self.quick_print("PRINT", number)

        elif line.startswith("IF"):
            self.quick_print("IF", number)

            if "NOT" in line:
                self.quick_print("-NOT", number)

            if "IDENTICAL" in line:
                self.quick_print("-IDENTICAL", number)

            if "THEN" in line:
                self.quick_print("-THEN", number)

            for count, item in self.read_lines_enum:
                if item.startswith("ENDIF"):
                    self.quick_print("ENDIF", count)

                elif item.startswith("ELSE"):
                    self.quick_print("|ELSE", count)
                    for count1, item1 in self.read_lines_enum:
                        self.syntax(item1, count1)

                else:
                    self.syntax(item, count)

        # TODO: Add FOR loops.

        # TODO: Add WHILE loops.

        elif "VARIABLE" in line:
            self.quick_print("VARIABLE", number)

            if "EQUALS" in line:
                self.quick_print("-EQUALS", number)

                if "STRING" in line:
                    self.quick_print("--STRING", number)

                elif "INTEGER" in line:
                    self.quick_print("--INTEGER", number)

                elif "BOOLEAN" in line:
                    self.quick_print("--BOOLEAN", number)

                elif "FLOAT" in line:
                    self.quick_print("--FLOAT", number)

    def quick_print(self, *args):
        print("{} on line: {}.".format(args[0], args[1] + 1))


if __name__ == "__main__":
    Interpreter("./example.stre")
