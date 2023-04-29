
def comp_parser(lines):
    comp_parts = []
    comp_name = ''
    comp_type = ''
    new = True
    # checks if it selects an already existing composition
    for l in lines:
        if 'different_comp' in l or 'current_comp' in l:
            new = False
            break
    if new == False:
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
        lines = lines[i+1:]
    if comp_type == 'current_comp()':
        comp_type = 'app.project.activeItem'
    elif 'different_comp' in comp_type:
        index = comp_type[len(comp_type)-2:-1]
        comp_type = 'app.project.item(' + str(index) + ')'
    elif '\"' in comp_name:
        # default values
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
        return "comp = app.project.items.addComp(" + comp_name + ", " + str(width) + ", " + str(height) + ", " + str(pixel) + ", " + str(duration) + ", " + str(framerate) + ")", lines
    else:
        print("Error: Composition must be created first")
    return comp_name + " = " + comp_type, lines