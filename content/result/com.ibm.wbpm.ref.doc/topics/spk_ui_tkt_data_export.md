# Data export

## Restrictions

## Configuration properties

Under Configuration,
set or modify the appearance and behavior properties for the view.

<!-- image -->

| Appearance configuration property   | Description                                                                                                                                                                                                                                | Data type   |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Color style                         | Specifies the color style for the view.                                                                                                                                                                                                    | String      |
| Shape style                         | Specifies the shape style for the view. The default is square.                                                                                                                                                                             | String      |
| Size style                          | Specifies the size of the view.                                                                                                                                                                                                            | String      |
| Outline only                        | Specifies whether the view displays its color-based style only when you hover a cursor over it. By default, this property is not selected.                                                                                                 | Boolean     |
| Icon                                | Specifies the name of the icon that precedes the text on the button. For example: calendar, clock-o, camera, cloud-upload, bell, info, file-text. See Font Awesome V4.7.0 for a complete list of icons.  By default, no icon is specified. | String      |
| Width                               | Specifies the width of the view in px (pixels), % (percent), or em units. For example, 50px, 20%, or 0.4em. If no unit type is specified, then px is assumed.                                                                              | String      |

| Behavior configuration property   | Description                                                                                                                                                                                                                                                                                                                                                                                                   | Data type    |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| Target control                    | Specifies the relative path to the table or repeating layout for populating the output file. If this view is bound to data, the value is overridden. Tip: If you experience issues with partial export of data, for example, with paginated tables, bind the Data export view to the same list variable as the table instead of using the Target control property.                                            | String       |
| Export file type                  | Specifies the file type of the output file: {Microsoft Excel 2007+ file type xlsx | Comma Separated Values file type csv}                                                                                                                                                                                                                                                                                     | String       |
| Default file name                 | Specifies the default name for the output file. Users can change the name when they save their files.                                                                                                                                                                                                                                                                                                         | String       |
| Include column headers            | Includes column headers at the top of the output file. If the view is bound to a table, and the Column headers property does not have any headers defined, the column headers of the bound table are included. If the view is bound to data, the settings in the Column headers property are used as the column headers.                                                                                      | Boolean      |
| Tab index                         | Specifies the tabbing sequence index. The tab indexes start at 1 and can be set sparsely. For example, you can use 1, 5, 10. The property controls the tabbing sequence when you move between UI areas by pressing the Tab key.                                                                                                                                                                               | Integer      |
| Include hidden columns            | Includes all columns, regardless of their visibility status. By default, columns that are not visible are not included in the output file. If this view is bound to data, all columns are included.                                                                                                                                                                                                           | Boolean      |
| Column formatting                 | Specifies configuration options for the exported columns. Column format string. The data format to use for each column in the output file, according to Microsoft formatting standards. When you export data to a .csv file, color styling in the target control is not preserved in the output file. For more information about Microsoft formatting standards, see Create or delete a custom number format. | ColumnSpec[] |
| Column headers                    | The headers of the exported columns. Requires the Include hidden columns property to be selected. If the view is bound to a table, these headers are used instead of the table column headers.                                                                                                                                                                                                                |              |

## Events

- On load: Activated when the view is loaded. For
example,console.log("DataExport loaded")
- On click: Activated when a user clicks the page and before the output file
is generated. For example,return ${Text1}.isValid();If the evaluated
expression returns false, the output file is not generated.
- On cell export: Activated when a cell is exported. The expression can
return a String, number, or Boolean value to replace the cell value, a null to cause the exported
cell to be blank, or an object containing a format property to override the cell's format. If an
object is returned, it can also contain a value property to override the exported value of the cell.
For example, me.setVisible("READONLY")

## Methods

For more information about the methods for Data export, see the Data export JavaScript API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.