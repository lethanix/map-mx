""" mxgeojson.py """

import pandas as pd
import geopandas as gpd
import streamlit as st
from pyproj import CRS

crs_4326 = CRS("EPSG:4326")

#*###############################################
@st.cache
def listGeometries(layer="estados",
                  url="https://louiscmm.github.io/MX-GeoJSON/Mexico_estados&municipios.json"):

    if layer == "municipios":
        mx_ls = gpd.read_file(url, layer="municipalities")
        return mx_ls.mun_name

    elif layer == "estados":
        mx_ls = gpd.read_file(url, layer="states")
        return mx_ls.state_name

    else:
        print("Invalid argument layer ", layer)
        return -1


#*###############################################
@st.cache
def getGeometry(location,
                layer="estados",
                url="https://louiscmm.github.io/MX-GeoJSON/Mexico_estados&municipios.json"):

    if layer == "municipios":
        mx_gdf = gpd.read_file(url, layer="municipalities")
        mx_gdf = mx_gdf[mx_gdf.mun_name == location]

    elif layer == "estados":
        mx_gdf = gpd.read_file(url, layer="states")
        mx_gdf = mx_gdf[mx_gdf.state_name == location]

    else:
        print("Invalid argument layer ", layer)
        return -1

    mx_gdf     = mx_gdf['geometry']
    mx_gdf.crs = crs_4326

    return mx_gdf


#*###############################################
@st.cache
def getInsideFrom(here, of_this):
    within = pd.DataFrame(
        {"WithinLocation": here.contains(of_this.geometry[i]).array[0]}
        for i in range(0, len(of_this) - 1)
    )

    within = within[within.WithinLocation == True]
    inside_df = of_this.iloc[within.index.array]

    return inside_df
