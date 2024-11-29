# Image

## Data binding

You can use the binding to specify the image. If no binding is specified, the
Default image URL configuration property is used. To set a different image
for different screen sizes, you must use theDefault image URL configuration
property.

## Configuration properties

Under Configuration,
set or modify the appearance and behavior properties for the view.

<!-- image -->

| Appearance configuration property   | Description                                                                                                                                                                                                                               | Data type   |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Border radius                       | Specifies the radius of the curvature for an image. You can make an image perfectly round by setting it to at least half of the width specified for the Width property. By default, no border radius is specified.                        | String      |
| Width                               | Specifies the width of an image in pixels, percent, or em units. For example: 50px or 20% or 0.4em. If only a number is specified without any unit, the number is interpreted as the number of pixels. By default, no width is specified. | String      |
| Height                              | Specifies the height of an image in pixels or em units. For example: 50px or 0.4em. If only a number is specified without any unit, the number is interpreted as the number of pixels. By default, no height is specified.                |             |

| Behavior configuration property   | Description                                                                                                                                                                                                              | Data type   |
|-----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Prevent multiple clicks           | Prevents a user from clicking an image more than once when the on click event is programmed. By default, this property is not selected.                                                                                  | Boolean     |
| Image URL type                    | The type of the image URL.  Web External  Note: Use External for images that are not hosted on the local server.                                                                                                         |             |
| Image app acronym                 | The acronym of the process app or toolkit that contains the image. By default, the acronym of the current process app is used.                                                                                           |             |
| Default image URL                 | If the view is not bound, this URL is used. To set a different image for different screen sizes, you must use this property. To use an image, you must upload it to the designer. See Adding managed files               |             |
| Default image URL type            | If the view is not bound, this URL type is used.  Web External  Note: Use External for images that are not hosted on the local server.                                                                                   |             |
| Default image app acronym         | The default acronym of the process app or toolkit that contains the image. By default, the acronym of the current process app is used. If the view is not bound to any data, the acronym that is specified here is used. |             |

## Example

Upload the image that you want to use to the designer. See Adding managed files.

In this example, the Image view is inside a Vertical Layout view, which is inside a Well view.
The example uses the following configuration options:

- Image URL type is Web.
- Default image URL is magnolia.gif.
- Default image URL type is Web.
- Label position is Bottom.
- Border radius is 50px.
- Width is 300px.

At run time, you see the following:

## Events

- On load: Activated when the page loads. For
example:console.log("Img1 successfully loaded")
- On click: Activated when an image is clicked, before navigating away from
the page. If the evaluated expression returns false, the click does not fire a boundary event. For
example:return ${Text1}.isValid();

## Methods

For detailed information on the available methods for Image, see the Image JavaScript API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.