# Configuration

## Configuration properties

The appearance configuration
properties for Configuration are shown in the following table:

| Configuration property                       | Description                                                                                                            | Data type       |
|----------------------------------------------|------------------------------------------------------------------------------------------------------------------------|-----------------|
| Debugging on                                 | Specifies whether the debug switch is enabled. The debug switch enables views to log debug information in the console. | Boolean         |
| Logging > Show log                           | Facilitates testing on mobile devices, where the browser log is not easy to retrieve in real-time.                     | Boolean         |
| Logging > Last entry first                   | Inserts new entries at the top of the log window rather than at the end.                                               | Boolean         |
| Internationalization > Global text direction | Specifies the direction of the text on the page. Auto (based on user settings) Left-to-Right Right-to-Left             | String          |
| Internationalization > Locale                | Specifies the locale for the view.                                                                                     | String          |
| Internationalization > I18N service          | Specifies the I18N Ajax service that supplies internationalization to the UI views.                                    | AJAX Service    |
| Parameters                                   | Provides the list of parameters that can be accessed by the getParameter() method.                                     | NameValuePair[] |

## Methods

For detailed information on the available methods for Configuration, see the Configuration JavaScript
API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.