# Breadcrumbs

## Data binding

Set or modify the data binding for Breadcrumbs in the General properties
tab. Breadcrumbs can be bound to a NameValuePair variable, where
Name and Value are specified as type
String. If no data binding is used, the output data takes the type
ANY (loose data type).

## Events

Set
or modify the event handlers for the view in the Events properties. You can set
events to be triggered programmatically or when a user interacts with the view. For information about how to define and code events, see User-defined events. The Breadcrumbs view has the
following types of event handlers:

- On load: Activated when the view is loaded. For
example:console.log("BreadCrumbs loaded")
- On item click : Activated when the view is clicked. For example:alert("Breadcrumbs with label [" + label + "] on level " + item.level + " has data (if any) " +item.data); Whenthe Breadcrumbs view is clicked, the On item click event is passed thelabel of the level clicked (a string ) and theitem object. The item object contains threeproperties. Context variables label {String} item {object} Description Properties Note: When a breadcrumb entry is clicked, all the subsequent entries are deleted fromthe breadcrumb trail.

```
alert("Breadcrumbs with label [" + label + "] on level " + item.level + " has data (if any) " +item.data);
```

| Context variables   | label {String}    | item {object}    | Description                                                                                                                                                              |
|---------------------|-------------------|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Properties          |                   | label level data | The label of the item. An integer that represents the position of the item in the Breadcrumbs object, relative to 1. Any data that was set when the object was appended. |

Depending on the specific event, you can use JavaScript logic to modify the effects of the
view. More information on using events with views is found in the topic
User-defined events.

## Methods

For detailed information on the available methods for Breadcrumbs, see the Breadcrumbs JavaScript API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.