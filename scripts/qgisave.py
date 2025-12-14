import os
from qgis.core import (
    QgsProject,
    QgsRasterLayer,
    QgsRasterPipe,
    QgsRasterFileWriter
)

output_folder = "/Users/michelle/Documents/Fall '25/Capstone/NewPics"

project = QgsProject.instance()

for layer in project.mapLayers().values():
    if isinstance(layer, QgsRasterLayer):

        name = layer.name().replace(" ", "_")
        output_path = os.path.join(output_folder, f"{name}.tif")

        pipe = QgsRasterPipe()
        pipe.set(layer.dataProvider().clone())

        writer = QgsRasterFileWriter(output_path)
        writer.setOutputFormat("GTiff")
        writer.setCreateOptions(["COMPRESS=LZW"])

        writer.writeRaster(
            pipe,
            layer.width(),
            layer.height(),
            layer.extent(),
            layer.crs()
        )

        print(f"Saved: {output_path}")
