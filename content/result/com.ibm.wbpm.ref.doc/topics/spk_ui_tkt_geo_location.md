# Geo location

You can use this view in association with the Map and OpenLayers API views. However, the
OpenLayers API might not be necessary, depending on the device. The content of the location object
and the precision of these metrics depend on the device on which the user interface is running.
Whichever the device, a latitude and longitude must be available through this object. Location is a
context variable, which is available within the On Location Resolved event of
this view.

For this view to work, it must be connected to some sort of data network, such as a mobile, wifi,
Ethernet, or similar network. If no connection exists, the view does not work. As a browser built-in
security function, the page requests permission to access the user's location information.

Like the Geo coder view, the Geo location view adds another layer of information by allowing
users to see where they are on a map. You can use it to provide a point of reference. For more
efficiency, first place the OpenLayers API view at the top of the page or, at the very least, before
the Map view. For more information, see Map and OpenLayers API.

## Configuration properties

| Configuration property   | Description                                                                                                                                  | Data type         |
|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| Monitoring mode          | Monitoring modes for the view: Once on Load, Continuous, Initially Stopped.                                                                  | GeoMonitoringMode |
| High accuracy            | If you select this option, location detection is more accurate but uses more battery power.                                                  | Boolean           |
| Timeout                  | You can enter the number of milliseconds after which the device stops trying to detect the specified location. The default value is 6000 ms. | Integer           |
| Max age of data          | You can enter, in milliseconds, the oldest geo location data that you accept. The default value is 0 ms.                                     | Integer           |

## Example

1. Use the OpenLayers API view to specify an API key.
2. Use the Geo location view to find the user's location and display it on the Map.
3. Use the Geo coder view to display a physical address on a text view, such as Note, Output Text,
Text, or others.
4. Add the Map view to the page and adjust the appearance properties as appropriate.
5. Add a Custom HTML view to have the Map view communicate the coordinates to the
map.<script>
  function updateLocation(me, location){
     var map = page.ui.get("Map1");

     //Setting the center of the map and adding a marker
     map.setCenter(location.latitude, location.longitude);
     map.addMarker();

     // <optional> Printing the Coordinates to the Coordinates field 
     var coordinates= page.ui.get("Coordinates");
     coordinates.setText("Latitude: " + location.latitude +" "+"Longitude: "+

     location.longitude );
  }
</script>

<!-- image -->

## Methods

For detailed information on the available methods for Geo location, see the Geo location JavaScript API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.

For information about associated geographical views, see Geo location, Map, and OpenLayers API.