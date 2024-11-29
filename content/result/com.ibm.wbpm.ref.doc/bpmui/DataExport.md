### Methods

### Parent

### Helpers

<!-- image -->

| Color style:   | The color style for this view.  {Default | Primary | Info | Success | Warning | Danger | Dark}                                                                                                      | ButtonColorStyle   |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|
| Shape style:   | Rounded, flat or square (default) view shape. {Default | Rounded | Flat}                                                                                                                            | ButtonShapeStyle   |
| Size:          | Size-based styling for this view (default, large, small, extra-small) {Default | Large | Small | Extra-Small}                                                                                       | ButtonSizeStyle    |
| Outline only:  | Shows the color-based style of the view only when it is hovered over.                                                                                                                               | Boolean            |
| Icon:          | Icon name, for example: calendar, clock-o, camera, cloud-upload, bell, info, file-text, etc... Check http://fontawesome.io/icons for a comprehensive list. (Note that the "fa-" prefix is optional) | String             |
| Width:         | The width in px, % or em.\r\nFor example\: 50px, 20%, 0.4em. If no unit is specified, px is assumed.                                                                                                | String             |

| Target view:            | Relative path to the table or repeating layout used to populate output file. Overridden if this view is bound to data.                                                                                                                                           | String        |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| Export file type:       | File type to export to {Microsoft Excel 2007+ file type xlsx | Comma Separated Values file type csv}                                                                                                                                                             | ExcelFileType |
| Default file name:      | Default name for file. Users will be able to change this when saving.                                                                                                                                                                                            | String        |
| Include column headers: | If the view is bound to a table, and the Column headers property is empty, the column headers of the bound table are included. If the view is bound to data, the settings in the Column headers property are used as the column headers.                         | Boolean       |
| Tab index:              | The tabbing sequence index of the form view. Indices start at 1, and can be set sparsely. For example, you can use 1, 5, 10.                                                                                                                                     | Integer       |
| Include hidden columns: | Include all columns, regardless of visibility status. By default, columns which are not visible will not be included in output file. When the view is populated by bound data, all columns will be included                                                      | Boolean       |
| Column formatting:      | Specific config options for exported columns. For more details on formatting strings, visit the following (hyperlinks in documentation)\: https\://support.office.com/en-us/article/Create-or-delete-a-custom-number-format-78f2a361-936b-4c03-8772-09fab54be7f4 | ColumnSpec[]  |
| Column headers:         | The headers of the exported columns. Requires the Include column headers property to be selected. If the view is bound to a table, these headers are used instead of the table column headers.                                                                   | String[]      |
| Column order:           | The column displaying order in the exported file. This option works only when the view is bound to data. The specified values must match the bound data parameters.                                                                                              | String[]      |

| Name     | Type     | Default   | Description                                                                                                     |
|----------|----------|-----------|-----------------------------------------------------------------------------------------------------------------|
| name     | {string} |           | CSS class name(s) to add to the control. Separate class names by a space if more than one class.                |
| replaced | {string} |           | CSS class name(s) to be replaced by the first argument. Separate class names by a space if more than one class. |

| Name       | Type               | Default   | Description                                                                                                                                                  |
|------------|--------------------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| targetPath | {?(string|object)} |           | Either path to target control or control view reference. If null or missing, will default to control returned by {@link DataExport#getTargetControl}.        |
| format     | {?string}          |           | File format to output to. Acceptable values incluse 'xlsx' and 'csv'. If null or missing, will default to format returned by {@link DataExport#getFileType}. |

| ${DataExport1}.exportFile() // exports a spreadsheet using currently set parameters for target control and file format                    |
|-------------------------------------------------------------------------------------------------------------------------------------------|
| ${DataExport1}.exportFile(${Table3}) // exports spreadsheet using data from Table3                                                        |
| ${DataExport1}.exportFile(${Table3}, 'csv') // exports spreadsheet using data from Table3 in csv format, regardless of any other settings |

| Name         | Type      | Default   | Description                                                               |
|--------------|-----------|-----------|---------------------------------------------------------------------------|
| collapseFlag | {boolean} |           | Set to true to collapse the view (equivalent to a view setting of "NONE") |

| Name   | Type    | Default   | Description                                    |
|--------|---------|-----------|------------------------------------------------|
| event  | {Event} |           | Value change event (usually an onchange event) |

| Name   | Type     | Default   | Description                                                                                                                                                                  |
|--------|----------|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| style  | {string} |           | "DEFAULT"|"DEF"|"D"=Default | "PRIMARY"|"PRI"|"P"=Primary | "INFO"|INF"|"I"=Info | "SUCCESS"|"S"=Success | "WARNING"|"WARN"|"W"=Warning | "DANGER"|ERROR|ERR"|"E"|"G"=Danger |

| Name   | Type                  | Default   | Description                                                                                                                                                                                                                                                                                                                       |
|--------|-----------------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| value  | {(string|string[])}   |           | Value to set format to. If value is a string, idx is required. If value is an array of strings, then a matching array of indexes may or may not be specified. If an array is specified, then each string in value will be mapped to the corresponding index in index. Otherwise, string array will replace current column formats |
| index  | {(integer|integer[])} |           | Index to set format at. If value is an array of strings, an array of indexes may be specified, which will map each format to the corresponding index.                                                                                                                                                                             |

| ${DataExport1}.setColumnFormats("$#", 1) // sets the 2nd column (index 1) to use "$#" as it's formatting string                                                                                          |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ${DataExport1}.setColumnFormats(["$#","#,##0.00","#%"], [1,3,5]) // sets the 2nd, 4th, and 6th columns (indices 1, 3, and 5) to use "$#", "#,##0.00", and "#%" as their formatting strings, respectively |
| ${DataExport1}.setColumnFormats(["$#","#,##0.00","#%"]) // sets the formatting for the 1st, 2nd, and 3rd columns to use "$#", "#,##0.00", and "#%" as their formatting strings, respectively             |

| Name    | Type       | Default   | Description            |
|---------|------------|-----------|------------------------|
| headers | {string[]} |           | List of column headers |

| Name   | Type      | Default   | Description                                                                   |
|--------|-----------|-----------|-------------------------------------------------------------------------------|
| flag   | {boolean} |           | Set to true to include column headers in output file, false to leave them out |

| Name     | Type      | Default   | Description                                                                   |
|----------|-----------|-----------|-------------------------------------------------------------------------------|
| enabled  | {boolean} |           | Enabled/read-only flag (true to enable view, false to disable/make read-only) |
| required | {boolean} |           | Enable/disable required field flag for control                                |

| Name   | Type     | Default   | Description                                                                                |
|--------|----------|-----------|--------------------------------------------------------------------------------------------|
| name   | {string} |           | Default name output file should have. Users will be able to change file name at save time. |

| Name   | Type     | Default   | Description                                                        |
|--------|----------|-----------|--------------------------------------------------------------------|
| type   | {string} |           | File format to output. Acceptable values include 'xlsx' and 'csv'. |

| Name   | Type     | Default   | Description             |
|--------|----------|-----------|-------------------------|
| text   | {string} |           | Rollover text to be set |

| Name   | Type     | Default   | Description                                                                                                                                                |
|--------|----------|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| icon   | {string} |           | See {@link http://fontawesome.io/icons Font Awesome} for a comprehensive list of icons. Refer to the knowledge center for the latest Font Awesome version. |

| Name   | Type      | Default   | Description                                                                          |
|--------|-----------|-----------|--------------------------------------------------------------------------------------|
| flag   | {boolean} |           | Set to true to include hidden columns/fields in output file, false to leave them out |

| Name    | Type      | Default   | Description                                                    |
|---------|-----------|-----------|----------------------------------------------------------------|
| visible | {boolean} |           | Label visibility flag (true to show view label, false to hide) |

| Name    | Type      | Default   | Description    |
|---------|-----------|-----------|----------------|
| outline | {boolean} |           | {true | false} |

| Name   | Type     | Default   | Description                                                            |
|--------|----------|-----------|------------------------------------------------------------------------|
| style  | {string} |           | "Default"|"D"=Default | "ROUNDED"|ROUND"|"R"=Rounded | "FLAT"|"F"=Flat |

| Name   | Type     | Default   | Description                                                                                                             |
|--------|----------|-----------|-------------------------------------------------------------------------------------------------------------------------|
| style  | {string} |           | "DEFAULT"|"DEF"|"NORMAL"|"D"=Default | "SMALL"|"S"=Small | "LARGE"|"L"=Large | "EXTRA-SMALL"|"X-SMALL"|"XS"|"X"=X-small |

| Name     | Type      | Default   | Description                                    |
|----------|-----------|-----------|------------------------------------------------|
| tabIndex | {integer} |           | Tab indices start at 1 and may be set sparsely |

| Name    | Type              | Default   | Description                                                                      |
|---------|-------------------|-----------|----------------------------------------------------------------------------------|
| control | {(string|object)} |           | Either the name of the control to use, or a view reference to the control to use |

| ${DataExport1}.setTargetControl("Table3") // sets the target control to Table3                                         |
|------------------------------------------------------------------------------------------------------------------------|
| ${DataExport1}.setTargetControl(${Table3}) // another way to set the target to Table3, this time passing Table3 itself |

| Name   | Type     | Default   | Description                         |
|--------|----------|-----------|-------------------------------------|
| text   | {string} |           | Text to be set on the export button |

| Name                | Type      | Default   | Description                                                                            |
|---------------------|-----------|-----------|----------------------------------------------------------------------------------------|
| data                | {Object}  |           | Value of bound data. The type of this parameter must match the type of the bound data. |
| createPseudoBinding | {boolean} |           | If set to true, creates a pseudo binding if there is no current binding.               |

| Name     | Type      | Default   | Description                                                             |
|----------|-----------|-----------|-------------------------------------------------------------------------|
| visible  | {boolean} |           | Visibility flag (true to show view, false to hide)                      |
| collapse | {boolean} |           | Set to true to collapse the control space when visible is set to false. |

| MyView.setVisible(false, false); //Equivalent to MyView.hide()   |
|------------------------------------------------------------------|
| MyView.setVisible(false, true); // Sets visibility to "None"     |

| Name   | Type     | Default   | Description      |
|--------|----------|-----------|------------------|
| width  | {string} |           | DataExport width |

| Name   | Type   | Default                | Description                   |
|--------|--------|------------------------|-------------------------------|
| phase  | {int}  | bpmext.ui.PHASE\_NORMAL | The phase we are currently in |