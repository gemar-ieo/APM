---
title: 'APM: An ArcGIS Model Builder toolbox to efficiently map and characterize pockmarks'
tags:
  - ArcGIS
  - marine geomorphology
  - pockmarks
  - geomorphometry
  - multibeam bathymetry
authors:
  - name: Luis Miguel Fernández-Salas
    orcid: 0000-0001-9689-0084
    affiliation: 1
  - name: Olga Sánchez-Guillamón
    orcid: 0000-0002-3068-6176
    affiliation: 2
  - name: Izaskun Villar-Menéndez
    orcid: 0009-0004-6915-5489
    affiliation: 3
  - name: Irene Díez-García
    orcid: 0000-0003-4555-6291
    affiliation: 4
  - name: Beatriz Arrese
    orcid: 0000-0003-0260-8020
    affiliation: 5
  - name: Miriam Sayago-Gil
    orcid: 0000-0002-3655-0798
    corresponding: true
    affiliation: 1
affiliations:
  - name: Instituto Español de Oceanografía (IEO-CSIC), Centro Oceanográfico de Cádiz, Muelle Pesquero S/N, 11006 Cádiz, Spain.
    index: 1
  - name: Instituto Español de Oceanografía (IEO-CSIC), Centro Oceanográfico de Málaga,Explanada de San Andrés (Muelle 9) 29002 Puerto de Málaga. Málaga, Spain.
    index: 2
  - name: Instituto Español de Oceanografía (IEO-CSIC), Centro Oceanográfico de Gijón, Av. del Príncipe de Asturias, 70 Bis, Gijon-Oeste, 33212 Gijón, Asturias. Spain.
    index: 4
  - name: Instituto Español de Oceanografía (IEO-CSIC), Centro Oceanográfico de Vigo, Subida a Radio Faro, 50-52, 36390 Vigo, Pontevedra. Spain.
    index: 4
  - name: Instituto Español de Oceanografía (IEO-CSIC), Servicios Centrales, Madrid, C/ Corazón de María, 8, 28002 Madrid, Spain.
date: 2 February 2026
bibliography: paper.bib
---

# Summary

Pockmarks are crater-like depressions on the seafloor caused by the focused migration of fluids (typically methane) from sub-seabed sediments into the water column [@Judd:2007]. Since their first documentation on the Scotian Shelf [@King:1970], they have been identified worldwide in diverse geological settings, ranging from continental shelves to deep oceans. The analysis of these features is crucial for understanding fluid flow processes, seafloor stability, and marine ecosystems.

The **Automatic Pockmarks Mapping (APM)** tool is a semi-automated toolbox developed within the ArcGIS environment. It integrates multiple geoprocessing functions into a systematic workflow to identify pockmarks and extract their quantitative parameters from high-resolution multibeam bathymetry data. The tool is designed to standardize the mapping process, reducing the subjectivity and time consumption associated with manual interpretation.

# Statement of need

Characterizing pockmark fields manually is a time-consuming and subjective task, prone to inconsistencies, especially when dealing with large datasets or high-density fields. While the availability of high-quality digital bathymetry has opened opportunities for automation, existing tools often present challenges. Some methodologies rely on closed-source software or require complex scripting in environments like R or MATLAB, which may have a steeper learning curve for some marine geoscientists.

Previous efforts, such as those by @Andrews:2010, @Gafeira:2012, and @Gafeira:2018, established the foundations for semi-automated mapping. However, some of these approaches are limited by software accessibility or specific morphological assumptions (e.g., handling of pockmark rims on sloping terrains).

APM addresses these needs by providing a user-friendly, open-source add-in directly integrated into **ESRI ArcGIS**, a standard software in marine geology. It allows researchers to:
1.  Rapidly simulate different detection criteria (e.g., varying BPI radii).
2.  Objectively delineate pockmark boundaries using the Bathymetric Position Index (BPI).
3.  Automatically extract key morphometric parameters (basal area, perimeter, depth, azimuth).
4.  Generate spatial density maps.

A distinct feature of APM is its robust handling of "low points." Unlike methods that simply select the deepest pixel—which can be misleading on sloping seafloors—APM identifies the low point closest to the pockmark's centroid, ensuring more accurate morphological characterization.

# Software description

The APM tool is implemented using **ArcGIS Model Builder**, enabling a visual and modular execution of geoprocessing workflows. The toolbox is structured into three primary functions:

1.  **Bathymetry Raster Optimization**: An optional step that prepares the input Digital Elevation Model (DEM) by applying low-pass filters to smooth data artifacts and generating hillshade layers to enhance visual interpretation.
2.  **Pockmark Mapping**: This core function utilizes the BPI algorithm [@Lundblad:2006] to detect concave features. It converts these features into polygons and performs initial filtering based on thresholds for basal area and an **Irregularity Index** [@Grosse:2009]. This stage allows for a "Selective Manual Cleaning" step, where the user can visually inspect and remove artifacts (e.g., contouritic moats or data errors) before final parameter calculation.
3.  **Pockmark Parameters Extraction**: The final stage computes morphometric variables for each identified feature, including width, length, orientation, and specific depth metrics. It produces a final shapefile of pockmarks, a dataset of their associated low points, and a Kernel Density map of the field.

![Flowchart illustrating the sequential stages of the APM tool workflow.](https://github.com/gemar-ieo/APM/blob/main/Images/flowchart.png)

# Reliability and Research Application

The efficacy of the APM tool was validated through a comparative analysis with expert manual mapping across four distinct case studies on the Spanish continental margin: the Guadiaro Deep Fan, Capbreton Canyon, Murcia Slope, and Mallorca Channel. These areas represent diverse geomorphological contexts, from rugged canyons to smoother continental slopes.

Results demonstrated that APM significantly reduces processing time while maintaining high statistical agreement with manual measurements. For instance, in the **Murcia Slope** case study, the tool successfully identified 95% of the manually delineated features in simple settings. The comparison of morphometric parameters, such as Basal Area and Perimeter, showed a strong positive correlation (close to a 1:1 ratio) between the automated and manual methods, particularly for isolated, simple pockmarks.

While complex, clustered pockmark chains remain a challenge for any automated algorithm, APM's modular design allows users to optimize BPI parameters to better separate individual features or merged structures. The tool has been proven robust for standardizing pockmark characterization and is currently available to the scientific community to facilitate reproducible marine geomorphological research.

# Acknowledgements

This work is a contribution to the EsMarEs project (Marine Strategies in Spain), and more specifically to action C12A2, "Characterization of the nature and composition of the seabed in marine demarcations and generation of information layers for better management." We would like to thank the projects from which the data originated, such as LIFE IP-INTEMARES (LIFE 15 IPE ES012) and the VIATAR project (IEO). The authors thank all participants and crews of the Spanish Institute of Oceanography-IEO cruises on board the R/V Ángeles Alvariño and R/V Ramón Margalef.

# References
