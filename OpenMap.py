import folium

australianCities = {
    'Canberra': [-35.293056, 149.126944],
    'Sydney': [-33.865, 151.209444]
}

mapData = folium.Map(
    location = australianCities['Canberra'],
    title = 'Open Map'
)

mapLayers = [
    {
        'name': 'Fire',
        'points': [
            folium.Marker(
                location = [-35.30818, 149.12445],
                popup = 'Fire',
                icon = folium.Icon(
                    icon = 'fire',
                    color = 'red')
            )
        ],
        'areas': [
            folium.Circle(
                radius = 1000,
                location = [-35.30818, 149.12445],
                popup = 'Fire',
                color = 'crimson',
                fill = True,
                fill_color = 'crimson'
            )
        ]
    },
    {
        'name': 'Traffic',
        'points': [
            folium.Marker(
                location = [-35.29276, 149.12694],
                popup = 'Bridge Closed',
                icon = folium.Icon(
                    icon = 'warning-sign',
                    color = 'red')
            ),
            folium.Marker(
                location = [-35.30170, 149.14110],
                popup = 'Bridge Closed',
                icon = folium.Icon(
                    icon = 'warning-sign',
                    color = 'red')
            )
        ],
        'areas': []
    }
]

for mapLayer in mapLayers:
    featureGroup = folium.map.FeatureGroup(
        name = mapLayer['name'],
        overlay = True,
        control = True,
        show = True
    ),
    for point in mapLayer['points']:
        
    for area in mapLayer['area']:
        point.add_to(featureGroup)
    featureGroup.add_to(mapData)

folium.LayerControl().add_to(mapData)

mapData.save('index.html')
