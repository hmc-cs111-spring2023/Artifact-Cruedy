# trim off the end of the string when it has spaces
# skip lines that have //
from shape_parser import *
from comp_parser import *
from effect_parser import *

def parser(input_file, output_file):
    f = open(input_file, "r")
    parse_lines = []
    for l in f:
        s = str(l)
        if '\n' in s:
            s = s.replace('\n', '')
        if s[:2] != "//" and s != "":
            parse_lines.append(s)
    type = parse_lines[0]
    script = open(output_file,"w")
    comp_line, parse_lines = comp_parser(parse_lines[1:])
    first_line = "var " + comp_line
    script.write(first_line + ";" + "\n")
    while parse_lines != []:
        if parse_lines[0] == "EFFECT" or parse_lines[0] == "SHAPE":
            type = parse_lines[0]
            parse_lines = parse_lines[1:]
        if type == "SHAPE":
            parse_lines = shape_parser(script, parse_lines)
        elif type == "EFFECT":
            parse_lines = effect_parser(script, parse_lines)
        else:
            print("Must specify type correctly")
    script.close()

parser("files/solid.txt", "files/solid.jsx")