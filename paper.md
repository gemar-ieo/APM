---
title: 'APM: An ArcGIS Model Builder toolbox to efficiently map and characterize pockmarks'
tags:
  - Gis addins
  - marine geomorphology
  - pockmarks mapping
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
    affiliation: 1
affiliations:
  - name: Instituto Español de Oceanografía (IEO-CSIC), Centro Oceanográfico de Cádiz, Muelle Pesquero S/N, 11006 Cádiz, Spain.
    index: 1
  - name: Instituto Español de Oceanografía (IEO-CSIC), Centro Oceanográfico de Málaga, Explanada de San Andrés (Muelle 9) 29002 Puerto de Málaga, Málaga, Spain.
    index: 2
  - name: Instituto Español de Oceanografía (IEO-CSIC), Centro Oceanográfico de Gijón, Av. del Príncipe de Asturias, 70 Bis, Gijon-Oeste, 33212 Gijón, Asturias. Spain.
    index: 3
  - name: Instituto Español de Oceanografía (IEO-CSIC), Centro Oceanográfico de Vigo, Subida a Radio Faro, 50-52, 36390 Vigo, Pontevedra, Spain.
    index: 4
  - name: Instituto Español de Oceanografía (IEO-CSIC), Servicios Centrales, Madrid, C/ Corazón de María, 8, 28002 Madrid, Spain.
    index: 5
date: 2 February 2026
bibliography: paper.bib
---

# Summary

**Automatic Pockmarks Mapping (APM)** is an ArcGIS Desktop add-in designed to automate the detection and morphometric characterization of seabed pockmarks from bathymetric datasets [@Gafeira:2012; @Gafeira:2018]. The tool integrates standardized geoprocessing workflows into a reproducible pipeline that reduces manual interpretation time. APM is structured into three main functions: **Bathymetry Raster Optimization**, **Pockmark Mapping**, and **Pockmark Parameters Extraction** [@Andrews:2010; @Picard:2018].

# Statement of need

Manual mapping of high-resolution multibeam data is **time-consuming and subjective**, which increases the risk of errors and limits consistency in subsequent analyses [@Andrews:2010; @Gafeira:2012]. While several methodologies for mapping pockmarks exist, there is a need for fast, objective, and free tools that minimize user involvement. **APM Toolbox** addresses this by providing a systematic methodology to identify, spatially delineate, and extract quantitative parameters of pockmarks regardless of the shape and size of the depression [@Gafeira:2018; @Picard:2018].

# State of the field

Several tools have been developed for pockmark mapping, such as those by **Andrews et al. (2010)**, **Gafeira et al. (2012, 2018)**, and **Picard et al. (2018)** [@Andrews:2010; @Gafeira:2012; @Gafeira:2018; @Picard:2018]. However, many of these rely on proprietary tools or require simplified terrain assumptions that limit their applicability in irregular submarine environments [@Gafeira:2012; @Picard:2018]. Unlike these, APM is distributed as **free software under the GNU GPL v3.0 license** and focuses on a balance between automation and expert judgment during the manual cleaning phase [@Gafeira:2018].

# Software design

APM employs a modular design using ArcGIS Model Builder, balancing **performance** with **usability and transparency** [@Gafeira:2018]. The visual workflow allows researchers to inspect every processing step, which is crucial for reproducibility in scientific studies.

Key components include:

- **Optimization Stage**: Applies focal statistics to reduce noise in DEMs, ensuring Bathymetric Position Index (BPI) calculations do not produce false positives [@Lundblad:2006].  
- **Feature Delineation**: Uses BPI to define pockmark rims, with a selective manual cleaning step to allow human expertise in distinguishing pockmarks from artifacts [@Lundblad:2006; @Gafeira:2018].  
- **Geomorphometric Engine**: Automatically extracts >12 parameters, including orientation via the "Longest Axis" method, which is critical for interpreting seabed currents [@Picard:2018].

# Research impact statement

APM has been applied in the **EsMarEs** project (Marine Strategies in Spain, action C12A2), covering diverse test areas: Guadiaro Deep Fan, Capbreton Canyon, Murcia Slope, and Mallorca Channel.

It has been successfully employed in academic research, including the Master’s thesis by @SuaEscobar:2025, generating standardized geomorphological layers (shapefiles and density maps) for marine spatial planning. Benchmarks show APM can reduce analysis time by up to 80% relative to manual workflows. By providing reproducible workflows, APM bridges raw bathymetric data and high-level analyses necessary for environmental strategy and scientific research.

# AI usage disclosure

No generative AI tools were used in the development of APM software. This manuscript was edited for structure and clarity with AI assistance, but all scientific content, geomorphological interpretations, and data were provided and verified by the authors.

# Acknowledgements

This work is a contribution to the **EsMarEs** project (Marine Strategies in Spain), action C12A2. We thank data sources including **LIFE IP-INTEMARES** (LIFE 15 IPE ES012) and **VIATAR** project (IEO), as well as all participants and crews of the R/V Ángeles Alvariño and R/V Ramón Margalef cruises.

# References
