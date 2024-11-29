# Table layout, Table layout row, and Table layout
cell

- Table layout row views are placed inside a Table layout view.
- Table layout cell views are placed inside Table layout row view.

## Configuration properties

Under Configuration, set or modify the configuration
properties for the view.

<!-- image -->

The appearance configuration properties for Table layout are shown in the following table:

| Appearance configuration property   | Description                                                                                                                                     | Data type   |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Border spacing                      | Specifies the spacing between cells in pixel units.                                                                                             | String      |
| Border collapse                     | Specifies one of the following setting for space between the cells: Separate: adds a space between the cells. Collapse: no space between cells. | String      |

## Example

1. Add a Table layout view.
2. Insert a Table layout row view within the Table layout view.
3. Insert two Table layout cell views within the Table layout row view.
4. Insert one Text view in each Table layout cell view.
5. Optionally, set Border spacing property to 25, and
the Border collapse property to Separate to add space
between the cells.

1. Add a Table layout view.
2. Insert three Table layout row views within the Table layout view.
3. Insert three Table layout cell views within the first Table layout row view that you added in
step 2.
4. Insert one Table layout cell views within the second Table layout row view that you added in
step 2.
5. Insert two Table layout cell views within the third Table layout row view that you added in step
2.
6. In the HTML attributes of the first cell in the first row, add the
attribute rowspan, set it to 3, and insert a Switch view
within the cell.
7. Insert a Button view within the second cell of the first row.
8. Insert a QR code view within the third cell of the first row.
9. In the HTML attributes of the cell of the second row, add the attribute
colspan, set it to 2, and insert a Single select view within
the cell.
10. Insert a Date Picker view within the first cell of the third row.
11. Insert a Text area view within the second cell of the third row.

<!-- image -->

## Methods

For detailed information on the available methods for Table layout, Table layout row, and Table
layout cell, see the Table
layout, the Table layout
row, or the Table
layout cell JavaScript API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.