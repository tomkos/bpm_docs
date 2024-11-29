# Modal alert

## Configuration properties

Under Configuration,
set or modify the appearance and behavior properties for the view.

<!-- image -->

| Appearance configuration property   | Description                                                                                                                                       | Data type   |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Color style                         | Specifies the color and icon for the modal alert. The colors correspond to variables in the specified theme.                                      | String      |
| Button label                        | The label of the button inside the modal alert. The default label is OK.                                                                          | String      |
| Help                                | The text that is displayed in the alert. You can use basic html tags, for example, <b></b>. Note: This property is in the General properties tab. |             |

## Example

1. Open the client-side human service that you are working with.
2. In the Starting page of your UI, drag a Modal alert
view and a Button view onto the editor.
3 Select the Modal alert view on the canvas, and clickProperties to set the properties of the view:

<!-- image -->

    - Under Configuration > Appearance, set Color style to Warning, and
specify Close for the Button label.
    - Under General, enter the following text in the
Help field:
This text appears inside the <b>Modal alert</b>
    - Under Visibility, set the visibility to Hidden.
4 Select the Button view, and click Properties ) to set the properties of the view:

<!-- image -->

- Under General, specify Alert as the button label.
- Under Configuration > Appearance, set Color style to Warning and the
width to 100%.
- Under Events, configure the on click  event so
that the modal alert is loaded when the button is clicked. Enter the following code in the
on click event:${Modal\_Alert1}.setVisible(true); Tip:
Modal\_Alert1 is the control ID of the modal alert view that you created. To
get the control ID, go to the Configuration > General page.
5. At run time, a browser opens showing the Alert button:
6. Click the Alert button. The modal alert appears:
7. Click Close. The modal alert closes.

## Events

- On load. Activated when the page loads. For example:
me.setVisible(true)
- On close Activated when the Modal alert button is clicked. For example:
${Text}.setText("Modal alert is closed")
- On show. Activated when the Modal alert is opened,
for example me.setText("Modal alert is open...");

## Methods

For more information about the available methods, see the Modal alert JavaScript API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.