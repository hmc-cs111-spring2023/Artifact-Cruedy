def effect_parser(script, lines):
    if "current_layer" in lines[0]:
        script.write("var layer = comp.selectedLayers[0];" + "\n")
    lines = lines[1:]
    effect_des = lines[0].split("from")
    i = lines.index("}")
    properties = lines[1:i]
    lines = lines[i+1:]
    effect_name = effect_des[0]
    effect_name = effect_name.strip()
    effect_cate = effect_des[1]
    effect_cate = effect_cate[:len(effect_cate)-1]
    effect_cate = effect_cate.strip()
    script.write("var effect = layer.property(\"" + str(effect_cate) + "\").addProperty(\"" + str(effect_name) + "\")" + ";" + "\n")
    #script.close()
    value = ""
    for p in properties:
        attr = p.split("=")
        value = attr[1]
        value = value.replace(" ", "")
    script.write("effect.property(\"" + str(effect_name) + "-0001\").setValue(" + value + ");" + "\n")
    return lines