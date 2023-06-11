# POPULATION ANALYSIS PYTHON SCRIPT - ANALYSIS OF CENSUS AND IMD DATA FOR A DEFINED AREA

# IMPORTS
import geopandas as gpd
import pandas as pd

# READ FILES
ProjectArea = gpd.read_file(r'C:/Users/charl/Documents/Essex Wildlife Trust/Population_analysis/Population_analysis/files/Analysis_area.shp')
ProjectBuffer = gpd.read_file(r'C:/Users/charl/Documents/Essex Wildlife Trust/Population_analysis/Population_analysis/files/11_miles_buffer.shp')
Car_van = pd.read_csv(
    r'C:/Users/charl/Documents/Essex Wildlife Trust/Population analysis private/census2021-ts045-lsoa.csv')
LSOAs = gpd.read_file(r'C:/Users/charl/Documents/Essex Wildlife Trust/Population analysis private/LSOA_2021_EW_BGC.shp')

# CLIP LSOAs TO PROJECT AREA AND BUFFER AREA
ProjLSOAs = gpd.clip(LSOAs, ProjectArea)
BuffLSOAs = gpd.clip(LSOAs, ProjectBuffer)

ProjLSOAs.to_file(r'C:/Users/charl/Documents/Essex Wildlife Trust/Population analysis private/ProjLSOAs.shp')
BuffLSOAs.to_file(r'C:/Users/charl/Documents/Essex Wildlife Trust/Population analysis private/BuffLSOAs.shp')

# FILTER DATA TO APPROPRIATE AREA(S)
ProjCarVan = pd.merge(Car_van, ProjLSOAs, how='left', left_on=['geography code'], right_on=['LSOA21CD'])
BuffCarVan = pd.merge(Car_van, BuffLSOAs, how='left', left_on=['geography code'], right_on=['LSOA21CD'])

