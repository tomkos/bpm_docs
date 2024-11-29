# Zoom

| Binding              | Description                                                                               |
|----------------------|-------------------------------------------------------------------------------------------|
| zoomFactor (Decimal) | A number in a specified interval that can be used to set the zoom level on other controls |

| Instance configuration label     | Description                                                                                         | Definition configuration option   | Default value                                               |
|----------------------------------|-----------------------------------------------------------------------------------------------------|-----------------------------------|-------------------------------------------------------------|
| Minimum Value                    | A number that represents the minimum value of the zoom scale                                        | minimumValue (Decimal)            | (empty)When no value is specified, the implied value is 1.  |
| Maximum Value                    | A number that represents the maximum value of the zoom scale                                        | maximumValue (Decimal)            | (empty)When no value is specified, the implied value is 10. |
| Number of Zoom Levels            | The number of incremental steps that occur for the defined zoom interval as a user moves the slider | zoomLevels (Integer)              | (empty)When no value is specified, the implied value is 0.  |
| Zoom only when mouse is released | The zoom level refreshes only when a user releases the mouse after moving the slider                | zoomOnMouseUpOnly (Boolean)       | False (not selected)                                        |

This view does not use the visibility property.