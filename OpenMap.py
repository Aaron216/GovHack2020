import folium

australianCities = {
    'Canberra': [-35.293056, 149.126944],
    'Sydney': [-33.865, 151.209444]
}

mapData = folium.Map(
    location = australianCities['Canberra'],
    title = 'Open Map'
)

fireData = folium.FeatureGroup(
    name='Fire'
)
fireData.add_child(
    folium.Marker(
        location = [-35.30818, 149.12445],
        popup = 'Fire',
        icon = folium.Icon(
            icon = 'fire',
            color = 'red')
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

trafficData = folium.FeatureGroup(
    name='Trafic'
)
trafficData.add_child(
    folium.Marker(
        location = [-35.29276, 149.12694],
        popup = 'Bridge Closed',
        icon = folium.Icon(
            icon = 'warning-sign',
            color = 'orange')
    )
)
trafficData.add_child(
    folium.Marker(
        location = [-35.30170, 149.14110],
        popup = 'Bridge Closed',
        icon = folium.Icon(
            icon = 'warning-sign',
            color = 'orange')
    )
)

mapData.add_child(fireData)
mapData.add_child(trafficData)

folium.LayerControl().add_to(mapData)

mapData.save('index.html')
