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
ProjCarVan = ProjLSOAs.join(Car_van.set_index('geography code'), on='LSOA21CD', how='left',
                      validate='one_to_one')
BuffCarVan = BuffLSOAs.join(Car_van.set_index('geography code'), on='LSOA21CD', how='left',
                      validate='one_to_one')

# ALL DATA CAR AND VAN PERCENTAGES
TotalAll = Car_van['Number of cars or vans: Total: All households'].sum()
TotalNoCarVan = Car_van['Number of cars or vans: No cars or vans in household'].sum()
Total1CarVan = Car_van['Number of cars or vans: 1 car or van in household'].sum()
Total2CarVan = Car_van['Number of cars or vans: 2 cars or vans in household'].sum()
Total3CarVan = Car_van['Number of cars or vans: 3 or more cars or vans in household'].sum()

PerTotalNoCarVan = (TotalNoCarVan/TotalAll)*100
PerTotal1CarVan = (Total1CarVan/TotalAll)*100
PerTotal2CarVan = (Total2CarVan/TotalAll)*100
PerTotal3CarVan = (Total3CarVan/TotalAll)*100

# PROJECT AREA CAR AND VAN PERCENTAGES
ProjAll = ProjCarVan['Number of cars or vans: Total: All households'].sum()
ProjNoCarVan = ProjCarVan['Number of cars or vans: No cars or vans in household'].sum()
Proj1CarVan = ProjCarVan['Number of cars or vans: 1 car or van in household'].sum()
Proj2CarVan = ProjCarVan['Number of cars or vans: 2 cars or vans in household'].sum()
Proj3CarVan = ProjCarVan['Number of cars or vans: 3 or more cars or vans in household'].sum()

PerProjNoCarVan = (ProjNoCarVan/ProjAll)*100
PerProj1CarVan = (Proj1CarVan/ProjAll)*100
PerProj2CarVan = (Proj2CarVan/ProjAll)*100
PerProj3CarVan = (Proj3CarVan/ProjAll)*100

RatioProjNoCar = PerProjNoCarVan/PerTotalNoCarVan
RatioProj1Car = PerProj1CarVan/PerTotal1CarVan
RatioProj2Car = PerProj2CarVan/PerTotal2CarVan
RatioProj3Car = PerProj3CarVan/PerTotal3CarVan

# BUFFER AREA CAR AND VAN PERCENTAGES
BuffAll = BuffCarVan['Number of cars or vans: Total: All households'].sum()
BuffNoCarVan = BuffCarVan['Number of cars or vans: No cars or vans in household'].sum()
Buff1CarVan = BuffCarVan['Number of cars or vans: 1 car or van in household'].sum()
Buff2CarVan = BuffCarVan['Number of cars or vans: 2 cars or vans in household'].sum()
Buff3CarVan = BuffCarVan['Number of cars or vans: 3 or more cars or vans in household'].sum()

PerBuffNoCarVan = (BuffNoCarVan/ProjAll)*100
PerBuff1CarVan = (Buff1CarVan/ProjAll)*100
PerBuff2CarVan = (Buff2CarVan/ProjAll)*100
PerBuff3CarVan = (Buff3CarVan/ProjAll)*100

results = open(r'C:/Users/charl/Documents/Essex Wildlife Trust/Population analysis private/results.txt', "w")
results.write('Percentage of cars without a car or van in the project area: {:.2f}%, {:.2f} times the national '
              'percentage. \n'.format(PerProjNoCarVan, RatioProjNoCar))
results.write('Percentage of cars with one car or van in the project area: {:.2f}%, {:.2f} times the national '
              'percentage. \n'.format(PerProj1CarVan, RatioProj1Car))
results.write('Percentage of cars with two cars or vans in the project area: {:.2f}%, {:.2f} times the national '
              'percentage. \n'.format(PerProj2CarVan, RatioProj2Car))
results.write('Percentage of cars with three or more cars or vans in the project area: {:.2f}%, {:.2f} times the '
              'national percentage. \n'.format(PerProj3CarVan, RatioProj3Car))
results.close()

ProjCarVan.to_csv(r'C:/Users/charl/Documents/Essex Wildlife Trust/Population analysis private/ProjCarVan.csv')
