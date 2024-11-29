# Check box group

## Data binding

Set or modify the data binding for the Check box group in the General
properties. The binding for the Check box group view is defined as a list of ANY
(ANY []), which represents the check boxes that are selected by the user,
but in practice, the binding needs to be either a list of strings or
a list of NameValuePair like objects which have Name and Value properties.

## Configuration properties

Under Configuration, set or modify the appearance and
items properties for the view.

<!-- image -->

| Appearance configuration property   | Description                                                                                                                                                                                              | Data type   |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Width                               | Specifies the width of the Check box group view. You can specify the width in px (pixels), % (percent), or em units. For example, 50px, 20%, or 0.4em. If no unit type is specified, then px is assumed. | String      |
| Label placement                     | Specifies where to put the label. The available options are Top and Left.  Note that labels placed on the left change the specified width of the view.                                                   | String      |
| Label width                         | The width of the label. You can specify the width in px (pixels), % (percent), or em units. For example, 50px, 20%, or 0.4em. If a unit type is not specified, px is assumed.                            | String      |
| Show validation marker              | Show a validation icon and border when the view is invalid.                                                                                                                                              | Boolean     |

| Items configuration property   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Data type                                                            |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| Item lookup mode               | The method used to populate the list of items that the user can select from. Note: Make sure the correct option is selected, otherwise the list will not be populated correctly. Start Empty Programmatically populate the selection list using the appendItem(value, displayText) method.  Items From Service The selection list is populated from a service that you specify in the List items service option.  Items From Static List The selection list is populated by properties that you enter in the Static list option.  Items From Config Option The selection list is populated from a business object list that you specify in the Item input data option.                                                             | String                                                               |
| List items service             | The service used to populate the list of items that appear in the selection list. The service is used when the Item lookup mode is Items From Service. The service is a service flow with appropriate Ajax access that provides the selection list based on the data provided by the Service input data business object. You can use this option as an alternative to binding the view to a list object.Tip:  The list items service uses two variables: an input variable of type string named data, and an output variable of type list named results, which outputs the result as the data that is bound to the view. If the output variable name is not results of the list items service, no values will be available to use. | AJAX Service                                                         |
| Service input data             | A business object that provides the input data that is passed to the service flow that populates the selection list. This option is used when the Item lookup mode is Items From Service.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | ANY                                                                  |
| Ignore input data changes      | Disables the automatic service call when the service input data changes. This option is used only when Item lookup mode is set to Items From Service.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Boolean                                                              |
| Item input data                | A business object list that populates the selection list. This property is used only if the Item lookup mode is Items From Config Option.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | ANY[]                                                                |
| Item selection data            | In the Display property field, set the business object property to display in the selection list. If no values are specified for the data mapping properties, the default values are name for Value property, and value for Display property.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | String Option value property: String Option display property: String |
| Static list                    | A static list of items to populate the selection list. Use this option only for a static list. Do not specify a variable for this option. For a variable list, use the Items From Config Option lookup mode.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | NameValuePair[]                                                      |

## Example

1. Under General, specify a name for your check box group, for example,
Needed office supplies:.
2 Under Items :
    - Set Item lookup mode to Items From Static
List.
    - Under Items list, expand Static list, and then use
the plus (+) buttons to add the following name and value pairs to the list:
Name
Value

1
Notepads

2
Pens

3
Printer ink

4
File folders
    - Under Appearance, set Width to
350px, and Label placement to
Left.
    - Save your changes.

- Notepads
- Pens
- Printer ink
- File folders

## Events

Set
or modify the event handlers for the view in the Events properties. You can set
events to be triggered programmatically or when a user interacts with the view. For information about how to define and code events, see User-defined events. Check box group has the following
types of event handlers:

- On load: Activated when the page loads. For example:
console.log(me.getItemCount())
- On service items: Activated when the service flow returns the items list.
It gets activated when Item lookup Mode is set to Items From
Service. For example:
console.log("CheckboxGroup1 item service retrieved items successfully")
- On service error: Activated when the selection service returns an error. It
gets activated when Item Lookup Mode is set to Items From
Service. For example: me.clearItems()
- On change: Activated when the bound data changes, such as when a check box
button is selected. For example:
${CheckboxGroup2}.reloadServiceItems(me.getSelectedIndices())

Depending on the specific event, you can use JavaScript logic to modify the effects of the view.
More information on using events with views is found in the topic User-defined events.

## Methods

For detailed information on the available methods for the Check box group, see the Check box group JavaScript
API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.