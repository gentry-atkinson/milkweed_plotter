#Author: Gentry Atkinson
#Organization: St. Edwards University
#Date: 25 August, 2023
#Description: Read the Excel file and plot the point on a map.

import pandas as pd
import geopandas as gpd
import contextily as ctx
from matplotlib import pyplot as plt
from shapely.geometry import Point
#from pyproj import Proj, transform

if __name__ == "__main__":

    xls = pd.ExcelFile(r"Milkweed coordinates.xlsx")
    sheet = xls.parse(0)
    coords = [(sheet['Latitude'][i], sheet['Longitude'][i]) for i in range(len(sheet))]
    #coords_wm = [transform(Proj(init='epsg:3857'), Proj(init='epsg:4826'), i[0], i[1]) for i in coords]
    #print(coords_wm)


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

    print(geo_df)

    ax = geo_df.plot(c='red', figsize=(10, 10))
    ax.axis((-99, -97.5, 29.5, 31))
    crs = {'init': 'epsg:4326'}
    ctx.add_basemap(
        ax,
        source=ctx.providers.CartoDB.Voyager,
        crs=crs,
        zoom=10
    )


    plt.title("Map with Plotted Points")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.show()
