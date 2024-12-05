# Automatic Pockmarks Mapping (APM) Test Instructions

## Step 1: Download the Bathymetry Files
Before starting the process, download the bathymetry file **BAT_5m** from the `DATA` folder in the `TEST` directory. This file represents the bathymetry of the continental slope area of Murcia, Spain, with a 5-meter resolution.

## Step 2: Bathymetry Raster Optimization
Start by cleaning the bathymetry and applying the Bathymetry Raster Optimization tool, followed by hillshading. The default parameters are Azimuth 315 and Altitude 45, as shown in the image below:

![Bathymetry Optimization](https://gemar-ieo.github.io/APM/test/Images/02_BLOQUE1_PANTALLA.jpg)

The result after filtering errors is shown here:

![Optimized Bathymetry](https://gemar-ieo.github.io/APM/test/Images/03_BLOQUE1_RESULTADO.jpg)

## Step 3: Pockmarks Mapping
Now, proceed with the Pockmarks Mapping tool, starting with the creation of the Bathymetric Position Index (BPI). The parameters used are radii of 20 and 100 for the continental slope zone of Murcia. The settings are shown in the image below:

![BPI Parameters](https://gemar-ieo.github.io/APM/test/Images/04_BLOQUE2A_PANTALLA.jpg)

The result of the BPI is shown in the following image:

![BPI Result](https://gemar-ieo.github.io/APM/test/Images/05_BLOQUE2A_RESULTADO.jpg)

## Step 4: Pockmark Extraction
Proceed with pockmark extraction using the following parameters:
- BPI threshold: -0.9
- Irregularity index threshold: 2.1

This step results in a shapefile of pockmarks, shown below:

![Pockmark Extraction](https://gemar-ieo.github.io/APM/test/Images/06_BLOQUE2B_PANTALLA.jpg)

The extracted pockmarks are displayed in the image below:

![Pockmark Extraction Result](https://gemar-ieo.github.io/APM/test/Images/07_BLOQUE2B_RESULTADO.jpg)

## Step 5: Selective Manual Cleaning
Optionally, perform selective manual cleaning of the pockmarks by inspecting and removing unwanted polygons. This process is shown below:

![Selective Cleaning](https://gemar-ieo.github.io/APM/test/Images/08_BLOQUE2C_PANTALLA.jpg)

The cleaned pockmarks are displayed here:

![Cleaned Pockmarks](https://gemar-ieo.github.io/APM/test/Images/10_BLOQUE2C_RESULTADO.jpg)

## Step 6: Extraction of Pockmarks Parameters
Select the cleaned pockmarks shapefile and the optimized bathymetry for this step. The settings are shown below:

![Pockmarks Parameter Extraction](https://gemar-ieo.github.io/APM/test/Images/11_BLOQUE3A_PANTALLA.jpg)

The first table with partial parameters is shown here:

![Partial Parameters](https://gemar-ieo.github.io/APM/test/Images/12_BLOQUE3A_RESULTADO.jpg)

## Step 7: Final Extraction and Density Mapping
For the final extraction and density mapping, configure the parameters as shown below:

![Final Extraction Settings](https://gemar-ieo.github.io/APM/test/Images/13_BLOQUE3B_PANTALLA.jpg)

The final pockmark parameters are displayed here:

![Final Parameters](https://gemar-ieo.github.io/APM/test/Images/15_BLOQUE3B_RESULTADO2.jpg)

Finally, the spatial density map of the pockmarks is shown in the image below:

![Pockmark Density Map](https://gemar-ieo.github.io/APM/test/Images/14_BLOQUE3B_RESULTADO1.jpg)
