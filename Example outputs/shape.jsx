// Current composition
var comp = app.project.activeItem;

// Create new solid out of a New layer
var layer = comp.layers.addSolid([1, 0, 1], "My Solid", comp.width, comp.height, comp.pixelAspect, comp.duration);
layer.name = "My Solid";