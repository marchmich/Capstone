# Capstone

![Amazonian Rainforest](https://images.pexels.com/photos/975771/pexels-photo-975771.jpeg?auto=compress\&cs=tinysrgb\&dpr=2\&h=300 "Amazonian Rainforest")

My name is **Michelle Marchesini Vanegas**. This capstone project investigates deforestation in the **Colombian Amazon** and its relationship to the **2016 Colombian Peace Agreement**. The Amazon rainforest is one of the most biodiverse ecosystems on Earth, yet in Colombia it faces intense pressure from illegal logging, cattle ranching, and coca cultivation. Armed conflict historically accelerated these activities by pushing illicit economies deeper into remote forested regions, resulting in widespread habitat loss and fragmentation. Following the Peace Agreement, expectations emerged around reduced violence and improved environmental protection; however, the extent to which deforestation trends changed after 2016 remains unclear.

This project combines **remote sensing**, **geospatial analysis**, and **computer science techniques** to quantify land-use change before and after the Peace Agreement and to evaluate whether policy shifts correspond to measurable environmental outcomes.

---

## Research Objectives

* Measure deforestation and land-cover change in selected regions of the Colombian Amazon before and after 2016
* Compare observed deforestation patterns with modeled future scenarios
* Assess whether post-conflict dynamics correspond to changes in forest loss
* Develop reproducible, open-source workflows for environmental monitoring

---

## Data Sources

1. **NASA EarthData – Observed Land Cover**
   [CMS: Landsat-derived Annual Land Cover Maps for the Colombian Amazon (2001–2016)](https://www.earthdata.nasa.gov/data/catalog/ornl-cloud-landcover-colombian-amazon-1783-1)

2. **NASA EarthData – Modeled Scenarios**
   [Modeled Deforestation Scenarios, Amazon Basin (2002–2050)](https://www.earthdata.nasa.gov/data/catalog/ornl-cloud-lc14-amazon-scenarios-1153-1#publications)

3. **Global Forest Watch – Independent Monitoring Platform**
   [Global Forest Watch: Colombia Forest Change Map](https://www.globalforestwatch.org/map/country/COL/?mainMap=eyJzaG93QW5hbHlzaXMiOnRydWV9)

   Global Forest Watch provides near–real-time forest loss data, policy context, and interactive spatial layers. In this project, it is used as a complementary reference to contextualize Landsat-based observations and modeled scenarios.

---

## Methodology Overview

Using **Landsat**, **Sentinel-2**, and **PlanetScope** imagery, this project applies:

* Vegetation indices (e.g., **NDVI**, **NBR**)
* Change detection techniques
* Pixel-based land-cover classification and counting

The workflow quantifies land-cover distribution and deforestation trends across multiple years, enabling comparison between observed data and projected scenarios. All analysis scripts are written in **Python**, with spatial preprocessing and visualization supported by **QGIS**.

---

## Land Cover Pixel Analysis Using Landsat

### Overview

Classified Landsat imagery is processed to quantify land cover types over a region of interest. Each image is categorized into land cover classes based on predefined map values. Pixel counts are converted into area estimates to measure land-cover distribution.

Each pixel represents **30 m × 30 m**, consistent with Landsat spatial resolution.

The final outputs include CSV files reporting:

* Raster (layer) name
* Land cover class value and name
* Pixel count
* Percentage coverage
* Area in hectares

---

### Land Cover Classification Scheme for Dataset #1

| Value | Class Name                 | Description                                         |
| ----: | -------------------------- | --------------------------------------------------- |
|     0 | Unclassified               | Lack of temporal segment after break in time series |
|     1 | Forest                     | Stable forest ecosystems                            |
|     2 | Natural grasslands         | Regions dominated by natural grass                  |
|     3 | Urban                      | Persistent urban areas                              |
|     4 | Pastures                   | Pasturelands and croplands introduced by humans     |
|     5 | Secondary forest           | Regenerating vegetation (≥ 2 years)                 |
|     6 | Water                      | Rivers, lakes, and water bodies                     |
|     7 | Highly reflective surfaces | Sandbanks, exposed rocks, reflective ground         |

### Land Cover Classification Scheme

| Value | Class Name                 | Description                                         |
| ----: | -------------------------- | --------------------------------------------------- |
|     0 | No Data              | Lack of temporal segment after break in time series |
|     1 | Deforestation | Regions with deforestation patterns             |
|     2 | Forest                     | Stable forest ecosystems                            |
|     3 | Non-Forest                     | Urban areas, Rivers, Lakes, Sandbanks, Exposed Rocks, or reflective ground                                 |
|

---

## Repository Structure

The repository is organized to clearly separate raw data, processed outputs, and analysis scripts used throughout the project.

* **`TIFF_original/`**
  Contains all original **cropped `.tif` files** corresponding specifically to the Colombian Amazon region. These files represent the raw raster inputs used for pixel counting, classification, and visualization.

* **`archives/`**
  Contains **processed and derived raster files**, including cleaned, reclassified, and transformed versions of the original `.tif` datasets. These files are generated through the analysis workflow and are preserved for reproducibility and comparison.

* **`scripts/`**
  Contains all Python and utility scripts used for data processing, analysis, and visualization (described below).

---

## Scripts

All scripts used in this project are located in the **`scripts/`** folder in the main repository. These scripts support raster processing, pixel analysis, visualization, and batch file handling.

* **`deforestation.py`**
  Performs pixel counting for the second data source using **4 color bands**, focused on deforestation classification.

* **`pixel_count.py`**
  Performs pixel counting for the second data source using **8 color bands**, enabling finer land-cover differentiation.

* **`qgisave.py`**
  Automates batch saving of QGIS project layers to a user-specified output folder.

* **`tiff_to_png.py`**
  Converts `.tif` raster files to `.png` format in batch. This script was used to generate image sequences for video creation.

* **`videolabel.py`**
  Adds legends and labels to raster images, enhancing the interpretability of visual outputs and videos.

---

## Capstone Document

The full written capstone report is available below:

[Download capstone___Michelle_Marchesini-1.pdf](https://portfolios.cs.earlham.edu/wp-content/uploads/2025/09/capstone___Michelle_Marchesini-1.pdf)

---

## Takeaway

This project demonstrates how **computer science and geospatial analysis** can be combined to study environmental change in post-conflict regions. By integrating observed satellite data, modeled scenarios, and independent monitoring platforms, the work provides a reproducible framework for analyzing deforestation and supports future conservation and policy evaluation efforts in the Colombian Amazon.
