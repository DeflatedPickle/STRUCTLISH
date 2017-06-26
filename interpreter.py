#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

from sys import exit

__title__ = "Interpreter"
__author__ = "DeflatedPickle"
__version__ = "1.6.1"


class Interpreter(object):
    def __init__(self, file):
        self.open = open(file)

        self.read_lines = self.open.readlines()
        self.read_lines_stripped = [line.strip("\n") for line in self.read_lines]

        self.read_lines_enum = enumerate(self.read_lines_stripped)

        self.flag_start = False

        self.metadata = {"name": None}

        self.variable_dictionary = {}

        self.main_loop()

    def main_loop(self):
        self.metadata["name"] = self.read_lines_stripped[0]

        for count, item in self.read_lines_enum:
            self.syntax(item, count)
            # print(count + 1, item)

    def syntax(self, line, number):
        line_split = line.split(" ")

        if not self.flag_start:
            self.flag_start = True
            print("Started Interpreting: {}.\n".format(self.metadata["name"]))

        if "COMMENT" in line:
            # self.quick_print("COMMENT", number)
            index = line_split.index("COMMENT")
            del line_split[index:]

        if line.startswith("EXIT"):
            # self.quick_print("EXIT", number)
            print("\nFinished Interpreting: {}.".format(self.metadata["name"]))
            exit()

        elif "PASS" in line:
            # self.quick_print("PASS", number)
            pass

        elif "PRINT" in line:
            # self.quick_print("PRINT", number)
            is_variable = False

            if "VARIABLE" in line:
                is_variable = True

            print_type, print_value = self.work_out_type(line, number, line_split[-1])

            if is_variable:
                print(self.variable_dictionary[print_value]["value"])

            else:
                print(" ".join(line_split[2:]))

        elif line.startswith("IF"):
            # self.quick_print("IF", number)
            variable_type, variable_value = self.work_out_type(line, number, line_split[2])
            value_type, value_value = self.work_out_type(line, number, line_split[-2])

            is_variable_a_variable = self.is_variable(line_split, variable_value)
            is_value_a_variable = self.is_variable(line_split, value_value)
            is_not = False
            compare = ""

            if "NOT" in line:
                # self.quick_print("-NOT", number)
                is_not = True

            if "IDENTICAL TO" in line:
                # self.quick_print("-IDENTICAL TO", number)
                compare = "IDENTICAL TO"

            elif "MORE THAN" in line:
                # self.quick_print("-MORE THAN", number)
                compare = "MORE THAN"

            elif "LESS THAN" in line:
                # self.quick_print("-LESS THAN", number)
                compare = "LESS THAN"

            if "THEN" in line:
                # self.quick_print("-THEN", number)
                pass

            for count, item in self.read_lines_enum:
                if item.startswith("ENDIF"):
                    # self.quick_print("ENDIF", count)
                    break

                elif item.startswith("ELSE IF"):
                    # self.quick_print("|ELSE IF", count)
                    self.syntax(item, count)

                elif item.startswith("ELSE"):
                    # self.quick_print("|ELSE", count)
                    self.syntax(item, count)

                else:
                    if is_variable_a_variable:
                        current_variable = self.variable_dictionary[variable_value]["value"]

                    else:
                        current_variable = variable_value

                    if is_value_a_variable:
                        current_value = self.variable_dictionary[value_value]["value"]

                    else:
                        current_value = value_value

                    if compare == "IDENTICAL TO":
                        if is_not:
                            if current_variable != current_value:
                                self.syntax(item, count)

                        else:
                            if current_variable == current_value:
                                self.syntax(item, count)

                    elif compare == "MORE THAN":
                        if current_variable > current_value:
                            self.syntax(item, count)

                    elif compare == "LESS THAN":
                        if current_variable < current_value:
                            self.syntax(item, count)

        # TODO: Add FOR loops.

        elif "FOR" in line:
            # self.quick_print("FOR", number)
            variable_type, variable_value = self.work_out_type(line, number, line_split[2])
            value_type, value_value = self.work_out_type(line, number, line_split[-2])

            is_variable_a_variable = self.is_variable(line_split, variable_value)
            is_value_a_variable = self.is_variable(line_split, value_value)
            is_in = False
            in_what = ""

            value_from = 0
            value_to = 0

            self.variable_dictionary[variable_value] = {"type": variable_type, "value": None}

            if "IN" in line:
                is_in = True

            if "RANGE" in line:
                in_what = "RANGE"
                try:
                    value_from = int(line_split[line_split.index("TO") - 1])
                    value_to = int(line_split[line_split.index("TO") + 1])

                except ValueError:
                    value_from = 0
                    value_to = int(line_split[-1])

            for count, item in self.read_lines_enum:
                if item.startswith("ENDFOR"):
                    # self.quick_print("ENDFOR", count)
                    break

                else:
                    if in_what == "RANGE":
                        for variable in range(value_from, value_to):
                            self.variable_dictionary[variable_value]["value"] = variable
                            self.syntax(item, count)

                        del self.variable_dictionary[variable_value]

        # TODO: Add WHILE loops.

        elif "VARIABLE" in line:
            # self.quick_print("VARIABLE", number)
            variable_name = line_split[1]
            variable_type = None
            variable_value = None

            if "EQUALS" in line:
                # self.quick_print("-EQUALS", number)
                variable_type, variable_value = self.work_out_type(line, number, line_split[-1])

            self.variable_dictionary[variable_name] = {"type": variable_type, "value": variable_value}

    def is_variable(self, line, value):
        if "VARIABLE" in line[line.index(str(value)) - 1]:
            return True

        else:
            return False

    def work_out_type(self, line, number, variable_value):
        variable_type = None
        line_split = line.split(" ")

        if "STRING" in line_split[line_split.index(variable_value) - 1]:
            # self.quick_print("--STRING", number)
            variable_type = "STRING"
            variable_value = str(variable_value)

        elif "INTEGER" in line_split[line_split.index(variable_value) - 1]:
            # self.quick_print("--INTEGER", number)
            variable_type = "INTEGER"
            variable_value = int(variable_value)

        elif "BOOLEAN" in line_split[line_split.index(variable_value) - 1]:
            # self.quick_print("--BOOLEAN", number)
            variable_type = "BOOLEAN"
            variable_value = bool(variable_value)

        elif "FLOAT" in line_split[line_split.index(variable_value) - 1]:
            # self.quick_print("--FLOAT", number)
            variable_type = "FLOAT"
            variable_value = float(variable_value)

        return variable_type, variable_value

    def quick_print(self, *args):
        print("{} on line: {}.".format(args[0], args[1] + 1))


if __name__ == "__main__":
    Interpreter("./example.stre")
