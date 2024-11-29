# Vertical layout

Vertical layout and Horizontal layout are among the views that are
most commonly used to design a user interface. Used in conjunction, the Horizontal layout and
Vertical layout views provide the majority of the flow layout capabilities, which you can use to
design complex user interfaces.

## Configuration properties

<!-- image -->

| Appearance configuration property   | Description                                                                                                                                                                                                                                                                     | Data type   |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Layout flow                         | The layout of the views: Horizontal Horizontal Inline Scroll Horizontal Tight Horizontal Auto-Wrap Vertical Vertical Tight                                                                                                                                                      | String      |
| Horizontal alignment                | The horizontal alignment of the views in the layout:  Justified Left Center Right  Note: Justified does not work well in combination with the Horizontal Inline Scroll and the Horizontal Auto-Wrap layout flow. If you use this combination, you might see unexpected results. | String      |
| Vertical alignment                  | The vertical alignment of the views in the layout. This property applies only to horizontal layout flows. Top Middle Bottom                                                                                                                                                     | String      |
| Width                               | Specifies the width of the view. You can specify the width in px (pixels), % (percent), or em units. For example, 50px, 20%, or 0.4em. If no unit type is specified, then px is assumed.                                                                                        | String      |
| Height                              | Specifies the height of the view in px (pixels) or em units. If no unit type is specified, then px is assumed.                                                                                                                                                                  | String      |

| Responsive configuration property   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Data type            |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| Responsive sensor                   | (Optional) The identifier of the responsive sensor view that contains this layout. If omitted, the nearest sensor in the parent container is used.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Boolean              |
| Behavior                            | Specifies how the section must behave based on the box factors that are defined in the responsive sensor. Box factor name: The name of the responsive sensor box factor to which these attributes apply. Child layout: The layout you can use with the specified box factor.  Vertical Vertical Tight Horizontal Horizontal Inline Scroll Horizontal Tight Horizontal Auto-Wrap   Child alignment: The alignment you can use with the specified box factor:  Justified Left Center Right   Child width: Widths of child views that you can use with this box factor. For example, 60%.Note that you can specify more widths for the views that are included in the layout. For example, 80%, 20%.   Visibility: The visibility settings you can use with the specified box factor. Visible None Hidden   Width: The section width you can use with the specified box factor. Height: The section height you can use with the specified box factor. CSS style: The CSS styles you can apply to the specified box factor. CSS class: The CSS classes you can add to the specified box factor. | ResponsiveBehavior[] |

| Performance configuration property   | Description                                                                                                                                                                                                                              | Data type   |
|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Async loading                        | Improves the UI experience for large data sets at the expense of a slower overall row-loading time once the section starts loading. This property is used only when the section is bound to a list.                                      | Boolean     |
| Async batch size                     | Specifies the number of rows that are loaded synchronously in an asynchronous batch. Use this property to optimize the synchronous and asynchronous loading performance. This property is used only when the section is bound to a list. | Integer     |

## Example

In the designer, add a Vertical layout view to your page layout, which you will use as a
container view. Inside the container, place three Panel views, which you can name Work
Categories, Claim Type, and Elements. Set
the configuration properties for each view as follows.

- For Vertical layout: Under Appearance, set
Layout flow to Vertical, Horizontal
alignment to Justified, and Vertical
alignment to Top. Leave Width and
Height blank.
- For Work Categories: Under Appearance, set
Color style to Warning, and
Width to 350px.
- For Claim Type: Under Appearance, set
Color style to Success, and
Width to 350px.
- For Elements: Under Appearance, set
Color style to Danger, and
Width to 350px.

At run time, the result shows three panels of the same height and width, stacked one on top of
the other within the vertical section: Work Categories is yellow for
Warning, Claim Type is green for
Success, and Elements is red for
Danger.

## Events

- On load: Activated when the page loads. For example:
me.setWidth("100%");
- On responsive update: Activated when the section is resized according to
the screen size of a device.

## Methods

For the methods that are available for Vertical layout, see the Vertical layout JavaScript
API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.