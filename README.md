# APM Toolbox – Automatic Pockmarks Mapping
DOI: https://doi.org/10.5281/zenodo.18454767

## Scientific summary

APM Toolbox is an ArcGIS Desktop add-in designed to automate the detection and morphometric characterization of seabed pockmarks from bathymetric datasets. It integrates standardized geoprocessing workflows into a reproducible pipeline that reduces manual interpretation time and supports marine geomorphological research.

This repository contains the official implementation of the APM Toolbox developed by the Grupo de Geociencias Marinas (IEO-CSIC).

## Installation

To install, double-click the Add-In file **AUTOMATIC_POCKMARK_MAPPING_201124.esriAddIn**. Once installed, the file is copied to:
`<user_directory>\Documents\ArcGIS\AddIns`.

Then, access the Add-In Manager from ArcMap via:  
`Menu > Customize > Add-In Manager`.

![APM Add-In](https://gemar-ieo.github.io/APM/Images/APM_addin.jpg)

To add the toolbar:

1. Go to `Menu > Customize > Toolbars > Automatic Pockmark Mapping`.
2. The toolbar will appear in ArcMap.

![APM Toolbar](https://gemar-ieo.github.io/APM/Images/APM_toolbar.jpg)

## Usage

Click on the added toolbox to select one of the following options:
1. **Bathymetric Raster Optimization**
2. **Pockmarks Mapping**
3. **Extraction of Pockmarks Parameters**

Each option includes several tools.

![APM Main Menu](https://gemar-ieo.github.io/APM/Images/APM_main_menu.jpg)

### 1.- Bathymetric Raster Optimization
This tool enhances the quality of bathymetric data by applying filters and hillshading. It smooths data with a low-pass filter to reduce noise and applies a hillshade to visualize the surface with improved lighting.

![Bathy Optimization](https://gemar-ieo.github.io/APM/Images/APM_bathy_optimizaton.jpg)

### 2.- Pockmarks Mapping
This tool automates the identification of seafloor depressions (pockmarks) in three stages:
- **Building the Bathymetric Position Index (BPI)**: This step calculates BPI values for highlighting depressions using adjustable radii.
- **Pockmark Extraction**: Depressions are identified with a customizable BPI threshold, then smoothed and analyzed for area, perimeter, and irregularity.
- **Selective Manual Cleaning**: Optionally, manually inspect and remove erroneous polygons for refinement.

![Pockmarks Mapping](https://gemar-ieo.github.io/APM/Images/APM_pockmars_mapping.jpg)

### 3.- Extraction of Pockmarks Parameters
This tool calculates geometric and morphological features of pockmarks:
- **Partial Extraction**: Computes parameters such as irregularity index, area, perimeter, and depth.
- **Final Extraction and Density Mapping**: Identifies low points, calculates final polygons, and generates a spatial density map using Kernel Density.

![Pockmarks Parameters](https://gemar-ieo.github.io/APM/Images/APM_extraction_parameters.jpg)

## TEST Folder and Data

In the `TEST` folder, you will find all the necessary data to perform the test using the **Automatic Pockmarks Mapping (APM)** tool. The folder contains the following:

1. **Bathymetry Data**: The bathymetry file **BAT_5m** with a 5-meter resolution covering the continental slope area of Murcia, Spain, is located in the `DATA` folder. This file is the starting point for all the operations.
   
2. **Instructions**: A detailed guide on how to run the test and use the APM tool is provided in the README_TEST.md file, located in the `TEST` folder.

3. **Images**: The images referenced in the test (such as screenshots of the interface and results) are stored in the `Images` folder within `TEST`. These images are used to visualize the steps and results of the process.

To begin, download the bathymetry file from the `DATA` folder, then follow the instructions in the README_TEST.md file for each step of the process.

## How to cite

If you use APM Toolbox in your research, please cite:

Fernández-Salas et al. (2026)  
APM Toolbox v1.0  
Zenodo DOI: https://doi.org/10.5281/zenodo.18454767

A software paper describing the toolbox is submitted to the Journal of Open Source Software (JOSS).

## License

This software is released under the GNU General Public License v3.0.

## Learn More

For more details about the **Automatic Pockmarks Mapping (APM)** tool, visit the [official website](https://gemar.ieo.csic.es/APM/).


