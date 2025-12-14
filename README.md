# Capstone<!-- wp:paragraph -->
![Amazonian Rainforest](https://images.pexels.com/photos/975771/pexels-photo-975771.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=300 "Amazonian Rainforest")

<p>My name is Michelle Marchesini Vanegas. My project investigates deforestation in the Colombian Amazon and its relationship to the 2016 Colombian Peace Agreement. The Amazon rainforest is one of the most biodiverse ecosystems on Earth, yet in Colombia it faces intense pressure from illegal logging, cattle ranching, and coca cultivation. Armed conflict accelerated these activities by pushing illicit crops deeper into remote forests, resulting in widespread habitat loss and fragmentation. With the Peace Agreement came the expectation of reduced violence and environmental degradation, but its effectiveness  in curbing deforestation remains unclear.</p>
<!-- /wp:paragraph -->


<!-- wp:paragraph -->
<p>Using high-resolution PlanetScope imagery alongside Sentinel-2 and Landsat data, I will apply vegetation indices such as NDVI and NBR, as well as change detection techniques, to monitor land-use change in selected regions of the Colombian Amazon before and after 2016. My goal is to answer: Has the Peace Agreement contributed to measurable reductions in deforestation? Are there identifiable shifts in land use that correspond to coca eradication or alternative livelihood programs? By addressing these questions, I aim to provide timely, accurate insights into the environmental consequences of peacebuilding policies, support conservation planning, and develop an open-source tool that can empower local communities to monitor deforestation.</p>
<!-- /wp:paragraph -->
Data Sources:

1. [Earth Data:](https://www.earthdata.nasa.gov/data/catalog/ornl-cloud-landcover-colombian-amazon-1783-1) CMS: Landsat-derived Annual Land Cover Maps for the Colombian Amazon, 2001-2016
2. [Earth Data Prediction:](https://www.earthdata.nasa.gov/data/catalog/ornl-cloud-lc14-amazon-scenarios-1153-1#publications) Modeled Deforestation Scenarios, Amazon Basin: 2002-2050
# Land Cover Pixel Analysis Using Landsat

## Overview
This project processes classified **Landsat imagery** to quantify land cover types over a region of interest. Each image is categorized into land cover classes based on predefined map values. A Python script (`pixelcount.py`) counts the number of pixels in each class to estimate land cover distribution by area.

The final output is a CSV file listing:
- Layer (file) name
- Class value and name
- Pixel count
- Percentage coverage
- Area in hectares

---

## Data Classification
I obtained classified Landsat imagery and assigned land cover categories using the following map value definitions:

| Value | Class Name                     | Description |
|--------|--------------------------------|-------------|
| 0      | Unclassified                   | Lack of temporal segment after break in time series |
| 1      | Forest                         | Stable forest ecosystems |
| 2      | Natural grasslands             | Regions dominated by natural grass |
| 3      | Urban                          | Persistent urban areas |
| 4      | Pastures                       | Pasturelands and croplands introduced by humans |
| 5      | Secondary forest               | Regenerating vegetation (≥2 years) |
| 6      | Water                          | Rivers, lakes, and water bodies |
| 7      | Highly reflective surfaces     | Sandbanks, exposed rocks, reflective ground |

Each pixel represents **30m × 30m**, based on Landsat resolution.

---

## Pixel Counting Script

The file (`pixelcount.py`) reads each `.tif` file, counts the number of pixels per land cover class, and calculates area (in hectares) and percentage.


<!-- wp:paragraph -->
<p></p>
<!-- /wp:paragraph -->

<!-- wp:file {"id":10260,"href":"https://portfolios.cs.earlham.edu/wp-content/uploads/2025/09/capstone___Michelle_Marchesini-1.pdf"} -->
<div class="wp-block-file"><a href="https://portfolios.cs.earlham.edu/wp-content/uploads/2025/09/capstone___Michelle_Marchesini-1.pdf">capstone___Michelle_Marchesini-1</a><a href="https://portfolios.cs.earlham.edu/wp-content/uploads/2025/09/capstone___Michelle_Marchesini-1.pdf" class="wp-block-file__button" download>Download</a></div>
<!-- /wp:file -->
