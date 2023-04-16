def parser(file):
    f = open(file, "r")
    parse_lines = []
    for l in f:
        s = str(l)
        if '\n' in s:
            s = s.replace('\n', '')
        if s[:2] != "//" and s != "":
            parse_lines.append(s)
    if parse_lines[0] == "SHAPE":
        shape_parser(parse_lines[1:])
    elif parse_lines[0] == "EFFECT":
        effect_parser(parse_lines)

def shape_parser(lines):
    # need to check if the first line selects the composition
    print(lines)
    first_line = lines[0]
    comp_parts = first_line.split(' = ')
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
    print(first_line)

def effect_parser():
    
parser("shape.txt")


#script = open('script.jsx', 'w')


