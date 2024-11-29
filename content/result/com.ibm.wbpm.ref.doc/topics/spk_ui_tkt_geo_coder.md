# Geo coder

Like the Geo location view, the Geo coder view adds another layer of information by allowing
users to see where they are on a map. You can use it to provide a point of reference. For more
efficiency, first place the OpenLayers API view at the top of the page or, at the very least, before
the Map view. For more information, see Map and OpenLayers API.

## Example

1. Use the OpenLayers API view to specify an API key.
2. Use the Geo Location view to find the user's location and display it on the Map.
3. Use the Geo coder view to display a physical address on a text view, such as Note, Output Text,
Text, or others.
4. Add the Map view to the page and adjust the appearance properties as appropriate.
5. Add a Custom HTML view to have the Map view communicate the coordinates to the
map.<script>
  function updateLocation(me, location) {
     var map = page.ui.get("Map1");    

     //Setting the center of the map and adding a marker
     map.setCenter(location.latitude, location.longitude);
     map.addMarker();

     //Get physical address of user

     var geoCoder = page.ui.get("Geo\_Coder1");
     geoCoder.requestAddressLookup(location.latitude, location.longitude);
  }
</script>

<!-- image -->

## Events

- On load when the page loads, for example
me.requestAddressLookup(${Geolocation}.getData().latitude,
${GeoLocation}.getData().longitude)
- On Address requested when the location is requested, for example
console.log("Address requested")
- On Address resolved when the location is resolved, for example
${Location}.setText(address.formatted);
- On Address error when an error occurs at location retrieval, for example
${LocationErrorText}.setVisible(true)

## Methods

For detailed information on the available methods for Geo coder, see the Geo coder JavaScript API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.

For information about associated geographical views, see Geo location, Map, and OpenLayers API.