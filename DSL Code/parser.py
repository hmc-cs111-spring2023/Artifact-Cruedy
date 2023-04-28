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
        script = open("new_comp.jsx","w")
        script.write(first_line + ";" + "\n")
        if type == "SHAPE":
            script_line, parse_lines = shape_parser(parse_lines, comp_name)
            script.write(script_line + ";" + "\n")
        elif type == "EFFECT":
            effect_parser(parse_lines[1:], comp_name)

def comp_parser(lines):
    comp_parts = []
    comp_name = ''
    comp_type = ''
    if 'different_comp' in lines or 'current_comp' in lines:
        comp_parts = lines[0].split(' = ')
        comp_name = comp_parts[0]
        comp_type = comp_parts[1]
        lines = lines[1:]
    else:
        i = lines.index('}')
        li = lines[:i]
        comp_parts = li[0].split(' = ')
        comp_name = comp_parts[1]
        comp_name = comp_name[:len(comp_name)-1]
        comp_type = li[1:]
        print(comp_type)
        lines = lines[i+1:]
    if comp_type == 'current_comp()':
        comp_type = 'app.project.activeItem'
    elif 'different_comp' in comp_type:
        index = comp_type[len(comp_type)-2:-1]
        comp_type = 'app.project.item(' + str(index) + ')'
    elif '\"' in comp_name:
        width = "1920"
        height = "1080"
        pixel = "1.0"
        duration = "5"
        framerate = "30"
        for t in comp_type:
            att_parts = t.split(" = ")
            if att_parts[0] == "width":
                width = att_parts[1]
            elif att_parts[0] == "height":
                height = att_parts[1]
            elif att_parts[0] == "pixel":
                pixel = att_parts[1]
            elif att_parts[0] == "duration":
                duration = att_parts[1]
            else:
                framerate = att_parts[1]
        return "comp = app.project.items.addComp(" + comp_name + ", " + str(width) + ", " + str(height) + ", " + str(pixel) + ", " + str(duration) + ", " + str(framerate)
    else:
        print("Error: Composition must be created first")
    return comp_name, comp_name + " = " + comp_type, lines

def effect_parser(lines, comp_name):
    print(lines)

parser("new_comp.txt")