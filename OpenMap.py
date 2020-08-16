# GovHack 2020
# Team DISER
# Open Map: An aggregation of low-quality geo-spatial data points

import folium
import requests

# Generate Map
australianCities = {
    'Canberra': [-35.293056, 149.126944],
    'Sydney': [-33.865, 151.209444]
}

mapData = folium.Map(
    location = australianCities['Canberra'],
    title = 'Open Map'
)

# Add sample fire Data
fireData = folium.FeatureGroup(
    name='Fire'
)
fireData.add_child(
    folium.Marker(
        location = [-35.30818, 149.12445],
        popup = 'Fire',
        icon = folium.Icon(
            icon = 'fire',
            color = 'red'
        )
    )
)
fireData.add_child(
    folium.Circle(
        radius = 1000,
        location = [-35.30818, 149.12445],
        popup = 'Fire',
        color = 'crimson',
        fill = True,
        fill_color = 'crimson'
    )
)
mapData.add_child(fireData)

# Add ACT traffic data
trafficData = folium.FeatureGroup(
    name='Trafic'
)
response = requests.get('https://services1.arcgis.com/E5n4f1VY84i0xSjy/arcgis/rest/services/Public_Temporary_Road_Closures/FeatureServer/0/query?&where=objectid%3E0&outFields=*&f=json')
if response.status_code != 200:
    print('Error getting ACT Road Closure Data')
    exit()
for item in response.json()['features']:
    description = str(item['attributes']['roadsClosed']).strip()
    geometryX = item['geometry']['x']
    geometryY = item['geometry']['y']

    trafficData.add_child(
        folium.Marker(
            location = [geometryY, geometryX],
            popup = folium.Popup(
                html = description,
                min_width = 200,
                max_width = 400
            ),
            icon = folium.Icon(
                icon = 'warning-sign',
                color = 'orange'
            )
        )
    )
mapData.add_child(trafficData)

folium.LayerControl().add_to(mapData)
mapData.save('MapElement.html')
