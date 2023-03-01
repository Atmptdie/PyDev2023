import cowsay
import argparse

parser = argparse.ArgumentParser(prog="cowsay")


parser.add_argument("-e", dest="eyes")
parser.add_argument("-f", dest="cow")
parser.add_argument("-l", dest="show_cow_list", action="store_true")
parser.add_argument("-n", dest="wrap_text", action="store_true")
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
parser.add_argument("message")

