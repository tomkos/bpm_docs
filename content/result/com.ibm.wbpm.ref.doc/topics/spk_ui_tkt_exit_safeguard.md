# Exit Safeguard (deprecated)

A challenge is presented to users when they attempt to close the browser window or navigate away
from the page. This is an added security measure that warns users that closing the browser window
does not close or finish the task, which might result in unexpected behavior.

To suppress the challenge, you can use the setExitChallenged(false) in the
navigation event, such as On Click for buttons.

## Configuration properties

Under Configuration, set or modify the configuration
properties for the view.

The configuration properties for the Exit Safeguard view are shown in the following table:

| Configuration property       | Description                                                                                                                                                     | Data type   |
|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Challenge on exit by default | When this option is selected, a challenge is presented to the user if they attempt to close the browser window or navigate away from the page.                  | Boolean     |
| Exit challenge message       | Provides the additional message that is displayed for the exit challenge. All the browsers can display a challenge, but not all can add the additional message. | String      |

## Methods

For detailed information on the available methods for Exit Safeguard, see the Exit Safeguard JavaScript
API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.