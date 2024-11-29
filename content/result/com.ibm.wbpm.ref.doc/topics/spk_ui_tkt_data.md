# Data

## Data binding

## Configuration properties

Under
Configuration, set or modify the behavior properties for the view.

The behavior configuration properties for Data are shown in the following table:

| Behavior configuration property   | Description                                                                         | Data type   |
|-----------------------------------|-------------------------------------------------------------------------------------|-------------|
| Value formula                     | The formula or expression for calculating the value of the data stored in the view. | String      |

## Events

- On load: Activated when the page loads. For example,
me.setValue(${Text1}.getText())
- On change: Activated when the bound data in the view is changed either
synchronously or asynchronously. For example,
${Text2}.setText(me.getValue())An example of an asynchronous change is when a
server variable is changed by a sever call, which might happen during a boundary event that ends in
a stay-on-page event.

## Methods

For information about the methods for Data, see the Data JavaScript API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.

For more information about business objects and variables, see Business objects and variables.