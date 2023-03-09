#!/bin/python3
import cowsay
import argparse
import sys


class CowsayArgumentParser(argparse.ArgumentParser):
    '''
    Needed only for custom help message as
    the original class doesn't simply allow to change it
    '''

    def print_help(self):
        print("""Usage: cowsay [-bdgpstwy] [-h] [-e eyes] [-f cowfile]
          [-l] [-n] [-T tongue] [-W wrapcolumn] [message]""")


parser = CowsayArgumentParser(prog="cowsay")

parser.add_argument("-e", dest="eyes")
parser.add_argument("-f", dest="cow")
parser.add_argument("-l", dest="show_cow_list", action="store_true")
parser.add_argument("-n", dest="wrap_text", action="store_false")
parser.add_argument("-T", dest="tongue")
parser.add_argument("-W", dest="width", type=int)
parser.add_argument("-b", dest="preset", action="store_const", const="b")
parser.add_argument("-d", dest="preset", action="store_const", const="d")
parser.add_argument("-g", dest="preset", action="store_const", const="g")
parser.add_argument("-p", dest="preset", action="store_const", const="p")
parser.add_argument("-s", dest="preset", action="store_const", const="s")
parser.add_argument("-t", dest="preset", action="store_const", const="t")
parser.add_argument("-w", dest="preset", action="store_const", const="w")
parser.add_argument("-y", dest="preset", action="store_const", const="y")
parser.add_argument("message", nargs='*', default=sys.stdin)

parsed_args = parser.parse_args().__dict__


if parsed_args["show_cow_list"]:
    print(*cowsay.list_cows(), sep='\n')
    exit(0)

parsed_args["message"] = " ".join(parsed_args["message"])
args_drop_none = {}
for arg in parsed_args:
    if parsed_args[arg] is not None and arg != "show_cow_list":
        args_drop_none[arg] = parsed_args[arg]

print(cowsay.cowsay(**args_drop_none))
