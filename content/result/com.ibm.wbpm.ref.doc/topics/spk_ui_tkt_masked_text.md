# Masked text

You can bind this view to a String variable. You can also define behavior and
appearance configuration properties.

## Configuration properties

Under Configuration,
set or modify the appearance and behavior properties for the view.

<!-- image -->

| Appearance configuration property   | Description                                                                                                                                                                   | Data type   |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Monospace                           | Prevents the mask from moving as the text is entered.                                                                                                                         | Boolean     |
| Width                               | The width of the view. You can specify the width in px (pixels), % (percent), or em units. For example, 50px, 20%, or 0.4em. If a unit type is not specified, px is assumed.  | String      |
| Size style                          | Specifies the size of the masked text.                                                                                                                                        | String      |
| Label placement                     | Specifies the label placement relative to the contained text: Top or Left.The default label placement is Top.                                                                 | String      |
| Label width                         | The width of the label. You can specify the width in px (pixels), % (percent), or em units. For example, 50px, 20%, or 0.4em. If a unit type is not specified, px is assumed. | String      |

| Behavior configuration property   | Description                                                                                                                                                                                                                                             | Data type   |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Tab index                         | Defines the index of the tabulation sequence through fields. Tab indexes start at 1. You can add them sparsely, for example 1, 5, 10.                                                                                                                   | Integer     |
| Placeholder text                  | Provides the placeholder text that is displayed when no value was entered. In most cases, this placeholder text is the same as the mask text.                                                                                                           | String      |
| Mask                              | To indicate what type of characters can be entered, use the # sign for numeric characters and the a letter for alphabetical characters.Tip: The question mark (?) is a reserved character, and the characters that follow a question mark are optional. | String      |
| Auto clear invalid text           | Select this option to have invalid text removed automatically.                                                                                                                                                                                          | Boolean     |

## Example of a numeric Masked text view

1. In the Appearance part of the Configuration window,
set Width to 200 px, Size style
to Large, and Label placement to
Top.
2. In the Behavior part, set the Placeholder text to
a fake phone number that complies with the dialing conventions of your location, for example
(555) 555 - 5555 and in the Mask field, enter a string
of # characters on the same pattern, for example (###) ### - ####.Leave
the other options blank.

## Example of an alphabetical Masked text view

1. In the Appearance part of the Configuration window,
set Width to 200 px, Size style
to Large, and Label placement to
Top.
2. In the Behavior part, set the Placeholder text to
State and in the Mask field, enter
aa.Leave the other options blank.

## Events

- On load  when the page loads, for example
me.setMask(${CountryCodeData}.getValue() == "uk" ? "(###) ####-####" : (###)
###-####)
- On change  when the data in the view is modified, for example
me.setValid(@validNumber(newText),"Please enter a valid phone number")
- On focus  when the view gets focus, for example
me.setSizeStyle("L")
- On blur  when the user clicks or tabs away from the view, for example
me.setSizeStyle("D")
- On input  when the user enters data in the view, for example return
potential.substr(0,3) != "555"

## Methods

For more information about the available methods, see the Masked text JavaScript API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.