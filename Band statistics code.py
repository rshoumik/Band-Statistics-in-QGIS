#Use this to get Band Statistics for your raster layer in QGIS
import csv
from qgis.core import QgsRasterBandStats

# Path to create or overwrite csv file
text_file_path = "C:/Users/You/Desktop//result.csv"

with open(text_file_path, 'wb') as csvfile:
    # fieldnames will be the column names in the csv
    fieldnames = ['Statistic', 'Value']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    layers = QgsMapLayerRegistry.instance().mapLayers().values()
    writer.writeheader()
    # Iterate through all layers in the layer panel
    for layer in layers:
        # Fetch name, data, extent and stats from each layer
        name = layer.name()
        provider = layer.dataProvider()
        ext = layer.extent()
        stats = provider.bandStatistics(1,QgsRasterBandStats.All,ext,0)
        # Begin with empty row then populate following rows with statistics
        writer.writerow({'Statistic': '', 'Value': ''})
        writer.writerow({'Statistic': 'Raster Name', 'Value': layer.name()})
        writer.writerow({'Statistic': 'Band Number', 'Value': stats.bandNumber})
        writer.writerow({'Statistic': 'Mean', 'Value': stats.mean})
        writer.writerow({'Statistic': 'Std Dev', 'Value': stats.stdDev})
        writer.writerow({'Statistic': 'Sum', 'Value': stats.sum})
        writer.writerow({'Statistic': 'Sum of Squares', 'Value': stats.sumOfSquares})
        writer.writerow({'Statistic': 'Minimum', 'Value': stats.minimumValue})
        writer.writerow({'Statistic': 'Maximum', 'Value': stats.maximumValue})
        writer.writerow({'Statistic': 'Range', 'Value': stats.range})