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

Pockmarks are crater-like depressions on the seafloor formed by the focused expulsion of fluids such as methane or pore water. They are important indicators of active geological processes, seabed stability, and benthic habitat distribution [@Judd:2007]. High-resolution multibeam bathymetry now allows researchers to detect thousands of these features, but manual mapping is slow and inconsistent.

**Automatic Pockmarks Mapping (APM)** is an ArcGIS Desktop addins toolbox for Arcmap that automates the detection and morphometric characterization of seabed pockmarks. The software converts bathymetric digital elevation models into standardized geomorphological datasets through a reproducible workflow. APM is organized into three main stages: bathymetry optimization, pockmark delineation, and parameter extraction. The tool reduces operator bias and enables large-scale statistical analysis of pockmark fields while remaining accessible to users without advanced programming skills.

# Statement of need

Manual mapping of high-resolution multibeam data is **time-consuming and subjective**, which increases the risk of errors and limits consistency in subsequent analyses [@Andrews:2010; @Gafeira:2012]. While several methodologies for mapping pockmarks exist, there is a need for fast, objective, and free tools that minimize user involvement. **APM Toolbox** addresses this by providing a systematic methodology to identify, spatially delineate, and extract quantitative parameters of pockmarks regardless of the shape and size of the depression [@Gafeira:2018; @Picard:2018].

APM addresses the need for a standardized and objective workflow that integrates directly into a widely used GIS environment. The target audience includes marine geologists, geomorphologists, environmental agencies, and graduate students who require automated tools but may not have programming expertise. By providing repeatable detection and measurement procedures, APM supports quantitative comparisons between regions and time periods.

# State of the field

Several semi-automated approaches to pockmark mapping have been proposed. Script-based tools such as those of @Andrews:2010 provide flexibility but require coding expertise. GIS-based toolboxes developed by @Gafeira:2012 and @Gafeira:2018 demonstrated that automated pockmark characterization is feasible within ArcGIS environments. More recent work has used geomorphometric approaches to infer seabed processes from mapped depressions [@Picard:2018].

APM extends this line of research with a design focused on operational usability. Unlike workflows that assume flat terrain or require external dependencies, APM is packaged as a self-contained toolbox that operates on sloping continental margins and complex bathymetry. The software incorporates a robust irregularity filtering strategy derived from geomorphometric principles and emphasizes a hybrid approach combining automation with expert validation. This design choice reflects a “build vs. contribute” decision: APM was developed to solve practical limitations encountered in institutional workflows where existing tools could not be directly integrated or adapted.

# Software design

APM is implemented using ArcGIS Model Builder in a modular architecture that prioritizes transparency and reproducibility. The visual workflow allows users to inspect every processing step and adapt parameters to their datasets without modifying source code.

The pipeline consists of three components:

- **Optimization stage**: Digital elevation models are smoothed using focal statistics to suppress acquisition noise and avoid false detections during terrain analysis.

- **Feature delineation**: Pockmark rims are identified using the Bathymetric Position Index (BPI) [@Lundblad:2006]. A selective manual cleaning step is intentionally preserved to allow expert interpretation when natural depressions overlap with anthropogenic artifacts.

- **Geomorphometric engine**: The toolbox extracts geometric descriptors including area, depth, volume, eccentricity, and orientation. Orientation is computed using a longest-axis method consistent with previous geomorphometric studies [@Picard:2018], enabling interpretation of bottom current influence.

This architecture reflects a deliberate trade-off: while lower-level code could achieve marginal speed improvements, the chosen design maximizes accessibility, auditability, and long-term maintainability.


# Research impact statement

APM has been applied in the **EsMarEs** project (Marine Strategies in Spain, action C12A2), covering diverse test areas: Guadiaro Deep Fan, Capbreton Canyon, Murcia Slope, and Mallorca Channel.

It has been successfully employed in academic research, including the Master’s thesis by @SuaEscobar:2025, generating standardized geomorphological layers (shapefiles and density maps) for marine spatial planning. Benchmarks show APM can reduce analysis time by up to 80% relative to manual workflows. By providing reproducible workflows, APM bridges raw bathymetric data and high-level analyses necessary for environmental strategy and scientific research.

The software is actively maintained in a public repository and distributed under an open license, supporting community inspection, reuse, and extension.

# AI usage disclosure

No generative AI tools were used in the development of APM software. This manuscript was edited for structure and clarity with AI assistance, but all scientific content, geomorphological interpretations, and data were provided and verified by the authors.

# Acknowledgements

This work is a contribution to the **EsMarEs** project (Marine Strategies in Spain), action C12A2. We thank data sources including **LIFE IP-INTEMARES** (LIFE 15 IPE ES012) and **VIATAR** project (IEO), as well as all participants and crews of the R/V Ángeles Alvariño and R/V Ramón Margalef cruises.

# References
