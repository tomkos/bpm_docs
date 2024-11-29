# Radio Buttons (deprecated)

| Process Designer desktop editor   | Process Designer web editor   |
|-----------------------------------|-------------------------------|
|                                   |                               |

## Restrictions and limitations

None

## Data binding

| Binding description                                                | Data type   |
|--------------------------------------------------------------------|-------------|
| Sets the initial selection and then contains subsequent selections | ANY (List)  |

## Configuration properties

<!-- image -->

| Configuration property       | Description                                                                                                                                                                                                                                                                                                                                                                                                          | Data type                                              |
|------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| Selection Service            | Identifies the service that is called using Ajax to dynamically return a list of options to display as radio buttons. You can use the selection service input text option to identify the specific list that the service returns.The default value is Default Selection Service, which serves as a template for the selection service implementation that you must provide.                                          | Service Input: text(String) Output: results(ANY)(List) |
| Selection List               | Identifies the list that contains options to show as radio buttons.                                                                                                                                                                                                                                                                                                                                                  | SelectionType                                          |
| Selection Service Input Text | Provides the text to send to the selection service as input. For example, if the selection service contains named lists, enter the name of the list that you want.                                                                                                                                                                                                                                                   | String                                                 |
| Display Name Property        | For data objects in selection lists that are not String or NameValuePair types, specify which property to use as their display names. The default value is name. For example, if you have a business object with parameters called field1 and field2, and you want to use field2 as the display name, enter field2 or set this property to a variable that contains "field2" as a string. The default value is name. | String                                                 |
| Disable Sorting              | Specifies whether to display the radio buttons sorted alphabetically by label or by the order in which they appear in the list.The default value is not selected (False).                                                                                                                                                                                                                                            | Boolean                                                |
| Layout                       | Specifies whether the radio buttons stack vertically or align horizontally.The default value is Vertical.                                                                                                                                                                                                                                                                                                            | RadioButtonsOrientation                                |