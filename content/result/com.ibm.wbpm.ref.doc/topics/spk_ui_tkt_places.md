# Places

## Example

1. Use the OpenLayers API view to specify an API key. For more information, see OpenLayers API.
2. Use the Geo location view to find the user's location and display it on the map.
3. Use the Places view to display the places of interest of your choice and their location.
4. Use the Multi select view to select the place of interest you want to show, for example gas
stations.
5. Add the Map view to the page and configure the map appearance as appropriate.
6. Add a Custom HTML view to have the Map view communicate the coordinates and places to the
map.<script>
function updateLocation(me, location) {
   var map = page.ui.get("Map1");

   //Setting the center of the map and adding a marker
   map.setCenter(location.latitude, location.longitude);
   map.addMarker();

  //places

  var placesSearch = page.ui.get("Places1");

        placesSearch.requestNearbySearch(
            location.latitude,
            location.longitude,
            {
                radius: 10000,
                types: ["fuel"],
            }
            );    
    }
</script>

The result appends a list of gas stations after the map shown in Geo coder.

## Events

- On Load when the Places view is loaded on the page, for example
me.requestNearbySearch(${Geo}.getData().latitude, ${Geo}.getData().longitude, ["bank"],
true);
- On Place requested when a place is requested, for example
${Map}.addMarker(location)
- On Place resolved when a place is found, for example for(var i = 0;
i < places.length; i++){console.log("Place: " + places[i].name + " -- " +
places[i].vicinity);}
- On Place error when a place cannot resolve a location, for example
${Map}.setCenter(${Geo}.getData().latitude, ${Geo}.getData().longitude); console.log("Maps
cannot be reached at this time.")

## Methods

For detailed information on the available methods for Places, see the Places JavaScript API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.

For information about associated geographical views, see Geo coder,
Geo location, Map, and OpenLayers API.