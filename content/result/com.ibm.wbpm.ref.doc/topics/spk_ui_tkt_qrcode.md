# QR code

Typically, QR scanners are available for download on camera-enabled smart phones for free. After
you line up the scanner to the QR code, you are automatically taken to a specific web site that was
configured on the QR code view.

## Data binding

## Configuration properties

Under
Configuration, set or modify the appearance and behavior properties for the
view. Under Events, set the formula configuration properties.

<!-- image -->

The appearance configuration properties for the QR code view are shown in the following
table:

| Appearance configuration property   | Description                                                                                                                                                                   | Data type   |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Label placement                     | Specifies the label placement for the view: Top Left  Note: Labels on the left change the specified width of the view.                                                        | String      |
| Label width                         | The width of the label. You can specify the width in px (pixels), % (percent), or em units. For example, 50px, 20%, or 0.4em. If a unit type is not specified, px is assumed. | String      |
| Width                               | Specifies the width of the view in pixels, percent, or em units. For example: 50px or 20% or 0.4em. If no unit type is specified, px is assumed.                              | String      |
| Height                              | Specifies the height of the view in px (pixels) or em units. If no unit type is specified, px is assumed.                                                                     | String      |
| Background image URL                | Specifies the background image for the QR view.                                                                                                                               | String      |

| Behavior configuration property   | Description                                                                                                                                                                                                                                                                                                                                                                         | Data type   |
|-----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Error correction level            | Specifies the error correction levels that are used for QR codes. Each error code adds a different amount of backup data depending on how much damage the QR code is expected to suffer in its intended environment, hence how much error correction might be required. Level L - up to 7% damage Level M - up to 15% damage Level Q - up to 25% damage  Level H - up to 30% damage | String      |

## Events

| Formula configuration property   | Description                                                                                                                     | Data type   |
|----------------------------------|---------------------------------------------------------------------------------------------------------------------------------|-------------|
| QR code formula                  | Specifies the formula or expression to use for calculating the QR code value.For more information about formulas, see Formulas. | String      |

- On load: Activated when the QR code is loaded. For example:
me.setQRCode("www.ibm.com")
- On change: Activated when the QR code value is changed. For example:
${Text1}.setText(oldQRCode); ${Text2}.setText(newQRCode);

## Methods

For detailed information on the available methods for QR code, see the QR code JavaScript API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.