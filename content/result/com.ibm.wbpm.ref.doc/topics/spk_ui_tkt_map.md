# Map

You can define the appearance and behavior of maps by setting configuration properties.

## Configuration properties

Under Configuration,
set or modify the appearance and behavior properties for the view.

<!-- image -->

| Appearance configuration property   | Description                                                                                                                                            | Data type   |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Map type                            | The type of map.                                                                                                                                       | MapType     |
| Zoom level                          | The zoom level between 0, which shows the whole world, and 20, which shows details down to individual buildings when they exist.                       | Integer     |
| Width                               | The width of the map, in pixels (px), percentage of the original map (%), or em units, for example 50 px, 20%, or 4 em. The default unit is the pixel. | String      |
| Height                              | The height of the map, in pixels (px) or em units. For example 50 px or 4em. The default unit is the pixel.                                            | String      |

| Behavior configuration property   | Description                                                                                        | Data type   |
|-----------------------------------|----------------------------------------------------------------------------------------------------|-------------|
| Disable panning                   | Prevents users from panning the map, which results in fixing the map location.                     | Boolean     |
| Hide zoom control                 | Prevents users from zooming in and out.                                                            | Boolean     |
| Hide map type control             | Prevents users from changing the map type.                                                         | Boolean     |
| Hide scale control                | Prevents users from scaling the map.                                                               | Boolean     |
| Hide rotate control               | Prevents users from rotating the map.                                                              | Boolean     |
| Show marker                       | Shows or hides the marker. It requires the Latitude and Longitude configuration properties be set. | Boolean     |
| Latitude                          | Specifies the latitude on which to center the map.                                                 | Decimal     |
| Longitude                         | Specifies the longitude on which to center the map.                                                | Decimal     |
| Map source                        | Specifies the map provider: OpenStreetMap or Bing Maps.                                            | String      |

## Events

- On load when the page loads, for example
me.setWidth("100%")
- On click when the map is clicked, for example
${Map}.addMarker(latLng)
- On marker click when the marker is clicked, for example
console.log(marker.lng, marker.lat)

## Example

1. Drag the OpenLayers API view onto the page. For more information about this view, see OpenLayers API.
2. Drag the Map view onto the page.
3. In the Behavior configuration properties, specify the latitude and
longitude.
4 Set the map source to OpenStreetMap .Tip: You can find thelatitude and longitude of your location in one of the following ways:
    - Run a search on the Google website.
    - Use a specialized website, such as http://www.latlong.net/ .
    - Use the Geo Location view as explained in Geo location.
5. Set the Appearance properties. For example, select the
Roadmap type and set the zoom level to
16.OpenStreetMap provides only a roadmap view. Bing Maps also proposes
satellite and hybrid views.

<!-- image -->

## Methods

For more information about the available methods, see the Map JavaScript API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.