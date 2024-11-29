# Laying out a page or view using the grid layout

## About this task

The grid layout is where you can arrange content using grids, containers, and cells.

A grid is a container that is 12 units wide. The actual width of each unit is variable and
depends on the screen size. Within a grid, you can have containers and cells. A container groups
related cells. Cells are placeholders for content. Containers and cells can be from 1 to 12 units
wide. If the container does not have at least one cell, the designer removes it.

<!-- image -->

If the total width of the cells in a grid is 12, the grid forms a complete row. When you edit a
cell in a complete row, the designer tries to preserve the complete row by automatically resizing
other cells. That is, if you delete a cell, another cell expands to occupy the space. Similarly, if
you add a cell to the left or right of another cell, a cell shrinks to fit the new cell. However,
there is a minimum size of 3 for new or automatically resizing cells. In this case, the designer
moves the end cell to form a new row. When you are editing a grid that has less or more than 12
units, the designer does not automatically resize cells. The limit of 12 units applies regardless of
the number of containers within a grid.

A grid does not have a vertical limit. However, having too many vertically stacked cells results
in a user interface that requires users to do a lot of scrolling.

Under Properties > General, you can set the grid layout properties that are described in the following
table.

| Property             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Horizontal span      | Specifies the number of horizontal units that a selected grid cell or container occupies in a grid. A grid is a maximum of 12 horizontal units wide. You can specify a number from 1 to 12. If you increase or decrease the horizontal span, the width of the selected grid cell or container will increase or decrease on the right side of its current position.                                                                                                                                                      |
| Visibility           | Specifies whether a grid cell or container is displayed or hidden in a grid. This property has the following options: Show: Displays a selected grid cell or container. Hide: Hides a selected grid cell or container, but lists it in the Invisible Items  pop-up window. You can display a hidden grid cell or container again by selecting it in the pop-up list and setting visibility back to Show.                                                                                                                |
| Orientation          | Specifies whether the layout items in a selected grid cell are laid out horizontally or vertically. This property has the following options: Horizontal: Arranges the layout items beside each other in a horizontal line. Vertical: Arranges the layout items on top of each other in a vertical stack.                                                                                                                                                                                                                |
| Horizontal alignment | Controls the horizontal alignment of layout items in a selected grid cell. This property has the following options: Left: Aligns the layout items at the left of the horizontal space. Center: Aligns the layout items at the center of the horizontal space. Right: Aligns the layout items at the right of the horizontal space.  Note: Horizontal alignment is not available for layout items in a selected grid cell unless the orientation is horizontal.                                                          |
| Vertical alignment   | Controls the vertical alignment of content in a selected container or grid cell, such as the grid cells in a container or the layout items in a grid cell. This property has the following options: Top: Aligns the content at the top of the vertical space. Middle: Aligns the content at the middle of the vertical space. Bottom: Aligns the content at the bottom of the vertical space.  Note: Vertical alignment is not available for layout items in a selected grid cell unless the orientation is horizontal. |
| Control ID           | Specifies an alphanumeric identifier that uniquely identifies a selected layout item. This ID can be used to locate items in JavaScript and advanced preview artifacts.                                                                                                                                                                                                                                                                                                                                                 |

To lay out a page or view using the grid layout, use the following instructions.

## Procedure

1. Use the toolbar slider to select Grid.
2 Use the insertion points of the default grid pattern to add more cells or containers to thecanvas.
    - Add a grid above or below existing grids.
    - Add a cell to a grid or container. If there are more than 12 units of cells in the grid, the
new cell wraps to the next line.
    - Delete a cell from a grid. If the grid is a complete row, the cell or container to the right
expands to occupy the space of the deleted cell. The content of the deleted cell is
removed.
    - Change the vertical alignment of the grid cells in a selected container.
    - Change the orientation of a grid cell.
    - If the orientation of a grid cell is horizontal, change the alignment of the layout items ina selected grid cell:
        - Horizontal alignment
        - Vertical alignment
- Resize a cell or container by dragging its right border. The cell or container to the right
correspondingly expands or contracts. However, the minimum that it will automatically contract is 3
units. If the cell or container reaches this minimum, it flows instead to the next row.
- Hide a cell or container by changing its Visibility property. The
layout no longer displays it, but the Invisible Items
 pop-up lists it as an invisible item that you can select.
- Delete a grid or container. The content of the deleted grid or container, including cells
and cell content, is removed.
3. Click Save or Finish Editing.

## Results