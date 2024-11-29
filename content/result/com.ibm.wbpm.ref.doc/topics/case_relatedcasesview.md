# Related Cases

This correlation among cases facilitates the grouping of similar cases and enables case workers
to efficiently handle batch processing, prioritizing related cases with greater effectiveness.

1. From the Case Details page, select the Related Items
tab.Note: Cases that are already related to the selected case appear in the table.
2. To relate a new case, click Add Related.
3. In the Add Related dialog box, use the filter criteria to search for
cases. By default, the filter criteria displays the properties Added On and
Case Identifier which can be used to search for cases. To have more
properties listed in the filter criteria, add properties into the Case Search
view while authoring the solution. For more
information, see Designing views.
4. Select one or more cases from the list and click Relate.
5. A Relationship dialog box appears, where you can add a comment on the
relationship between the cases. This is optional. You can link cases by choosing a relationship
name from the Current case relates to drop-down list, which connects the
current case to the chosen cases. Also, you can select a relationship name from the
Relate the selected items as drop-down list to link the chosen cases to the
current case. Examples of predefined relationship names that might appear in the drop-down list
include Buyer, Seller, Customer Representative, Customer, Sales Representative, and others. If there
are no predefined relationship names, the default relationship name is set to
Related.
6. The case that is related now appears in the Related Items tab.

- To separate cases that are already related, either choose Unrelate from
the overflow menu or click Unrelate after selecting the case from the
table.
- To view details of the case, select View from the overflow menu.

## Configuration properties

| Property                    | Description                                                                                                                          | Data type   |
|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Case Identifier             | The Case Identifier of the case instance as required by the view.                                                                    | String      |
| Target Object Store Name    | The repository name that the view needs to connect.                                                                                  | String      |
| Is Case Client              | The option set to indicate whether the view is used in the context of Case Client or Workplace.                                      | Boolean     |
| Solution Prefix             | The prefix of the solution that is being deployed.                                                                                   | String      |
| Columns                     | Case instance properties to be rendered at run time in a table. Details of the configuration options in column are given in table 2. |             |
| Relationship Names          | List of relationship names used when you link cases.                                                                                 | String      |
| Get Repository Name Service | Service to retrieve the repository name that is associated to the case instance.                                                     | Service     |

| Property   | Description                                                                                                                                                                                                                                                                                                                                                                                          | Data type   |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Property   | Symbolic name of a case instance property. Case Business Object is not supported.                                                                                                                                                                                                                                                                                                                    | String      |
| Label      | Label of the column that renders as a table column header at run time.                                                                                                                                                                                                                                                                                                                               | String      |
| Render as  | Denotes the format in which the cell contents are to be rendered. Possible values: Simple HTML Custom                                                                                                                                                                                                                                                                                                | String      |
| Visibility | The visibility of the column. Possible values: Visible Read-Only None                                                                                                                                                                                                                                                                                                                                | String      |
| Sortable   | Select the checkbox to allow the data in the column to be sorted.                                                                                                                                                                                                                                                                                                                                    | String      |
| Options    | Options to format the data in the column, depending on the data type.Date Picker  For example, if the required format is Monday 08 Jun, 2015, enter: "datePattern":"EEEE dd MMM, yyyy" These options work only if the column is rendered as HTML or Custom. For custom rendering, in the On custom cell event, use the cell.getFormattedValue() function to get a value with the applied formatting. | String      |
| CSS        | The CSS styling to be applied to the column. You can use CSS style (For example - color:#00ff00) or CSS classes. If a colon is included in this field, the table control assumes the CSS style. Otherwise, it assumes that one or more CSS class names are specified.                                                                                                                                | String      |
| Width      | Width of column in px, em, or %. If no unit is specified, the value is assumed in px. Note: Consider leaving a single column width undefined so that the browser can calculate any remaining space and assign it to the column whose width is not specified.                                                                                                                                         | String      |

| Property           | Description                                          | Data type   |
|--------------------|------------------------------------------------------|-------------|
| Relationship Names | Users can set names in the Custom Case Details page. | String      |