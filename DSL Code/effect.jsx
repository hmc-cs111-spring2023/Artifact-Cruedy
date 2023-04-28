var comp = app.project.activeItem;
var layer = comp.selectedLayers[0];
var effect = layer.property("ADBE Effect Parade").addProperty("ADBE Gaussian Blur 2");
effect.property("ADBE Gaussian Blur 2-0001").setValue(20);
