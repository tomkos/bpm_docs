# Text (deprecated)

| Process Designer desktop editor   | Process Designer web editor                                                        |
|-----------------------------------|------------------------------------------------------------------------------------|
|                                   | Remember: This control stretches horizontally to occupy the space available to it. |

## Restrictions and limitations

None

## Data binding

| Binding description                                                                                                                     | Data type   |
|-----------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Contains the text that this control displays. The String can be empty and the Text control saves the text that the user enters into it. | String      |

## Configuration properties

| Configuration property   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Data type                                                 |
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| Enable Autocompletion    | Sets whether the field displays suggestions based on what the user types. You must specify an autocompletion service if you enable autocompletion.The default value is not selected (False).                                                                                                                                                                                                                                                                  | Boolean                                                   |
| Autocompletion Service   | Specifiy the service that provides type-ahead content assistance. Business Automation Workflow provides the default autocompletion service to show the API for this service. You must provide your own service implementation.                                                                                                                                                                                                                                | Service Input: text(String) Output: results(String)(List) |
| Autocompletion Delay     | Sets the number of milliseconds to wait following the last keystroke before sending the input text to the autocompletion service.The default value is 1000.                                                                                                                                                                                                                                                                                                   | Integer                                                   |
| Validation               | Sets the JavaScript regular expression used to validate what the user entered in the field. Enter the pattern portion of the JavaScript regular expression as a string. For example, use\d* to validate against zero or more digits. If you set this field to a string variable instead, surround the content in the variable with quotation marks and use escape characters where necessary. For example, use"\\d*" to validate against zero or more digits. | String                                                    |