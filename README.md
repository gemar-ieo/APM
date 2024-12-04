# AUTOMATIC POCKMARKS MAPPING (APM)

Automatic Pockmarks Mapping (APM) is an add-in for ArcGis Desktop developed by Grupo de Geociencias Marinas of the Instituto Español de Oceanografía (IEO-CSIC).  The application provides a set of geoprocessing tools for automating the task of mapping pockmarks and extracting some geomorphometric parameters. 

## Installation
To install them simply double click the Add-In file **AUTOMATIC_POCKMARK_MAPPING_201124.esriAddIn**. Once installed, it is not necessary to keep the Add-In file in the computer, it will be copied to *"<user_directory>\Documents\ArcGIS\AddIns"*.

Then, they should appear in the Add-In Manager of ArcMap , under *Menu > Customize > Add-In Manager*.

<img src="https://gemar-ieo.github.io/APM/Images/APM_addin.jpg" />

To add tool:

1. Go to *Menu > Customize > Toolbars>Automatic Pockmark Mapping. 
2. The toolbar appears in ArcMap

<img src="https://gemar-ieo.github.io/APM/Images/APM_toolbar.jpg" />

## Usage

To use the Add-In simply click on the added toolbox and select the options: a)Bathymetric Raster Optimization, b)Pockmarks Mapping, and c)Extraction of Pockmarks Parameters. Each option includes several tools.

<img src="https://gemar-ieo.github.io/APM/Images/APM_main_menu.jpg" />

+ **Bathymetric Raster Optimization:** The Bathymetry Raster Optimization tool enhances the quality and visualization of bathymetric data by applying optional filtering and hillshading techniques. First, a low-pass filter smooths the data reducing noise and eliminating anomalies. Next, the hillshade tool generates a visually enhanced surface by simulating illumination based on user-defined light source parameters. This streamlined process ensures high-quality Digital Elevation Models (DEMs) and improved data visualization, making it an essential tool for bathymetric analysis.

<img src="https://gemar-ieo.github.io/APM/Images/APM_bathy_optimizaton.jpg" />

+ **Pockmarks Mapping:** The Pockmark Mapping Tool automates and refines the identification and analysis of seafloor depressions called pockmarks. It operates in three stages:

1.- Building the Bathymetric Position Index (BPI): This calculates BPI values to highlight depressions, using an annulus-shaped analysis with adjustable radii for precise mapping. 

2.- Pockmark Extraction: Depressions are identified using a customizable BPI threshold (-0.9 by default), converted into polygons, smoothed for cartographic quality, and analyzed for area, perimeter, and irregularity index to characterize their morphology.

3.- Selective Manual Cleaning (Optional): Users can visually inspect and remove erroneous polygons, refining results to align with expert criteria.

The tool produces high-quality, customizable pockmark maps ready for further geological analysis.

<img src="https://gemar-ieo.github.io/APM/Images/APM_pockmars_mapping.jpg" />


+ **Extraction of Pockmarks Parameters:** The Pockmark Parameter Extraction Tool calculates and refines key geometric and morphological features of seafloor pockmarks in two phases:

1.-Partial Extraction: This phase computes essential parameters such as irregularity index, width, length, orientation, area, perimeter, and mean and minimum depths. Steps include adding depth data to pockmark polygons, calculating dimensions and depth statistics, removing invalid pockmarks, and cleaning irrelevant data fields for a refined dataset.

2.- Final Extraction and Density Mapping: Low points for each pockmark are identified, prioritizing proximity to polygon centroids to account for seafloor gradients. Final pockmark polygons are generated with height data and classified as single or multiple pockmarks. Finally, a spatial density map is produced using the Kernel Density tool, offering a comprehensive visualization of pockmark distribution.

<img src="<img src="https://gemar-ieo.github.io/APM/Images/APM_extraction_parameters.jpg" />" />


## References (reference will be updated when published)

Fernández-Salas, L.M., Sánchez-Guillamón, O., Villar-Menéndez, I., Díez-García, I.P., Arrese, B. and Sayago-Gil, M.(send to publish).From Manual to Automatic: Using ArcGIS Model Builder to Efficiently Map and Characterize Pockmarks.Computers & Geosciences, xxx(xxx), xxx. https://doi.org/xxxx


