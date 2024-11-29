# Modal section

## Configuration properties

Under Configuration,
set or modify the appearance and behavior properties for the view.

<!-- image -->

| Appearance configuration property   | Description                                                                                                            | Data type        |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------|------------------|
| Modal placeholder width             | Specifies the width of the view in pixels (px), percentage of the original width (%), or em units.                     | String           |
| Show buttons                        | Shows the buttons in the modal.                                                                                        | Boolean          |
| Color style                         | The color style of the primary button. The available options are Default, Primary, Info, Success, Warning, and Danger. | ButtonColorStyle |
| Text on primary button              | The text on the button that allows the user to confirm the action in the modal. For example, Save or OK.               | String           |
| Text on secondary button            | The text on the button that allows the user to dismiss the action in the modal. For example, Close or Cancel.          | String           |

| Behavior configuration property   | Description                                                                                                                                            | Data type   |
|-----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Close on click                    | If you select Close on click, users can close the modal section by clicking anywhere outside of it. By default, the modal section cannot be dismissed. | Boolean     |

## Events

- On load: Activated when the page loads, for example
me.setVisible(true);
- On close: Activated when the Modal section window is closed, for example
${Output\_Text1}.setText("Modal section closed...");, where
Output\_Text1 is the control ID of the output text.
- On show: Activated when the Modal section window is opened, for example
me.setText("Modal section is open...");
- On primary button clicked: Activated when the modal's primary button is
clicked. For example: btn text: Save
onclick: customized save function/actions
- On secondary button clicked: Activated when the modal's secondary button is
clicked. For example:btn text: Close
onclick action: me.hide();

## Methods

For more information about the available methods, see the Modal section JavaScript API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.