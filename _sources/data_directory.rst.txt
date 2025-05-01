Data Directory
==============

This section outlines the structure and contents of the project's data directory.

Directory Structure
-------------------

.. code-block::

    data/
    ├── raw/
    │   ├── terraclimate/
    │   │   ├── tmax_2020.nc
    │   │   └── ...
    │   └── cmip6/
    │       ├── SSP585/
    │       │   ├── tasmax_2030.nc
    │       │   ├── tasmax_2050.nc
    │       │   └── ...
    ├── interim/
    │   └── harmonized_climate/
    └── processed/
        ├── suitability_layers/
        └── dashboards/

Data Sources
------------

- **Terraclimate**
  [https://www.climatologylab.org/terraclimate.html](https://www.climatologylab.org/terraclimate.html)
  Used for current historical baseline (e.g., 2000–2020) of temperature, precipitation, etc.

- **CMIP6 Models**
  Acquired via Copernicus or ESGF data portals. Focused on `SSP585` and `SSP245` scenarios for 2030 and 2050 projections.

Storage & Access
----------------

- All large raster datasets are stored in an AWS S3 bucket for scalable access.
- Vector data is stored in a shared PostGIS database and accessed programmatically.

File Naming Conventions
-----------------------

Use lowercase, snake_case filenames. Climate data is named like:

- `tasmax_ssp585_2030_ACCESS-ESM1-5.nc`
- `precipitation_terraclimate_2020.nc`