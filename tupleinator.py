# got too tired from replacing every warn() call that has or does not have
# arguments since tuples were created in zig 0.6.0? don't worry, i'm here
# for you
#
# this script is a source-2-source translator from code that doesn't use
# tuples on warn() calls to code that does use them.
#
# this code is in the public domain
# written by lun-4, github.com/lun-4
import re
import sys

w = lambda x: sys.stderr.write(x + "\n")
out = lambda x: sys.stdout.write(x)


def process(f):
    lines = f.readlines()
    iterator = iter(lines)

    w(repr(lines))

    wanted_functions = ["warn", "doError", "setErrContext", "print"]
    index = 0

    full_line: str = ""
    for line in iterator:
        index += 1
        w("single line iter: " + str(index) + " " + repr(line))
        full_line: str = line

        # don't consume lines that don't have warns in them

        break_loop = True
        for func_name in wanted_functions:
            if func_name + "(" in line:
                break_loop = False

        if break_loop:
            w("broke from no func")
            out(full_line)
            continue

        # don't consume lines with tuples already
        if ".{" in line:
            w("broke from tuple")
            out(line)
            continue

        param_counter = 1

        while ";" not in full_line:

            # this stops the code from before that considered
            # function calls to be full on warn stops in the line and so
            # the code didn't notice the end warn()
            param_counter = 0
            stop = False
            for char in full_line:
                if char == "(":
                    param_counter += 1
                if char == ")":
                    param_counter -= 1
                if param_counter == 0:
                    stop = True

            if stop:
                break

            try:
                full_line += next(iterator)
                w("extend line for semicolon" + full_line + " END")
            except StopIteration:
                w("got eof")
                out(full_line)
                break

        line = full_line

        # try to find if that warn has actual strings in it and it isnt
        # an alias or smth
        try:
            start_quote = line.index('"')
        except ValueError:
            w("quote not found")
            out(line)
            continue

        # try to find the possible start and and markers for many
        # parts of a warn() call
        end_quote = line.index('"', start_quote + 1)

        possible_tuple_chars = (
            line[end_quote + 1],
            line[end_quote + 2],
            line[end_quote + 3],
        )

        try:
            comma_index = end_quote + possible_tuple_chars.index(",") + 1
        except ValueError:
            comma_index = end_quote + 1

        try:
            end_semicolon = line.index(";")
            end_char = ";"
        except ValueError:
            # assume branch of switch
            end_semicolon = line.rindex(",")
            end_char = ","

        end_paren = end_semicolon - 1
        w(str(comma_index))
        line_result = f"{line[:comma_index]} , .{{ {line[comma_index + 1:end_paren]} }}){end_char}\n"
        w("line = " + line + " => result = " + line_result)
        out(line_result)


def main():
    with open(sys.argv[1], "r") as f:
        process(f)


if __name__ == "__main__":
    main()
