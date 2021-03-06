import pandas as pd
import folium
from folium import TileLayer, Map, Circle
from folium.plugins import HeatMap, HeatMapWithTime


MID_ATLANTIC = (34.875083, -41.793607)


class FoliumMap:
    
    def __init__(self):
        pass
    
    def build_map(self, 
         location=None, 
         zoom_start=6,
         max_zoom=15, 
         **kwargs):
        
        if location is None:
            location = MID_ATLANTIC
        
        self.map = Map(location=location,
                       zoom_start=zoom_start,
                       **kwargs)

    def add_bubbles(self, xycoords, 
                    popups=None, 
                    tooltips=None,
                    radius=1,  
                    color='crimson', 
                    fill_color='crimson',
                    fill=True,
                    **kwargs):
        
        if popups is None:
            popups = [None] * len(xycoords)

        if tooltips is None:
            tooltips = [None] * len(xycoords)

        if type(radius) == int:
            radius = [radius] * len(xycoords)
        
        if type(color) == str:
            color = [color] * len(xycoords)

        if type(fill_color) == str:
            fill_color = [fill_color] * len(xycoords)

        for i, gps in enumerate(xycoords):
            circle = Circle(
                location=gps, 
                popup=popups[i], 
                tooltip=tooltips[i],
                radius=radius[i],
                color=color[i], 
                fill=fill, 
                fill_color=fill_color[i], **kwargs)
            circle.add_to(self.map)

    def add_heatmap(self, xycoords, name=None,
                    radius=5, 
                    blur=7, 
                    overlay=True, 
                    control=True, 
                    **kwargs):

        # Generate heat map
        heatmap = HeatMap(xycoords,
                          name=name,
                          radius=radius,
                          blur=blur,
                          overlay=overlay,
                          control=control,
                          **kwargs)
        
        heatmap.add_to(self.map)

