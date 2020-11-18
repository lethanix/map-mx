import folium
import pandas as pd
import streamlit as st
import geopandas as gpd
import mxgeojson as mxg

from streamlit_folium import folium_static


#*###############################################
#*--> Select the location you want.
visual = st.radio(
    "¿Qué nivel deseas visualizar?",
    ('Estado', 'Municipio') )

if visual == 'Estado':

    location = st.selectbox(
        "¿Qué estado deseas seleccionar?",
        mxg.listGeometries()
    )

    # Get the POLYGON of the location.
    this_place = mxg.getGeometry(location)

elif visual == 'Municipio':

    location = st.selectbox(
        "¿Qué estado deseas seleccionar?",
        mxg.listGeometries("municipios")
    )

    # Get the POLYGON of the location.
    this_place = mxg.getGeometry(location, "municipios")

#*###############################################
#*--> Create map.
with st.spinner("Generando mapa..."):
    mx_lat, mx_lon = 23, -102
    m = folium.Map(location=[mx_lat, mx_lon], zoom_start=5)

    # Color the location.
    folium.Choropleth(
        geo_data     = this_place,
        fill_color   = 'purple',
        fill_opacity = 0.2,
        line_color   = 'purple',
        line_opacity = 0.2
    ).add_to(m)

    folium.LayerControl().add_to(m)

    ## Display stations.
    #for i, xrow in stations_in_location.iterrows():
    #    # generate the popup message that is shown on click.
    #    tt_txt = f"<b>Estacion: </b> {xrow.nombre}"
    #    pu_txt = f"<b>Estacion: </b> {xrow.nombre} <br><b>Código: </b> {xrow.codigo} <br><b>ID: </b> {xrow.id} <br><b>RedesID: </b> {xrow.redesid}"
#
    #    folium.Marker(
    #        location=(xrow.lat, xrow.lon),
    #        tooltip=tt_txt,
    #        popup=folium.map.Popup(pu_txt, max_width=150),
    #        icon=folium.Icon(color="purple", icon="cloud")
    #    ).add_to(m)

    folium_static(m)



