#Author: Gentry Atkinson
#Organization: St. Edwards University
#Date: 25 August, 2023
#Description: Read the coordinate Excel file and plot the points on a map.

# Maps provided by CartoDB
# (C) OpenStreetMap contributors (C) CARTO

import pandas as pd
import geopandas as gpd
import contextily as ctx
import xyzservices as xyz
from matplotlib import pyplot as plt
from shapely.geometry import Point

if __name__ == "__main__":

    xls = pd.ExcelFile(r"Milkweed coordinates.xlsx")
    sheet = xls.parse(0)
    coords = [(sheet['Latitude'][i], sheet['Longitude'][i]) for i in range(len(sheet))]

    locations = {
        'name': [],
        'Latitude': [],
        'Longitude': []
    }

    for ll in coords: 
        locations['name'].append(f'{ll[0]:.2f}, {ll[1]:.2f}')
        locations['Latitude'].append(ll[0])
        locations['Longitude'].append(ll[1])

    points = [Point(p[1], p[0]) for p in coords]
    geo_df = gpd.GeoDataFrame(locations, geometry=points)

    ax = geo_df.plot(c='red', figsize=(10, 10))
    ax.axis((-97.760, -97.750, 30.225, 30.235))
    crs = {'init': 'epsg:4326'}
    ctx.add_basemap(
        ax,
        #source=ctx.providers.CartoDB.Voyager,
        source=ctx.providers.OpenTopoMap,
        crs=crs,
    )


    plt.title("Map with Plotted Points")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    #plt.show()
    plt.savefig('st_edwards_milkweed_map.png')
