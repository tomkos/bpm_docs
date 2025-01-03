# Defining a property type

Set the type property for a page widget property or an action property to one of the following
values.

| Property type   | Description                                                                         |
|-----------------|-------------------------------------------------------------------------------------|
| Tab             | Defines a new tab in the Edit Settings window.                                      |
| Section         | Defines a section that can be expanded and collapsed.                               |
| Dropdown        | Defines a drop-down list that is used to select a value from a group of properties. |
| propertyPanel   | Defines a content pane in which a group of properties are displayed.                |

| Property type   | Description                                   |
|-----------------|-----------------------------------------------|
| Boolean         | Defines a property that has a Boolean value.  |
| Datetime        | Defines a property that has a datetime value. |
| Float           | Defines a property that has a float value.    |
| Integer         | Defines a property that has an integer value. |
| String          | Defines a property that has a string value.   |

```
{
   "propertyType":"property",
   "type":"integer",
   "id":"integer1",
   "defaultValue":20,
   "required":false,
   "visibility":true,
   "title":"Integer property 1"
},
{
   "propertyType":"property",
   "type":"float",
   "id":"float1",
   "defaultValue":12.34,
   "required":false,
   "visibility":true,
   "title":"Float property 1"
},
{
   "propertyType":"property",
   "type":"boolean",
   "id":"boolean1",
   "defaultValue":false,
   "required":false,
   "visibility":true,
   "title":"Boolean property 1"
},
{
   "propertyType":"property",
   "type":"string",
   "id":"string1",
   "defaultValue":"default string",
   "required":false,
   "visibility":true,
   "title":"String property 1"
},
```

The following example shows a datetime property for a custom page widget. This property is
defined in the properties section of the page widget definition file as follows:

```
{
   "propertyType":"property",
   "type":"datetime",
   "id":"datetime1",
   "defaultValue":"2013-05-01T03:00:00Z",
   "required":false,
   "visibility":true,
   "title":"Date Time 1"
},
```

| Property type   | Description                                                                                                                                                                                   |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| caseType        | Displays an editor that enables users to select a case type in Case Builder.                                                                                                                  |
| Choicelist      | Displays a choice list for the property. This value can be used with other property types such as String.                                                                                     |
| contextualMenu  | Displays an editor that enables users to edit a menu for a page widget in Case Builder.                                                                                                       |
| Label           | Provides a read-only label that is displayed for the property. This value must be set to label for an action.                                                                                 |
| Order           | Displays an editor that enables users to configure the order of the tabs in the Case Information widget.                                                                                      |
| Role            | Displays a list of roles that are available in the solution from which the user can select.                                                                                                   |
| Task            | Displays a list of tasks that are available in the solution from which the user can select.                                                                                                   |
| Textarea        | Displays an input field in which the user can enter a text string.                                                                                                                            |
| Toolbar         | Displays an editor that enables users to edit a toolbar for a page widget in Case Builder.                                                                                                    |
| View            | Displays a selection list that contains all the views that are available for the case types in a solution.                                                                                    |
| viewList        | Displays a list of case type-view pairs that enables the user to select a view. This property enables the user to add multiple views into the list. The output is a list of view identifiers. |