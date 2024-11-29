# Single select

## Data binding

Set or modify the data binding for the view in the General properties. The
view can be bound to an ANY  type.

## Configuration properties

Under Configuration,
set or modify the appearance and behavior properties for the view.

<!-- image -->

| Appearance configuration property   | Description                                                                                                                                                                                                                                                             | Data type   |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Width                               | The width of the view. You can specify the width in px (pixels), % (percent), or em units. For example, 50px, 20%, or 0.4em. If a unit type is not specified, px is assumed.                                                                                            | String      |
| Size                                | The size of the text in the view, the size of the label text, and the amount of padding around the text. For example, to make the text and label more readable on smart phones, you can set this configuration option to Large to compensate for the small screen size. | String      |
| Label placement                     | The position of the label.                                                                                                                                                                                                                                              | String      |
| Label width                         | The width of the label. You can specify the width in px (pixels), % (percent), or em units. For example, 50px, 20%, or 0.4em. If a unit type is not specified, px is assumed.                                                                                           | String      |

| Behavior configuration property   | Description                                                                                                                            | Data type   |
|-----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Tab index                         | The tabbing sequence index of the form control. The tab indices start at 1 and can be set sparsely. For example, you can use 1, 5, 10. | Integer     |
| Placeholder                       | Text that is displayed before a selection is made.                                                                                     | String      |

The items configuration properties for the Single select view are shown in the following
table:

| Item configuration property   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Data type         |
|-------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| Item lookup mode              | The method used to populate the list of items that the user can select from. Note: Make sure the correct option is selected, otherwise the list will not be populated correctly. Start Empty Programmatically populate the selection list using the appendItem(value, displayText) method.  Items From Service The selection list is populated from a service that you specify in the List items service option.  Items From Static List The selection list is populated by properties that you enter in the Static list option.  Items From Config Option The selection list is populated from a business object list that you specify in the Item input data option.                                                             | String            |
| List items service            | The service used to populate the list of items that appear in the selection list. The service is used when the Item lookup mode is Items From Service. The service is a service flow with appropriate Ajax access that provides the selection list based on the data provided by the Service input data business object. You can use this option as an alternative to binding the view to a list object.Tip:  The list items service uses two variables: an input variable of type string named data, and an output variable of type list named results, which outputs the result as the data that is bound to the view. If the output variable name is not results of the list items service, no values will be available to use. | Service flow      |
| Service input data            | A business object that provides the input data that is passed to the service flow that populates the selection list. This option is used when the Item lookup mode is Items From Service.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | ANY               |
| Ignore input data changes     | Disables the automatic service call when the service input data changes. This option is used only when Item lookup mode is set to Items From Service.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Boolean           |
| Item input data               | A business object list that populates the selection list. This property is used only if the Item lookup mode is Items From Config Option.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | ANY[]             |
| Item selection data           | In the Display property field, set the business object property to display in the selection list. If no values are specified for the data mapping properties, the default values are name for Value property, and value for Display property.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | SelectDataMapping |
| Output business data          | When the view is bound to a complex type, the property that the user selects is passed to the property specified in Display property and to the property that is bound to the view.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | SelectDataMapping |
| Static list                   | A static list of items to populate the selection list. Use this option only for a static list. Do not specify a variable for this option. For a variable list, use the Items From Config Option lookup mode.  Important:  The Name field in a value pair is used to calculate the value of another field, therefore it must be unique. To avoid unexpected behavior where variable data might be passed from one activity to another, ensure that the names used in the value pairs are unique.                                                                                                                                                                                                                                    | NameValuePair[]   |
| Enable clearing selection     | Show an option to clear the selection in the list.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Boolean           |

The selection state is copied to the listSelected property in the input business object list. You
can retrieve the selection by binding a view to this property. See Example: Populating items by using a list business object.

## Example: Populating items from a static list

This example uses a Single select view with the label Grocery list and the
Item lookup mode  set to Items From Static List

| Name   | Value   |
|--------|---------|
| Item 1 | Bread   |
| Item 2 | Milk    |
| Item 3 | Bananas |
| Item 4 | Rice    |

<!-- image -->

## Example: Calculating totals using items from a static list

This example uses the value of the Name field in a static list to
calculate the value of another field.

The coach or page has a Horizontal Layout that contains a Single select view, an Integer view and
a Decimal view. The coach or page also has a Button view.

- General > Common > Labelis Item.
- General > Common > Control ID is Item.
- Configuration > Behavior > Placeholder is Select Item.
- Configuration > Items > Item lookup mode is Items From Static List.
- Configuration > Items > Static list has the following entries:
    - Name is .50, and Value is
Apple.
    - Name is .75, and Value is
Orange.
    - Name is .25, and Value is
Banana.

- General > Label is Quantity.
- General > Control ID is Quantity.

- General > Label is Total.
- Behavior > Decimal places is 2.
- Events > Value formula has the following entry:@{Item}*@{Quantity} where Item is the
control ID of the Single select view, and Quantity is the control ID of the Integer view.

The Button view has the label OK.

<!-- image -->

<!-- image -->

## Example: Populating items from a service flow

This example uses a service flow with Ajax access to initialize a list that is used as the
selection list.

Note: By default, Ajax access is allowed only to trusted callers. To run the coach or page in
Process Designer, go to the Overview tab in the service flow and change the
Ajax access to Allow calls from all callers.

- Configuration > Behavior > Label is Grocery List.
- Configuration > Behavior > Placeholder is Select Item.
- Configuration > Items > Item lookup mode is Items From Service.
- Configuration > Items > List items service is Retrieve Items Service.Note: To create a service flow,
click New beside the List items service
option.
- Configuration > Items > Item selection data has the following settings:
    - Value property is name.
    - Display property is value.

```
tw.local.results = new tw.object.listOf.NameValuePair();

tw.local.results[0] = new tw.object.NameValuePair();
tw.local.results[0].name = "Item 0";
tw.local.results[0].value = "Milk";

tw.local.results[1] = new tw.object.NameValuePair();
tw.local.results[1].name = "Item 1";
tw.local.results[1].value = "Bread";

tw.local.results[2] = new tw.object.NameValuePair();
tw.local.results[2].name = "Item 2";
tw.local.results[2].value = "Bananas";

tw.local.results[3] = new tw.object.NameValuePair();
tw.local.results[3].name = "Item 3";
tw.local.results[3].value = "Rice";
```

<!-- image -->

<!-- image -->

<!-- image -->

## Example: Populating items by using a list business object

This example uses a cust[] list object of type Customer to populate a list of first names in the
selection list. When the user selects a name, the selection is displayed in a text box. The
client-side human service has the private variables cust and
output, both of type Customer.

- An ID parameter of type String.
- A firstname parameter of type String.
- A lastname parameter of type String.

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

- General > Label is Name.
- General > Binding is output.firstName.
- Configuration > Behavior > Placeholder is Select a name.
- Configuration > Items > Item lookup mode is Items From Config Option.
- Configuration > Items > Item input data is Customer[].
- Configuration > Items > Item selection data has the following settings:
    - Value property is ID.
    - Display property is firstName.
- Configuration > Items > Output business data has the following settings:

- Value property is ID.
- Display property is firstName.

- General > Label is Text.
- General > Binding is cust.listSelected.firstName.

<!-- image -->

<!-- image -->

## Events

Set
or modify the event handlers for the view in the Events properties. You can set
events to be triggered programmatically or when a user interacts with the view. For information about how to define and code events, see User-defined events.

The Single select view has the following types of event handlers:

- On load: Activated when the coach or page loads. For example:
console.log(me.getItemCount());
- On change: Activated when the bound data changes. For example:
${SingleSelect2}.reloadServiceItems(me.getSelectedIndices());
- On service items: Activated when the called service returns a list of
items. Activated only if Item lookup mode is set to Items From
Service. console.log("SingleSelect1 item service retrieved items
successfully");
- On service error: Activated when the called service returns an service
error. Activated only if Item lookup mode is set to Items From
Serviceme.clearItems();

## Methods

For detailed information on the available methods for the Single select view, see the Single select JavaScript
API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.