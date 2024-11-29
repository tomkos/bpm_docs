### Methods

### Parent

### Helpers

<!-- image -->

| Table style:             | The table style {Default | Elegant | Bordered | Striped | Hover Row | Condensed}                                                                                                                                      | TableStyle      |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| Color style:             | Color style of the table {None | Light | Primary | Info | Success | Warning | Danger}                                                                                                                                 | TableColorStyle |
| Highlight selection:     | Shade selected rows. A Color Style other than None must be specified.                                                                                                                                                 | Boolean         |
| Width:                   | The width in px, % or em.\r\nFor example\: 50px, 20%, 0.4em. If no unit is specified, px is assumed.                                                                                                                  | String          |
| Height:                  | The height of the table in px, %, em. The header or footer are not included.\r\nFor example\: 50px, 20%, 0.4em. If no unit is specified, px is assumed.                                                               | String          |
| Wrap column headers:     | Allow column headers to wrap                                                                                                                                                                                          | Boolean         |
| Show pop-ups:            | Show pop-up menus and views over the table when no height is specified. For example, show a Date Time Picker view over the table. If this option is not selected, the Date Time Picker is embedded in the table cell. | Boolean         |
| Style header and footer: | Apply a different header and footer style. Modern, for example, streamlines pagination in the header and footer. {Default | Modern}                                                                                   | TableHFStyle    |

| Selection mode:         | How many rows a user can select. {None | Single | Multiple}                                                                                                            | TableSelectionMode   |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| Allow rows to expand:   | Allow rows to expand to display additional information.                                                                                                                | Boolean              |
| Render expanded row as: | Choose how the content is rendered. For Custom, add HTML code to provide content for the row. The default rendering type is Coach View. {Coach View | Custom}          | TableRowRenderType   |
| Show Delete button:     | Show or hide the button to delete a row.                                                                                                                               | Boolean              |
| Show footer:            | Show or hide the footer. The footer is also displayed if any of footer views are enabled such as Show add button.                                                      | Boolean              |
| Show Add button:        | Show or hide the button to add a row. If the table is sorting or filtering, the newly added row might not be displayed properly until sorting or filtering is cleared. | Boolean              |
| Show table stats:       | Enables the display of table stats in the footer. For example, Showing 1 to 5 of 59 entries                                                                            | Boolean              |
| Show pager:             | Show or hide the number of pages. The number is displayed in the footer.                                                                                               | Boolean              |
| Show page sizer:        | Show or hide the page sizer which displays the number of rows on a page.                                                                                               | Boolean              |
| Initial page size:      | The number of rows displayed on a page.                                                                                                                                | Integer              |
| Resize columns:         | Allows the user to resize columns by dragging the column separators.                                                                                                   | Boolean              |
| ANY type:               | Specification of the business object definition type when the view is bound to an ANY type list. {Complex | Simple}                                                    | TableANYType         |

| Async loading:    | Provides a better UI experience for large data sets (at the expense of slower overall row-loading time once the section starts loading).                | Boolean   |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| Async batch size: | The number of rows that loaded synchronously in an asynchronous batch. This can help tune or optimize synchronous vs. asynchronous loading performance. | Integer   |

| Name     | Type     | Default   | Description                                                                                                     |
|----------|----------|-----------|-----------------------------------------------------------------------------------------------------------------|
| name     | {string} |           | CSS class name(s) to add to the control. Separate class names by a space if more than one class.                |
| replaced | {string} |           | CSS class name(s) to be replaced by the first argument. Separate class names by a space if more than one class. |

| Name   | Type     | Default   | Description             |
|--------|----------|-----------|-------------------------|
| obj    | {object} |           | The element to be added |

| ${Table}.appendElement({});  //to create a new empty row                   |
|----------------------------------------------------------------------------|
| ${Table}.appendElement({"str1":"strVal", "int1": 3});  //new row with data |

| Name   | Type       | Default   | Description                    |
|--------|------------|-----------|--------------------------------|
| objs   | {object[]} |           | The element/record to be added |

| Name            | Type      | Default   | Description                                                                                                                                                                                                                                                                                                                   |
|-----------------|-----------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| col             | {any}     |           | When the type is "number" this is the column to be searched or null for all columns.  When type is "string" this is the property name in the table to be searched. When the type is "function" this is the comparator function to use for the search.  Note that when the type is function, the other parameters are ignored. |
| exp             | {string}  |           | regular expression or string to use for the search depending on useRegex                                                                                                                                                                                                                                                      |
| caseInsensitive | {boolean} |           | whether the search should be case insensitive                                                                                                                                                                                                                                                                                 |
| useRegex        | {boolean} |           | whether or not to use the regular expression set                                                                                                                                                                                                                                                                              |

| Name   | Type      | Default   | Description                                                                                              |
|--------|-----------|-----------|----------------------------------------------------------------------------------------------------------|
| index  | {integer} |           | (Optional) Index of page - if null, uses the current page                                                |
| actual | {boolean} |           | If true, gets the actual page size (i.e. number of rows on the page) instead of the configured page size |

| Name      | Type      | Default   | Description                                                                                                                                                                                                                                                                               |
|-----------|-----------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| index     | {integer} |           | 0-based index/position of record                                                                                                                                                                                                                                                          |
| asInTable | {boolean} |           | If true, returns record as sorted and/or filtered in the table, if false or omitted returns the record unfiltered and according to the original order. Record indices with "asInTable" take sorting and filtering into account but are independent of whether the table is paging or not. |

| Name      | Type      | Default   | Description                                                                                                                                                                                                                                     |
|-----------|-----------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| asInTable | {boolean} |           | If true, returns count of records filtered by search, if false or omitted returns the unfiltered record count. Record counts ith "asInTable" take sorting and filtering into account but are independent of whether the table is paging or not. |

| Name      | Type      | Default   | Description                                                                                                                                                                                                                                                                                                             |
|-----------|-----------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| record    | {Object}  |           | The record to look for                                                                                                                                                                                                                                                                                                  |
| asInTable | {boolean} |           | If true, returns the index of the record as sorted and/or filtered in the table, if false or omitted returns the index of the record unfiltered and according to the original order. Record indices with "asInTable" take sorting and filtering into account but are independent of whether the table is paging or not. |

| Name    | Type      | Default   | Description                                       |
|---------|-----------|-----------|---------------------------------------------------|
| recIdx  | {integer} |           | The index of the record                           |
| pageIdx | {integer} |           | (Optional) If not specified, assumes current page |

| Name      | Type      | Default   | Description                                                                                                                                                                                                                                                                                 |
|-----------|-----------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| asInTable | {boolean} |           | If true, returns records as sorted and/or filtered in the table, if false or omitted returns the records unfiltered and according to the original order. Record indices with "asInTable" take sorting and filtering into account but are independent of whether the table is paging or not. |

| Name    | Type      | Default   | Description                                       |
|---------|-----------|-----------|---------------------------------------------------|
| pageIdx | {integer} |           | (Optional) If not specified, assumes current page |

| Name   | Type     | Default   | Description                                              |
|--------|----------|-----------|----------------------------------------------------------|
| v      | {object} |           | A view instance in the table (in one of the table cells) |

| Name      | Type      | Default   | Description                                                                                                                                                                                                                                                                                                                                                                                         |
|-----------|-----------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| asInTable | {boolean} |           | If true, returns the index of the selected record based on the current filtering and sort order of the table. If false or omitted returns the index of the selected record regardless of table filtering and based on the natural/original order of the records. Record indices with "asInTable" take sorting and filtering into account but are independent of whether the table is paging or not. |

| Name      | Type      | Default   | Description                                                                                                                                                                                                                                                                                                                                                                                             |
|-----------|-----------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| asInTable | {boolean} |           | If true, returns the indices of the selected records based on the current filtering and sort order of the table. If false or omitted returns the index of the selected records regardless of table filtering and based on the natural/original order of the records. Record indices with "asInTable" take sorting and filtering into account but are independent of whether the table is paging or not. |

| Name      | Type      | Default   | Description                                                                                                                                                                                                                                                                                                                |
|-----------|-----------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| asInTable | {boolean} |           | If true, returns the selected record (if any) from the records not filtered out in the table. If false or omitted returns the selected record (if any) regardless of table filtering. Records returned with "asInTable" take sorting and filtering into account but are independent of whether the table is paging or not. |

| Name      | Type      | Default   | Description                                                                                                                                                                                                                                                                                                              |
|-----------|-----------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| asInTable | {boolean} |           | If true, returns the count of selected records from the records not filtered out in the table. If false or omitted returns the count of selected record regardless of table filtering. Record counts with "asInTable" take sorting and filtering into account but are independent of whether the table is paging or not. |

| Name      | Type      | Default   | Description                                                                                                                                                                                                                                                                                                                            |
|-----------|-----------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| asInTable | {boolean} |           | If true, it returns the selected records, if any, from the set of records that are not filtered out from the table. If false or omitted, it returns the selected records, if any, regardless of the table filtering. Records returned with "asInTable" take sorting and filtering into account, but do not depend on the table paging. |

| Name         | Type      | Default   | Description                                                               |
|--------------|-----------|-----------|---------------------------------------------------------------------------|
| collapseFlag | {boolean} |           | Set to true to collapse the view (equivalent to a view setting of "NONE") |

| Name    | Type        | Default   | Description              |
|---------|-------------|-----------|--------------------------|
| columns | {integer[]} |           | List of columns to hide. |

| Name      | Type             | Default   | Description                                                                                                                                                                                                                                                   |
|-----------|------------------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| record    | {integer|object} |           | the index of the record to be removed, or the record object itself                                                                                                                                                                                            |
| asInTable | {boolean}        |           | (Only used with index) If true, checks the selected status of the record at the sorted and/or filtered index position, if false or omitted checks the selected status of the record at the index according to the original order and regardless of filtering. |

| Name   | Type    | Default   | Description                                    |
|--------|---------|-----------|------------------------------------------------|
| event  | {Event} |           | Value change event (usually an onchange event) |

| Name         | Type      | Default   | Description                                                   |
|--------------|-----------|-----------|---------------------------------------------------------------|
| fetchNewData | {boolean} |           | (Optional) Set true or false whether new data load on refresh |

| Name      | Type             | Default   | Description                                                                                                                                                                                                                                                                                                              |
|-----------|------------------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| record    | {integer|object} |           | the index of the record to be removed, or the record object itself                                                                                                                                                                                                                                                       |
| asInTable | {boolean}        |           | (Only used with index) If true, removes the record at the sorted and/or filtered index position, if false or omitted removes the record at the index according to the original order. Record indices with "asInTable" take sorting and filtering into account but are independent of whether the table is paging or not. |

| Name            | Type      | Default   | Description                                                                                                                                                                                                                                                                                                                   |
|-----------------|-----------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| col             | {any}     |           | When the type is "number" this is the column to be searched or null for all columns.  When type is "string" this is the property name in the table to be searched. When the type is "function" this is the comparator function to use for the search.  Note that when the type is function, the other parameters are ignored. |
| exp             | {string}  |           | regular expression or string to use for the search depending on useRegex                                                                                                                                                                                                                                                      |
| caseInsensitive | {boolean} |           | whether the search should be case insensitive                                                                                                                                                                                                                                                                                 |
| useRegex        | {boolean} |           | whether or not to use the regular expression set                                                                                                                                                                                                                                                                              |

| Name      | Type      | Default   | Description                                                                                                                                                                            |
|-----------|-----------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| selected  | {boolean} |           | Flag to indicate whether to select or unselect the records                                                                                                                             |
| asInTable | {boolean} |           | (Only used with index) If true, sets the selected status of the records that are not filtered out, if false or omitted sets the selected status of all records regardless of filtering |

| Name   | Type     | Default   | Description                                                                                                                                                                              |
|--------|----------|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| style  | {string} |           | "DEFAULT"|"DEF"|"D"=Default | "LIGHT"|"L"=Light | PRIMARY"|"P"=Primary | "INFO"|INF"|"I"=Info | "SUCCESS"|"S"=Success | "WARNING"|"WARN"|"W"=Warning | "ERROR"|"ERR"|"DANGER"|"G"=Danger |

| Name   | Type      | Default   | Description                              |
|--------|-----------|-----------|------------------------------------------|
| index  | {integer} |           | Index of the column to change the label. |
| label  | {string}  |           | The new label.                           |

| Name        | Type     | Default   | Description                        |
|-------------|----------|-----------|------------------------------------|
| columnSpecs | {object} |           | The specifications for the columns |

| Name            | Type      | Default   | Description           |
|-----------------|-----------|-----------|-----------------------|
| defaultPageSize | {integer} |           | the default page size |

| Name     | Type      | Default   | Description                                                                   |
|----------|-----------|-----------|-------------------------------------------------------------------------------|
| enabled  | {boolean} |           | Enabled/read-only flag (true to enable view, false to disable/make read-only) |
| required | {boolean} |           | Enable/disable required field flag for control                                |

| Name   | Type                    | Default   | Description                                  |
|--------|-------------------------|-----------|----------------------------------------------|
| style  | {string Modern|Default} |           | Style option for the header and footer style |

| Name           | Type        | Default   | Description                                                                              |
|----------------|-------------|-----------|------------------------------------------------------------------------------------------|
| boolList       | {boolean[]} |           | List of booleans that corresponds to the table columns                                   |
| collapseHeader | {boolean}   |           | Set to true to collapse the thead element. Applies only when all the columns are hidden. |

| Name     | Type     | Default   | Description               |
|----------|----------|-----------|---------------------------|
| helptext | {string} |           | Help text for the control |

| Name      | Type      | Default   | Description                                |
|-----------|-----------|-----------|--------------------------------------------|
| highlight | {boolean} |           | Set to true to enable selection highlights |

| Name    | Type      | Default   | Description                                                    |
|---------|-----------|-----------|----------------------------------------------------------------|
| visible | {boolean} |           | Label visibility flag (true to show view label, false to hide) |

| Name   | Type      | Default   | Description    |
|--------|-----------|-----------|----------------|
| idx    | {integer} |           | the page index |

| Name   | Type      | Default   | Description   |
|--------|-----------|-----------|---------------|
| size   | {integer} |           | the page size |

| Name    | Type      | Default   | Description           |
|---------|-----------|-----------|-----------------------|
| minSize | {integer} |           | the minimum page size |
| maxSize | {integer} |           | the maximum page size |

| Name   | Type   | Default   | Description        |
|--------|--------|-----------|--------------------|
| data   | {any}  |           | set the query data |

| Name      | Type             | Default   | Description                                                                                                                                                                                                                 |
|-----------|------------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| record    | {integer|object} |           | the index of the record to be removed, or the record object itself                                                                                                                                                          |
| selected  | {boolean}        |           | Indicates whether to select or clear the record                                                                                                                                                                             |
| asInTable | {boolean}        |           | If true, it sets the selected record status at the sorted and/or filtered index position. If false or omitted, it sets the selected record status at the index according to the original order and regardless of filtering. |

| Name   | Type      | Default   | Description                                                                                                            |
|--------|-----------|-----------|------------------------------------------------------------------------------------------------------------------------|
| col    | {string}  |           | the column name                                                                                                        |
| asc    | {boolean} | false     | ascending order                                                                                                        |
| use    | {boolean} |           | sort value that was specified at cell render time using cell.setSortValue() instead of simply using the displayed text |

| Name   | Type     | Default   | Description                                                                                                |
|--------|----------|-----------|------------------------------------------------------------------------------------------------------------|
| style  | {string} |           | "D"=Default | "E"=Elegant | "B"=table-bordered | "S"=table-striped | "H"=table-hover | "C"=table-condensed |

| Name   | Type     | Default   | Description   |
|--------|----------|-----------|---------------|
|        | {string} |           | title         |

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

| Name   | Type     | Default   | Description    |
|--------|----------|-----------|----------------|
| width  | {string} |           | sets the width |

| Name    | Type        | Default   | Description              |
|---------|-------------|-----------|--------------------------|
| columns | {integer[]} |           | List of columns to show. |

| Name   | Type      | Default   | Description                  |
|--------|-----------|-----------|------------------------------|
| show   | {boolean} |           | Value to show/hide the pager |

| Name   | Type      | Default   | Description                                                                                                            |
|--------|-----------|-----------|------------------------------------------------------------------------------------------------------------------------|
| col    | {string}  |           | the column name                                                                                                        |
| asc    | {boolean} |           | ascending order, default is false                                                                                      |
| use    | {boolean} |           | sort value that was specified at cell render time using cell.setSortValue() instead of simply using the displayed text |

| Name   | Type   | Default                | Description                   |
|--------|--------|------------------------|-------------------------------|
| phase  | {int}  | bpmext.ui.PHASE\_NORMAL | The phase we are currently in |