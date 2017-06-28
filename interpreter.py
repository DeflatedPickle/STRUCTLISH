#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import sys

__title__ = "Interpreter"
__author__ = "DeflatedPickle"
__version__ = "1.9.1"


class Interpreter(object):
    def __init__(self, file):
        self.open = open(file)

        self.read_lines = self.open.readlines()
        self.read_lines_stripped = [line.strip("\n") for line in self.read_lines]

        self.read_lines_enum = enumerate(self.read_lines_stripped)

        self.language_syntax = {"keywords": ["IF", "ENDIF", "FOR", "ENDFOR", "THEN", "PASS", "NEWLINE"],
                                "data_types": ["VARIABLE", "STRING", "INTEGER", "BOOLEAN", "FLOAT"],
                                "functions": ["PRINT", "RANGE"],
                                "operators": ["NOT", "IN", "IDENTICAL", "TO", "MORE", "LESS", "THAN", "TO"],
                                "others": ["PROGRAM", "EXIT"]}

        self.flag_start = False

        self.metadata = {"name": None}

        self.variable_dictionary = {}

        self.current_line = None
        self.current_line_split = None
        self.current_line_number = 0

        self.found_variable = False
        self.found_value = False

        self.main_loop()

    def main_loop(self):
        for count, item in self.read_lines_enum:
            try:
                self.syntax(item, count)
            except:
                e = sys.exc_info()[0]
                print("\033[1;31m" + "\nException: {}, Line: {} - {}".format(e, count, item.strip()) + "\033[0;0m")
            # print(count + 1, item)

    def syntax(self, line, number):
        self.current_line = line
        self.current_line_split = line.split(" ")
        self.current_line_number = number

        self.found_variable = False
        self.found_value = False

        line_split = line.split(" ")

        if not self.flag_start:
            self.flag_start = True

            if "PROGRAM" in line:
                self.metadata["name"] = " ".join(line_split[1:])

            print("Started Interpreting: {}.\n".format(self.metadata["name"]))

        if "COMMENT" in line:
            # self.quick_print("COMMENT", number)
            index = line_split.index("COMMENT")
            del line_split[index:]

        if line.startswith("EXIT"):
            # self.quick_print("EXIT", number)
            print("\nFinished Interpreting: {}.".format(self.metadata["name"]))
            sys.exit()

        elif "PASS" in line:
            # self.quick_print("PASS", number)
            pass

        elif "PRINT" in line:
            # self.quick_print("PRINT", number)
            is_variable = False

            if "VARIABLE" in line:
                is_variable = True

            print_type, print_value = self.work_out_type(line, number)

            if is_variable:
                print(self.variable_dictionary[print_value]["value"])

            else:
                print(" ".join(line_split[2:]))

        elif "NEWLINE" in line:
            print("")

        elif line.startswith("IF"):
            # self.quick_print("IF", number)
            variable_type, variable_value = self.work_out_type(line, number)
            value_type, value_value = self.work_out_type(line, number)

            print("Variable Type: {}\nVariable Value: {}\n\nValue Type: {}\nValue Value: {}\n".format(variable_type, variable_value, value_type, value_value))

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

        elif "FOR" in line:
            # self.quick_print("FOR", number)
            variable_type, variable_value = self.work_out_type(line, number)
            value_type, value_value = self.work_out_type(line, number)

            is_in = False
            in_what = ""
            is_variable = False

            value_content = ""
            value_from = 0
            value_to = 0

            self.variable_dictionary[variable_value] = {"type": variable_type, "value": None}

            if "IN" in line_split:
                is_in = True

            if "RANGE" in line_split:
                in_what = "RANGE"
                try:
                    value_from = int(line_split[line_split.index("TO") - 1])
                    value_to = int(line_split[line_split.index("TO") + 1])

                except ValueError:
                    value_from = 0
                    value_to = int(line_split[-1])

            elif value_type == "VARIABLE":
                in_what = "VARIABLE"
                is_variable = True

            elif "STRING" in line_split:
                in_what = "STRING"
                value_content = " ".join(line_split[5:])[:-5]

            for count, item in self.read_lines_enum:
                if item.startswith("ENDFOR"):
                    # self.quick_print("ENDFOR", count)
                    break

                else:
                    if is_in:
                        if in_what == "RANGE":
                            for value in range(value_from, value_to):
                                self.variable_dictionary[variable_value]["value"] = value
                                self.syntax(item, count)

                            del self.variable_dictionary[variable_value]

                        elif in_what == "STRING":
                            for character in value_content:
                                self.variable_dictionary[variable_value]["value"] = character
                                self.syntax(item, count)

                            del self.variable_dictionary[variable_value]

                        else:
                            if is_variable:
                                for value in self.variable_dictionary[value_value]["value"]:
                                    self.variable_dictionary[variable_value]["value"] = value
                                    self.syntax(item, count)

                                del self.variable_dictionary[variable_value]

        # TODO: Add WHILE loops.

        elif "VARIABLE" in line:
            # self.quick_print("VARIABLE", number)
            variable_name = line_split[line_split.index("VARIABLE") + 1]
            variable_type = None
            variable_value = None

            operator = "EQUALS"

            if "EQUALS" in line:
                # self.quick_print("-EQUALS", number)
                operator = "EQUALS"
                variable_type, variable_value = self.work_out_type(line, number)

                self.variable_dictionary[variable_name] = {"type": variable_type, "value": " ".join(line_split[line_split.index(operator) + 2:]), "value_type": line_split[line_split.index(operator) + 1]}

            elif "PLUS" in line:
                operator = "PLUS"
                if self.variable_dictionary[variable_name]["value_type"] == "INTEGER":
                    self.variable_dictionary[variable_name]["value"] = int(self.variable_dictionary[variable_name]["value"]) + int(line_split[line_split.index(operator) + 2])

            elif "MINUS" in line:
                operator = "MINUS"
                if self.variable_dictionary[variable_name]["value_type"] == "INTEGER":
                    self.variable_dictionary[variable_name]["value"] = int(self.variable_dictionary[variable_name]["value"]) - int(line_split[line_split.index(operator) + 2])

            elif "MULTIPLY" in line:
                operator = "MULTIPLY"
                if self.variable_dictionary[variable_name]["value_type"] == "INTEGER":
                    self.variable_dictionary[variable_name]["value"] = int(self.variable_dictionary[variable_name]["value"]) * int(line_split[line_split.index(operator) + 2])

            elif "DIVIDE" in line:
                operator = "DIVIDE"
                if self.variable_dictionary[variable_name]["value_type"] == "INTEGER":
                    self.variable_dictionary[variable_name]["value"] = int(self.variable_dictionary[variable_name]["value"]) // int(line_split[line_split.index(operator) + 2])

            elif "MODULUS" in line:
                operator = "MODULUS"
                if self.variable_dictionary[variable_name]["value_type"] == "INTEGER":
                    self.variable_dictionary[variable_name]["value"] = int(self.variable_dictionary[variable_name]["value"]) % int(line_split[line_split.index(operator) + 2])

    def is_variable(self, line, value):
        if "VARIABLE" in line[line.index(str(value)) - 1]:
            return True

        else:
            return False

    def work_out_type(self, line, number):
        item_type = "NONE"
        item_value = self.current_line_split

        if "VARIABLE" in self.current_line_split:
            # self.quick_print("--VARIABLE", number)
            if not self.found_variable:
                item_type = "VARIABLE"
                item_value = self.current_line_split[self.current_line_split.index("VARIABLE") + 1]

                del self.current_line_split[self.current_line_split.index("VARIABLE")]
                self.found_variable = True

            elif self.found_variable:
                if not self.found_value:
                    try:
                        item_type = "VARIABLE"
                        item_value = self.current_line_split[self.current_line_split.index("VARIABLE") + 1]

                        self.found_value = True

                    except ValueError:
                        pass

        elif "STRING" in self.current_line_split:
            # self.quick_print("--STRING", number)
            if not self.found_variable:
                item_type = "STRING"
                item_value = str(self.current_line_split[self.current_line_split.index("STRING") + 1])

                del self.current_line_split[self.current_line_split.index("STRING")]
                self.found_variable = True

            elif self.found_variable:
                if not self.found_value:
                    try:
                        item_type = "STRING"
                        item_value = str(self.current_line_split[self.current_line_split.index("STRING") + 1])

                        self.found_value = True

                    except ValueError:
                        pass

        elif "INTEGER" in self.current_line_split:
            # self.quick_print("--INTEGER", number)
            if not self.found_variable:
                item_type = "INTEGER"
                item_value = int(self.current_line_split[self.current_line_split.index("INTEGER") + 1])

            elif self.found_variable:
                if not self.found_value:
                    try:
                        item_type = "INTEGER"
                        item_value = int(self.current_line_split[self.current_line_split.index("INTEGER") + 1])

                        self.found_value = True

                    except ValueError:
                        pass

        elif "BOOLEAN" in self.current_line_split:
            # self.quick_print("--BOOLEAN", number)
            if not self.found_variable:
                item_type = "BOOLEAN"
                item_value = bool(self.current_line_split[self.current_line_split.index("BOOLEAN") + 1])

            elif self.found_variable:
                if not self.found_value:
                    try:
                        item_type = "BOOLEAN"
                        item_value = bool(self.current_line_split[self.current_line_split.index("BOOLEAN") + 1])

                        self.found_value = True

                    except ValueError:
                        pass

        elif "FLOAT" in self.current_line_split:
            # self.quick_print("--FLOAT", number)
            if not self.found_variable:
                item_type = "FLOAT"
                item_value = float(self.current_line_split[self.current_line_split.index("FLOAT") + 1])

            elif self.found_variable:
                if not self.found_value:
                    try:
                        item_type = "FLOAT"
                        item_value = float(self.current_line_split[self.current_line_split.index("FLOAT") + 1])

                        self.found_value = True

                    except ValueError:
                        pass

        return item_type, item_value

    def quick_print(self, *args):
        print("{} on line: {}.".format(args[0], args[1] + 1))


if __name__ == "__main__":
    Interpreter("./example.stre")
