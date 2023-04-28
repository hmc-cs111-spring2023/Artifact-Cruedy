var comp = app.project.items.addComp("My Composition" , 1920, 1080, 1.0, 5, 30);
var layer = comp.layers.addSolid([1, 1, 0], "My Solid ", comp.width, comp.height, comp.pixelAspect, comp.duration);
var effect = layer.property("ADBE Effect Parade").addProperty("ADBE Gaussian Blur 2");
effect.property("ADBE Gaussian Blur 2-0001").setValue(20);
