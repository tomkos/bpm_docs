# Type ahead text

## Configuration properties

Under Configuration,
set or modify the appearance and behavior properties for the view.

<!-- image -->

| Appearance configuration property   | Description                                                                                                                                                                                                            | Data type   |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Width                               | Specifies the width of the view. You can specify the width in px (pixels), % (percent), or em units. For example, 50px, 20%, or 0.4em. If no unit type is specified, px is assumed. By default, no width is specified. | String      |
| Height                              | Specifies the width of the view. You can specify the width in px (pixels), % (percent), or em units. For example, 50px, 20%, or 0.4em. If no unit type is specified, px is assumed. By default, no width is specified. | String      |
| Label placement                     | Specifies one of the following label placement locations for the view:  Top: The label is placed at the top of the view.  Left: The label is placed at the left of the view.   The default value is Top.               | String      |
| Label width                         | The width of the label. You can specify the width in px (pixels), % (percent), or em units. For example, 50px, 20%, or 0.4em. If a unit type is not specified, px is assumed.                                          | String      |

| Behavior configuration property   | Description                                                                                                                                                    | Data type   |
|-----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Tab index                         | Specifies the tabbing sequence index of the form view. The tab indices start at 1 and may be set sparsely. By default, no tabbing sequence index is specified. | Integer     |
| Placeholder text                  | Text that is displayed when no text is entered.                                                                                                                | String      |
| Number of drop-down items         | The maximum number of drop-down items to display when the user starts typing. The default number is 4.                                                         | Integer     |

| Items configuration property   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Data type    |
|--------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| Item lookup mode               | Specifies the method you can use to populate the selection list. The available options are: Start Empty, Items From Service, Items From List.                                                                                                                                                                                                                                                                                                                                                                           | String       |
| Type-ahead items service       | A service flow with appropriate Ajax service access that populates the type-ahead list. The service is used when the lookup mode is Items From Service.Tip:  When the view is backed by a list items service, the service uses two variables: an input variable of type string named data, and an output variable of type list named results, which outputs the result as the data that is bound to the view. If the output variable name is not results of the list items service, no values will be available to use. | Service Flow |
| Items list                     | Items to populate the type-ahead list. The Item input data is used only if the item lookup mode is set to Items From List.                                                                                                                                                                                                                                                                                                                                                                                              | String[]     |

## Events

- On load: Activated when the view is loaded, for
exampleme.setPlaceholder(${Data1}.getValue())
- On change: Activated when the binding data changes, for
example${Service1}.setInputData(me.getText());${Service1}.execute()

## Methods

For detailed information about the available methods for Type ahead text, see the Type ahead text JavaScript
API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.