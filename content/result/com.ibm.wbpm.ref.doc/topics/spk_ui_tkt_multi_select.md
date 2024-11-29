# Multi select

## Data binding

Set or modify the data binding for the view in the Configuration properties.
The view can be bound to an ANY (List) type.

## Configuration properties

Under Configuration,
set or modify the appearance and behavior properties for the view.

<!-- image -->

| Appearance configuration property   | Description                                                                                                                                                                                                                                                             | Data type   |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Width                               | The width of the view. You can specify the width in px (pixels), % (percent), or em units. For example, 50px, 20%, or 0.4em. If a unit type is not specified, px is assumed.                                                                                            | String      |
| Size                                | The size of the text in the view, the size of the label text, and the amount of padding around the text. For example, to make the text and label more readable on smart phones, you can set this configuration option to Large to compensate for the small screen size. | String      |
| Label placement                     | The label placement locations for the view.                                                                                                                                                                                                                             | String      |
| Label width                         | The width of the label. You can specify the width in px (pixels), % (percent), or em units. For example, 50px, 20%, or 0.4em. If a unit type is not specified, px is assumed.                                                                                           | String      |
| Show validation marker              | Show a validation icon and border when the view is invalid.                                                                                                                                                                                                             | Boolean     |

| Behavior configuration property   | Description                                                                                                        | Data type   |
|-----------------------------------|--------------------------------------------------------------------------------------------------------------------|-------------|
| Tab index                         | The tabbing sequence index. The tab indices start at 1 and may be set sparsely. For example, you can use 1, 5, 10. | Integer     |

| Item configuration property   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Data type         |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| Item lookup mode              | The method used to populate the list of items that the user can select from. Note: Make sure the correct option is selected, otherwise the list will not be populated correctly. Start Empty Programmatically populate the selection list using the appendItem(value, displayText) method.  Items From Service The selection list is populated from a service that you specify in the List items service option.  Items From Static List The selection list is populated by properties that you enter in the Static list option.  Items From Config Option The selection list is populated from a business object list that you specify in the Item input data option.                                                              | String            |
| List items service            | The service used to populate the list of items that appear in the selection list. The service is used when the Item lookup mode is Items From Service. The service is a service flow with appropriate Ajax access that provides the selection list based on the data provided by the Service input data business object. You can use this option as an alternative to binding the view to a list object. Tip:  The list items service uses two variables: an input variable of type string named data, and an output variable of type list named results, which outputs the result as the data that is bound to the view. If the output variable name is not results of the list items service, no values will be available to use. | Service flow      |
| Service input data            | A business object that provides the input data that is passed to the service flow that populates the selection list. This option is used when the Item lookup mode is Items From Service.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | ANY               |
| Ignore input data changes     | Disables the automatic service call when the service input data changes. This option is used only when Item lookup mode is set to Items From Service.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Boolean           |
| Item input data               | A business object list that populates the selection list. This property is used only if the Item lookup mode is Items From Config Option.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | ANY[]             |
| Item selection data           | In the Display property field, set the business object property to display in the selection list. If no values are specified for the data mapping properties, the default values are name for Value property, and value for Display property.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | SelectDataMapping |
| Output business data          | When the view is bound to a complex type, the property that the user selects is passed to the property specified in Display property and to the property that is bound to the view.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | SelectDataMapping |
| Static list                   | A static list of items to populate the selection list. Use this option only for a static list. Do not specify a variable for this option. For a variable list, use the Items From Config Option lookup mode.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | NameValuePair[]   |

## Example: Items from a static list

|   Name | Value   |
|--------|---------|
|      1 | Milk    |
|      2 | Bread   |
|      3 | Bananas |
|      4 | Rice    |

<!-- image -->

## Example: Populating items by using a business object

This example uses a Customer business object to populate a list of first names in the selection
list. When the user selects multiple names, the corresponding record is displayed in a table.

- An ID parameter of type String.
- A firstName parameter of type String.
- A lastName parameter of type String.

```
var autoObject = [];
autoObject[0] = {};
autoObject[0].ID = "000";
autoObject[0].firstName = "Pierre";
autoObject[0].lastName = "de Fermat";
autoObject[1] = {};
autoObject[1].ID = "001";
autoObject[1].firstName = "Isaac";
autoObject[1].lastName = "Newton";
autoObject[2] = {};
autoObject[2].ID = "002";
autoObject[2].firstName = "John";
autoObject[2].lastName = "Venn";
autoObject
```

The client-side human service has a private variable outputList of type
Output[]. The Output type has two string parameters, value1
and value2. The Multi select view is bound to outputList,
which contains the data output of the view.

- Under General, set Binding to
outputList.
- Under Configuration > Items, set  Item lookup mode to Items From Config
Option.
- Under Configuration > Items, set Item input data to Customer[].
- Under Configuration > Items > Item selection data :
    - For Value property, specify ID.
    - For Display property, specify firstName.
- Under Configuration > Items > Output business data :

- For Value property, specify value1.
- For Display property, specify value2.

- Two columns titled Value1 and Value2
- Under General, Label is set to Output
List.
- Under General, Binding is set to
outputList[].

<!-- image -->

<!-- image -->

<!-- image -->

## Events

Set
or modify the event handlers for the view in the Events properties. You can set
events to be triggered programmatically or when a user interacts with the view. For information about how to define and code events, see User-defined events.

The Multi select view has the following types of event handlers:

- On load: Activated when the page loads. For example:
console.log(me.getItemCount());
- On change: Activated when the bound data changes. For example:
${MultiSelect2}.reloadServiceItems(me.getSelectedIndices());
- On service items: Activated when the service flow returns an item list.
Activated only if Item lookup mode is set to Items From
Service. console.log("MultiSelect1 item service retrieved items
successfully");
- On service error: Activated when the service flow returns an service error.
Activated only if Item lookup mode is set to Items From
Serviceme.clearItems();

Depending on the specific event, you can use JavaScript logic to modify the effects of the
view. More information on using events with views is found in the topic
User-defined events.

## Methods

For detailed information on the available methods for Multi select, see the Multi select JavaScript API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.