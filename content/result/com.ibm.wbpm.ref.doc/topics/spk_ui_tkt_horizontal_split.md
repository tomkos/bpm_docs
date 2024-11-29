# Horizontal split

## Data binding

## Configuration properties

Under Configuration,
set or modify the appearance and behavior properties for the view.

<!-- image -->

| Appearance configuration property   | Description                                                                                                                   | Data type       |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|-----------------|
| Height                              | The default setting is 100% of its container. The container must have an explicitly set height.                               | String          |
| Pane specs                          | Specifies various appearance variables for each pane, such as the size, collapsedSize, splitterThickness, and handleLocation. | SplitPaneSpec[] |
| Resizable panes                     | Allows the panes to be resized by dragging the edges horizontally.                                                            | Boolean         |

## Events

- On load: Activated when the view loads, for
example:me.collapsePane(me.getPaneCount() - 1)
- On pane collapsed: Activated when a pane collapses, for
example:${PaneStatus}.setText("Last Pane Collapsed: " + paneIndex);
- On pane expanded: Activated when a pane expands, for
example:${PaneStatus}.setText("Last Pane Expanded: " + paneIndex);
- On pane resized: Activated when the pane is
resized, for
example:${PaneStatus}.setText("Last Pane Resized: " + paneIndex + " with " + changedSize + "px");

Depending
on the specific event, you can use JavaScript logic to modify the effects of the
view.

## Methods

For detailed information on the available methods for Horizontal split, see the Horizontal split JavaScript
API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.