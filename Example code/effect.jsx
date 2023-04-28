// Create a new composition
var comp = app.project.items.addComp("My Composition", 1920, 1080, 1.0, 10, 30);
// comp.openInViewer();

// Create a new solid layer
var layer = comp.layers.addSolid([1, 1, 0], "My Solid", comp.width, comp.height, comp.pixelAspect, comp.duration);

// Add the "Gaussian Blur" effect to the layer
var effect = layer.property("ADBE Effect Parade").addProperty("ADBE Gaussian Blur 2");
effect.name = "My Blur"; // Rename the effect
effect.property("ADBE Gaussian Blur 2-0001").setValue(20); // Set the blur amount to 20 pixels