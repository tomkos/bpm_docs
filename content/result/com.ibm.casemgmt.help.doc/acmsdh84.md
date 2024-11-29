# Container width and height

When you first open a view in Properties View Designer, the canvas contains a single layout
container. This container is the root container in which you add other containers and
properties.

Each container is as wide as its parent container if a width and height is not specified. You can
set a custom width.

The default height is determined by the content of the container. You can override the default
height by setting the height to a specific percentage or number of pixels. If you set the container
to a specific height (percentage), you must also set a specific height for the parent container or
containers, including the root container. If the height of the content exceeds the specified height,
a vertical scroll bar is displayed.

- The Tabbed Layout container always fills the full width of the container unless an explicit
height and width are specified.
- All tab panes within the container have the same width regardless of their explicit width
settings.
- The height can be set for the tab container or for the individual tab panes within the
container.
- If the content of a tab pane exceeds the specified width and height of the tab container,
horizontal or vertical scroll bars are displayed.

- The Titled Layout container expands to the height of its content. When the container is
collapsed, the height is reduced to the height of the title bar.
- If an explicit height is specified, the container height is always that height. When the
container is collapsed, the content is hidden but the height is not reduced.

- The default width for each container is an equal percentage of the parent container.
- When you override any column settings, the default settings are discarded and you must specify
the settings for all columns.
- If the total column width exceeds the container width, a horizontal scroll bar is
displayed.

- Labels have the width equal to the longest label in the list.
- The column for the editor gets the remaining width.
- A field width percentage is the percentage of the editor column.
- The field width can be specified for each property. If a width is not specified, a default width
is used.

- You can specify the width of the table. If the combined column width exceeds the container
width, a horizontal scroll bar is displayed.
- You can specify the height of the table. If the height is not specified, the table increases in
height without a limit. If a height is specified, the table height is fixed and a vertical scroll
bar is displayed in the table as necessary.
- You can specify the field width for each property. If a width is not specified, a default width
is selected. Percentage-based field widths are specified as a percentage of the table width.