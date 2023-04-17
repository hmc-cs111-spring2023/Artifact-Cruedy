# trim off the end of the string when it has spaces
# skip lines that have //
def parser(file):
    f = open(file, "r")
    parse_lines = []
    for l in f:
        s = str(l)
        if '\n' in s:
            s = s.replace('\n', '')
        if s[:2] != "//" and s != "":
            parse_lines.append(s)
    type = parse_lines[0]
    comp = parse_lines[1]
    comp_parts = comp.split(' = ')
    comp_name = comp_parts[0]
    comp_type = comp_parts[1]
    if comp_type == 'current_comp()':
        comp_type = 'app.project.activeItem'
    elif 'different_comp' in comp_type:
        index = comp_type[len(comp_type)-2:-1]
        comp_type = 'app.project.item(' + str(index) + ')'
    else:
        print("Error: Composition must be created first")
    first_line = comp_name + " = " + comp_type
    script = open("shape.jsx","w")
    script.write(first_line)
    if type == "SHAPE":
        shape_parser(parse_lines[2:])
    elif type == "EFFECT":
        effect_parser(parse_lines[2:])

def shape_parser(lines):
    name = ""
    for l in lines:
        if '{' in l and l[0] != '{':
            name = l[:l.index('{')]
            lines.remove(l)
            break
    end = lines.index("}")
    attributes = lines[:end]
    name = name.replace("\"", "")
    

def effect_parser(lines):
    print(lines)
    
parser("shape.txt")