# Table

## Data binding

Set or modify the data binding for the view in the General properties tab.
The table view is bound to a list of objects that populates the rows.

## Configuration properties

Under Configuration, set or modify the configuration
properties for the view.

<!-- image -->

| Appearance configuration property   | Description                                                                                                                                                                                                                                                                                                                                                                    | Data type       |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| Table style                         | The style of the table.  You can choose between the following options:  Default (no borders, light gray background) Elegant (horizontal borders, white background) Bordered (borders around cells) Striped (rows on alternating white and light gray background) Hover row (row highlighted in gray at hover over) Condensed (compact appearance through reduced cell padding) | TableStyle      |
| Color style                         | The color style of the table. The colors correspond to variables in the specified theme. You can choose between the following options: None Light (light gray) Primary (dark blue) Info (light blue) Success (green) Warning (orange) Danger (red)                                                                                                                             | TableColorStyle |
| Highlight selection                 | Shades rows that are selected. This option does not work if the color style is none.                                                                                                                                                                                                                                                                                           | Boolean         |
| Width                               | Specifies the width of the table. You can specify the width in px (pixels), % (percent), or em units. For example, 50px, 20%, or 0.4em. If no unit type is specified, then px is assumed.                                                                                                                                                                                      | String          |
| Height                              | Specifies the height of the view in px (pixels) or em units. If no unit type is specified, then px is assumed. The height does not include the header or footer. If you specify a height and the rows exceed the available vertical space in the body of the table, the body becomes vertically scrollable.                                                                    | String          |
| Wrap column headers                 | Wraps column headers depending on the space available to the table.                                                                                                                                                                                                                                                                                                            | Boolean         |
| Show pop-ups                        | Pop-up menus and views appear over the table when the height is not specified. For example, if this option is selected, a Date Time Picker view appears over the table. Otherwise, the Date Time Picker is embedded in the table cell.                                                                                                                                         | Boolean         |
| Style header and footer             | Enables you to apply a different header and footer style. The Modern style, for example, streamlines pagination in the header and footer.                                                                                                                                                                                                                                      | TableHFStyle    |

| Behavior configuration property   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Data type          |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|
| Selection mode                    | Specify how many rows a user can select: None Single Multiple  For a table in Multiple selection mode, Select All selects all the data that is bound to that table.                                                                                                                                                                                                                                                                                                                                                                         | TableSelectionMode |
| Show Delete button                | Show or hide the button to delete a row.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Boolean            |
| Show Footer                       | Show or hide the footer.  The footer is also displayed if any of the footer views are enabled, for example, Show Add button.                                                                                                                                                                                                                                                                                                                                                                                                                | Boolean            |
| Show Add button                   | Show or hide the button to add a row. If the table is sorting or filtering, the newly added row may not be displayed as the last row in the table, or may not be displayed at all until sorting or filtering is cleared. Note that if you choose a Modern header and footer style and want to show the Add button, you must also select the Show footer option.                                                                                                                                                                             | Boolean            |
| Show table stats                  | Enables the display of table stats in the footer. For example, Showing 1 to 5 of 59 entries. Note that you must also select the Show footer option.                                                                                                                                                                                                                                                                                                                                                                                         | Boolean            |
| Show pager                        | Show or hide the number of pages. The pager only displays 5 pages, therefore, depending on the initial page size, and the number of records, the pages may not be consecutive (1, 2, 3...). For example: The table has a total of 50 entries, and the initial page size is set to 5. The page numbers that are shown are 1, 3, 5, 7, 10. The user clicks the Next  button to navigate through the pages in order, or uses the page number buttons to move quickly through the pages. Note that you must also select the Show footer option. | Boolean            |
| Show page sizer                   | Show or hide the page sizer which displays the number of rows on a page.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Boolean            |
| Initial page size                 | The number of rows displayed on a page.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Integer            |
| Resize columns                    | Allow users to resize columns by dragging the column separators.                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Boolean            |
| ANY type                          | The specification of the business object definition type when the view is bound to an ANY type list.                                                                                                                                                                                                                                                                                                                                                                                                                                        | TableANYType       |

| Column configuration property   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Data type   |
|---------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Render as                       | How cell contents should be rendered:  Coach View Seamless Coach View Simple HTML Custom  Views that are nested in table cells, such as Integer and Date Picker (deprecated), typically have visible borders. The table also has its own border. To remove the borders of the nested views, use a Seamless view. If you are using Coach View or Seamless Coach View, select showLabel to show the label of the nested view. For more information, see Rendering types.                                                                                                                                                                         | String      |
| Visibility                      | The column visibility.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | String      |
| Sortable                        | Allow the data in this column to be sorted. By default, only columns that are bound to simple types can be sorted. To sort a complex type you must set Render as to Custom and use an On custom cell event. For example:var div = document.createElement("div"); div.innerHTML = cell.row.data["firstName"]; cell.setSortValue(cell.row.data["firstName"]); return div;                                                                                                                                                                                                                                                                        | Boolean     |
| Options                         | Options to format the data in the column, depending on the data type.  Date Picker datePatternFor example, if the desired format is Monday 08 Jun, 2015, enter: "datePattern": "EEEE dd MMM, yyyy"  Decimal thousandsSeparator, decimalPlaces, decimalSeparator, postfix, prefix For example:  "decimalPlaces": 2, "decimalSeparator": ".", "thousandSeparator": ",", "prefix": "$"  Integer thousandSeparator Link href   These options work only if the column is rendered as as HTML or Custom. With Custom rendering, inside of the On custom cell event, you can use cell.getFormattedValue() to get a value with the formatting applied. | String      |
| CSS                             | The CSS styling to apply to the column. You can use CSS style (for example, For example, color:#00ff00 ) or CSS classes. If there is a colon in this field, the table view assumes that you have specified a CSS style. Otherwise, it assumes that you have specified one or more CSS class names.                                                                                                                                                                                                                                                                                                                                             | String      |
| Width                           | Width of column in px, em, or %. If no unit is specified px is assumed. Note: Consider leaving one column's width undefined so that the browser can calculate any remaining space and assign it to the column whose width is not specified.                                                                                                                                                                                                                                                                                                                                                                                                    | String      |
| Label                           | The label of the column.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | String      |
| showLabel                       | When the cell is rendered as a Coach View or a Seamless Coach View, shows or hides the view label.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Boolean     |

| Performance configuration property   | Description                                                                                                                                            | Data type   |
|--------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Async loading                        | Provides a better UI experience for large data sets (at the expense of slower overall row-loading time once the section starts loading).               | Boolean     |
| Async batch size                     | Defines how many rows are loaded synchronously in an asynchronous batch. This can help tune/optimize synchronous vs. asynchronous loading performance. | Integer     |

## Example

- A name parameter of type String.
- A favoriteSport parameter of type String.
- A favoritePlayer parameter of type String.

```
var autoObject = [];
autoObject[0] = {};
autoObject[0].name = "Dylan";
autoObject[0].favoriteSport = "Tennis";
autoObject[0].favoritePlayer = "Federer";
autoObject[1] = {};
autoObject[1].name = "Max";
autoObject[1].favoriteSport = "Soccer";
autoObject[1].favoritePlayer = "Messi";
autoObject
```

The client-side human service has a private variable profiles of type
Profiles[].

- General > Label is Profiles - Coach One.
- General > Binding is profiles[].
- A Name column with binding profiles.currentItem.name
- A Favorite Sport column with binding
profiles.currentItem.favoriteSport
- A Favorite Player column with binding
profiles.currentItem.favoritePlayer
- Configuration > Behavior
    - Selection mode is Single
    - Show Delete button is selected
    - Show footer is selected
    - Show Add button is selected
    - Show table stats is selected
- Configuration > Columns has three entries with the following settings:

- RenderAs is set to Coach View
- Visibility is set to Visible
- Sortable is selected

In the client-side human service, create a copy of the page and wire it to the first page. In the
second page, change the Table label to Profiles - Coach Two.

<!-- image -->

<!-- image -->

<!-- image -->

## Rendering types

## Events

Set
or modify the event handlers for the view in the Events properties. You can set
events to be triggered programmatically or when a user interacts with the view. For information about how to define and code events, see User-defined events.

Table has the following types of event handlers:

- On load: Activated when the table loads. For example:
me.setPageIndex(0);
- On custom cell: Activated when a cell that has custom rendering options
(set in the Columns configuration) loads. To use this event, you must set the Render as
configuration value to Custom in the Columns configuration. You can also use this
event to set cell.setSortValue(cell.value) for complex types. For example:
var div = document.createElement("div"); 
div.innerHTML = cell.row.data[cell.varName]; 
return div;
- On rows loaded: Activated when the rows are displayed. This event is
applicable only for paged tables. For example:
alert("All rows have " + (all ? "" : "NOT") + " been loaded");
- On expandable row loaded: This event fires when an expandable row loads. To
use this event, you must enable allow expandable rows config option. For example when the row is
rendered as Coach
View:row.views.forEach(function(view) { switch(view.context.viewid) { case "Text1": view.setData(row.data[varName]); break; case "Text2": view.setData(row.data[varName]); break; } });
Example when the row is rendered as
Custom:var div = document.createElement("div"); div.innerHTML = row.data[varName] + " " + row.data[varName]; return div;
- On row expanded: Triggers when the row expands. For example:
${Service\_Call1}.execute();
- On row collapsed: Triggers when the row collapses. For
example:alert("Collapsed row has index " + row.recordIndex);
- On row selected: Activated when the user selects a row. For example:
alert("Selected row has index " + row.recordIndex);
- On all rows selected: Activated when the user
uses Select All to select all the rows in a table that is in
Multiple selection mode or to clear the selection on all the table rows. It
provides a context variable that is named all to indicate that all or none of the
rows are selected. For example: alert("All rows selected: " + all);
- On row added: This event is called when a row is being added by the user
through the Add Row button. If it returns a JavaScript object, then the object is
added , otherwise an empty object is added. For
example:alert("New row will be added");
- On row deleted: Activated when the user asks to delete a record. If the
event returns false, the record is not deleted. This event can be used to require
user confirmation before the record is officially deleted. For
example:return confirm("Are you sure you want to delete item " + item.str1);
- On sorting by column header: Activated
when the user clicks the sort icon in a table column header. It returns false to
use the custom sorting and skip the default table sorting. You can use this event to set
me.context.binding.set("value", myCustomSortedList) to a custom-sorted list. For
example:alert("Sorting " + col + " column in " + order + " order"); 
me.context.binding.set("value", myCustomSortedList); 
return false;
- On page sizer change: Activated when the user
changes the value for the per-page input field. For
example:me.showPager(true);
- On column resized: Activated when the user resizes a column. For
example:alert("Column resized");
- On column dropped: Activated when the user drags and
drops a column.alert("Column dropped");

## Methods

For detailed information on the available methods for Table, see the Table JavaScript API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.