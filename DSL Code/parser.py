# trim off the end of the string when it has spaces
# skip lines that have //
from shape_parser import *

def parser(file):
    f = open(file, "r")
    parse_lines = []
    for l in f:
        s = str(l)
        if '\n' in s:
            s = s.replace('\n', '')
        if s[:2] != "//" and s != "":
            parse_lines.append(s)
    while parse_lines != []:
        type = parse_lines[0]
        comp_name, comp_line, parse_lines = comp_parser(parse_lines[1:])
        first_line = "var " + comp_line
        script = open("shape.jsx","w")
        script.write(first_line + ";" + "\n")
        if type == "SHAPE":
            script_line, parse_lines = shape_parser(parse_lines, comp_name)
            script.write(script_line + ";" + "\n")
        elif type == "EFFECT":
            effect_parser(parse_lines[1:], comp_name)

def comp_parser(lines):
    comp_parts = lines[0].split(' = ')
    comp_name = comp_parts[0]
    comp_type = comp_parts[1]
    if comp_type == 'current_comp()':
        comp_type = 'app.project.activeItem'
    elif 'different_comp' in comp_type:
        index = comp_type[len(comp_type)-2:-1]
        comp_type = 'app.project.item(' + str(index) + ')'
    else:
        print("Error: Composition must be created first")
    return comp_name, comp_name + " = " + comp_type, lines [1:]

def effect_parser(lines, comp_name):
    print(lines)

parser("shape.txt")