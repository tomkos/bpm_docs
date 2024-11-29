# Display text

## Data binding

## Configuration properties

Under
Configuration, set or modify the appearance and behavior properties for the
view. Under Events, set the formula configuration properties.

<!-- image -->

The appearance configuration properties for the Display text view are shown in the following
table:

| Appearance configuration property   | Description                                                                                                                                                                   | Data type   |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Width                               | The width of the view. You can specify the width in px (pixels), % (percent), or em units. For example, 50px, 20%, or 0.4em. If a unit type is not specified, px is assumed.  | String      |
| Text alignment                      | The alignment of the display text in relation to the width of the view.                                                                                                       | String      |
| Color style                         | The color style for the view. This setting applies only to the text, not to the label. The colors correspond to variables in the specified theme.                             | String      |
| Size style                          | The text size. The size applies to both label and text.                                                                                                                       | String      |
| Text weight                         | The text weight. The weight applies only to the text, not to the label.                                                                                                       | String      |
| Label placement                     | The placement of the label in relation to the text. Labels on the left change the specified width of the view.                                                                | String      |
| Label width                         | The width of the label. You can specify the width in px (pixels), % (percent), or em units. For example, 50px, 20%, or 0.4em. If a unit type is not specified, px is assumed. | String      |

| Behavior configuration property   | Description                                                                                                        | Data type   |
|-----------------------------------|--------------------------------------------------------------------------------------------------------------------|-------------|
| Allow HTML                        | Displays the bound data as HTML formatted text.                                                                    | Boolean     |
| Wrap text                         | Control  how text is wrapped to a new line. The available options are: Default Normal Keep all Anywhere Break word | String      |

## Example

In this example, the display text is bound to a string that has the following value:
"Important information"

The following appearance configuration properties are set for the Display text view:

- Text alignment is set to Left.
- Color style is set to Primary.
- Size style is set to Larger.
- Text weight is set to Slim.
- Label placement is set to Top.

In the General properties tab, the name given to the
Label is Welcome.

These properties and their values result in a left-aligned text area that displays larger-sized
header labeled Welcome, above the message Important
information, in blue, slim and larger-sized font.

## Events

| Formula configuration property   | Description                                                                                                                                                                                                                             | Data type   |
|----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Text formula                     | The formula or expression that is used to calculate the display text.For example, you can specify the Display text value here using quotes, without needing to set a bound variable. For more information about formulas, see Formulas. | String      |

- On load: Activated when the page loads.

Depending
on the specific event, you can use JavaScript logic to modify the effects of the
view.

## Methods

For detailed information on the available methods for Display text, see the Display text JavaScript API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.