# Service data table

## Configuration properties

<!-- image -->

| Appearance configuration property   | Description                                                                                                                                            | Data type   |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Table style                         | Set the table style to use.                                                                                                                            | String      |
| Color style                         | Set the color style for the table.                                                                                                                     | String      |
| Highlight selection                 | Shades rows in a selected state. This option requires that a color style other than None be specified.                                                 | Boolean     |
| Width                               | The width in px, %, or em, for example 50px, 20%, or 0.4 em. If no unit is specified, px is assumed.                                                   | String      |
| Height                              | The height of the table in px or em (not including the header or footer if shown), for example 50px or 0.4 em. If no unit is specified, px is assumed. | String      |

| Behavior configuration property   | Description                                                                                                 | Data type    |
|-----------------------------------|-------------------------------------------------------------------------------------------------------------|--------------|
| Data service                      | The service flow with Ajax access to use with this view. The service flow supplies data to the table.       | Service Flow |
| Service data                      | Input data for the data service. Its type should match the input type for the service.                      | ANY          |
| Start empty                       | The table is initially empty. The table is populated by having the service run by using the refresh method. | Boolean      |
| Selection mode                    | The table item selection mode.                                                                              | String       |
| Show footer                       | Shows the table footer.                                                                                     | Boolean      |
| Show table stats                  | Shows the table statistics (for example Showing 1 to 5 of 59 entries).                                      | Boolean      |
| Show pager                        | Enables pagination.                                                                                         | Boolean      |
| Show page sizer                   | Enables the option to choose the number of rows to display per page.                                        | Boolean      |
| Initial page size                 | The initial maximum number of entries to be shown per page.                                                 | Integer      |

| Columns configuration property   | Description                                                                                                                                                                                                                        | Data type   |
|----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| dataElementName                  | Name of the data element to display for the column.                                                                                                                                                                                | String      |
| renderAs                         | Select how cell should be rendered.                                                                                                                                                                                                | String      |
| visibility                       | The visibility of the column.                                                                                                                                                                                                      | String      |
| sortable                         | If this option is enabled, users can sort the table by using this column.                                                                                                                                                          | Boolean     |
| options                          | Optional data to pass to the cell, depending on the type of data in the column: Decimal: thousandsSeparator, decimalPlaces, decimalSeparator, postfix, prefix - DatePicker: datePattern - Link: href - Integer: thousandSeparator. | String      |
| css                              | CSS options to add to the column, such as color:#00ff00.                                                                                                                                                                           | String      |
| width                            | The column width.                                                                                                                                                                                                                  | String      |
| label                            | Set the column label.                                                                                                                                                                                                              | String      |

| Performance configuration property   | Description                                                                                                                                                            | Data type   |
|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Async loading                        | Provides a better UI experience for large data sets (at the expense of slower overall row-loading time once the section starts loading).                               | Boolean     |
| Async batch size                     | Defines how many rows are loaded synchronously in an asynchronous batch. This option can help you optimize synchronous compared with asynchronous loading performance. | ANY         |

## Events

The user does not interact with the Service data table view, but rather the events are activated
when the user gets a result or error from the service flow call.

- On load: Activated when the table loads, for
example:me.setPageIndex(0);
- On service data loaded: Activated when a service flow with Ajax access that
supplies data to the table completes successfully, for
examplealert("service flow has returned with data");
- On service data error: Activated when a service flow with Ajax access that
supplies data to the table completes successfully, for
examplealert("service flow has returned with an error");
- On custom cell: Activated when a cell loads with custom rendering options
if the Render configuration value is set to Custom in
the Columns section, for
examplevar div = document.createElement("div"); div.innerHTML =cell.row.data[cell.varName]; return div;
- On rows loaded: Applicable only for paged tables, this event is activated
only when rows are displayed, for
examplealert("All rows have " + (all ? "" : "NOT") + " been loaded");
- On rows selected: Activated when a row is selected by a user, for
examplealert("Selected row has index " + row.index);
- On page sizer change: Activated when the user
changes the value for the per-page input field. For
example:me.showPager(true);

## Methods

For detailed information about the available methods for Service data table, see the Service data table JavaScript
API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.