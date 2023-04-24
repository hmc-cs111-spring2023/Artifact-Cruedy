import re
from matplotlib import colors

def shape_parser(lines, comp_name):
    name = ""
    for l in lines:
        if '{' in l and l[0] != '{':
            name = l[:l.index('{')]
            lines.remove(l)
            break
    end = lines.index("}")
    attributes = lines[:end]
    lines = lines[end+1:]
    name = name.replace("\"", "")
    # default values
    type = "solid"
    color = "black"
    width = "comp.width"
    height = "comp.height"
    unit = "comp.pixelAspect"
    time = "comp.duration"
    function = ""
    for a in attributes:
        sides = a.split("=")
        sides[0] = sides[0].replace(" ", "")
        sides[1] = sides[1].replace(" ", "")
        if sides[0] == 'type':
            type = sides[1]
            function = "add" + str(sides[1]).capitalize()
        elif sides[0] == 'color' and sides[1] != "black":
            color = sides[1]
        elif sides[0] == 'width' and sides[1] != "max":
            width = sides[1]
        elif sides[0] == 'height' and sides[1] != "max":
            height = sides[1]
        elif sides[0] == 'unit' and sides[1] != "pixel":
            unit = sides[1]
        elif sides[0] == 'time' and sides[1] != "max":
            time = sides[1]
    # Order: color, name, width, height, unit, time
    color = colors.to_rgba(color)
    color = color[:3]
    color_list = []
    for c in color:
        color_list.append(int(c))
    parameters = "(" + str(color_list) + ", " + "\"" + name + "\"" + ", " + width + ", " + height + ", " + unit + ", " + time + ")"
    return "var layer" + " = " + comp_name + ".layers." + function + parameters, lines