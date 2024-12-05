# Automatic Pockmarks Mapping (APM) Test Instructions

In this test, we begin with the initial bathymetry, available in the `DATA` folder under the file **01_BATI_inicial.jpg**.

## Step 1: Bathymetry Raster Optimization

First, we clean the bathymetry and apply the Bathymetry Raster Optimization tool, followed by hillshading. The default parameters are Azimuth 315 and Altitude 45, as shown in the image below:

![Bathymetry Optimization](https://gemar-ieo.github.io/APM/test/Images/02_BLOQUE1_PANTALLA.jpg)

The result after filtering errors is shown in the following image:

![Optimized Bathymetry](https://gemar-ieo.github.io/APM/test/Images/03_BLOQUE1_RESULTADO.jpg)

## Step 2: Pockmarks Mapping

Next, we proceed with the Pockmarks Mapping tool, starting with the creation of the Bathymetric Position Index (BPI). The parameters used are radii of 20 and 100 for the continental slope zone of Murcia. The settings are shown in the image below:

![BPI Parameters](https://gemar-ieo.github.io/APM/test/Images/04_BLOQUE2A_PANTALLA.jpg)

The BPI result is shown in the following image:

![BPI Result](https://gemar-ieo.github.io/APM/test/Images/05_BLOQUE2A_RESULTADO.jpg)

## Step 3: Pockmark Extraction

We then move on to pockmark extraction with the following parameters:
- BPI threshold: -0.9
- Irregularity index threshold: 2.1

This step results in a shapefile of pockmarks, shown in the image below:

![Pockmark Extraction](https://gemar-ieo.github.io/APM/test/Images/06_BLOQUE2B_PANTALLA.jpg)

The extracted pockmarks are shown in the following image:

![Pockmark Extraction Result](https://gemar-ieo.github.io/APM/test/Images/07_BLOQUE2B_RESULTADO.jpg)

## Step 4: Selective Manual Cleaning

Optionally, pockmarks can be cleaned manually by inspecting and removing unwanted polygons. This process is illustrated in the image below:

![Selective Cleaning](https://gemar-ieo.github.io/APM/test/Images/08_BLOQUE2C_PANTALLA.jpg)

The result of the selective cleaning process is shown in the following image:

![Cleaned Pockmarks](https://gemar-ieo.github.io/APM/test/Images/10_BLOQUE2C_RESULTADO.jpg)

## Step 5: Extraction of Pockmarks Parameters

For this step, select the cleaned pockmarks shapefile and the optimized bathymetry. The settings are shown in the image below:

![Pockmarks Parameter Extraction](https://gemar-ieo.github.io/APM/test/Images/11_BLOQUE3A_PANTALLA.jpg)

This results in the first table with partial parameters, as shown below:

![Partial Parameters](https://gemar-ieo.github.io/APM/test/Images/12_BLOQUE3A_RESULTADO.jpg)

## Step 6: Final Extraction and Density Mapping

The final extraction and density mapping steps are shown with the following parameters:

![Final Extraction Settings](https://gemar-ieo.github.io/APM/test/Images/13_BLOQUE3B_PANTALLA.jpg)

The final results include the pockmark parameters shown below:

![Final Parameters](https://gemar-ieo.github.io/APM/test/Images/15_BLOQUE3B_RESULTADO2.jpg)

And the spatial density map of the pockmarks:

![Pockmark Density Map](https://gemar-ieo.github.io/APM/test/Images/14_BLOQUE3B_RESULTADO1.jpg)
