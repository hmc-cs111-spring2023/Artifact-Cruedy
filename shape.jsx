// Current composition
var comp = app.project.activeItem;

// Create new solid out of a New layer
var layer = comp.layers.addSolid([1, 0, 1], "My Solid", comp.width, comp.height, comp.pixelAspect, comp.duration);

// Layer exists for 10 seconds
layer.outPoint = 10;
layer.name = "My Solid";