# Icon

The Icon view is similar to the Badge view. It is most commonly used for the following
purposes:

- Adding cosmetic character to a UI page
- Serving as a clickable button

## Data binding

## Configuration properties

Under Configuration,
set or modify the appearance and behavior properties for the view.

<!-- image -->

| Appearance configuration property   | Description                                                                                                                                                                                                                              | Data type      |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|
| Color style                         | Specifies a color style for the view. The colors correspond to variables in the specified theme. The default color style is Default (gray).                                                                                              | IconColorStyle |
| Icon size                           | Specifies the size of the icon in either pixel or em units. For example, 43px or 43em. If only a number is specified without any unit, the number is interpreted as the number of pixels. The default value is 43.                       | String         |
| Outline only                        | Specifies whether the view displays only its color-based style when you hover a cursor over it. By default, this property is not selected.                                                                                               | Boolean        |
| Icon                                | Specifies the name of an acceptable icon from the Font Awesome V4.7.0 web site. For example, calendar, clock-o, and camera. (The Font Awesome prefix fa- is optional.) By default, no icon is specified, but you must specify one.       | String         |
| Border radius                       | Specifies the radius of the curvature for an icon. You can make an icon perfectly round by setting it to at least half of the width specified for the Width property. By default, no border radius is specified.                         | String         |
| Width                               | Specifies the width of an icon in pixels, percent, or em units. For example: 50px or 20% or 0.4em. If only a number is specified without any unit, the number is interpreted as the number of pixels. By default, no width is specified. | String         |

| Behavior configuration property   | Description                                                                                                                        | Data type   |
|-----------------------------------|------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Prevent multiple clicks           | Prevents a user from clicking an icon more than once when the icon is used as a button. By default, this property is not selected. | Boolean     |

## Example

In this example, the following appearance configuration properties are set for the Icon view:

- Color style is set to Danger.
- Icon size is set to 43.
- Icon is set to gear.

These properties and their values result in a gear icon that looks like the following figure:

However, if the icon is nested inside of a section that has been set to "read only", such as a
horizontal layout, vertical layout, or view, the icon becomes slightly dimmer. For example:

The dimmer icon can be a problem if other icon views outside of the read-only section are set to
the same color. To ensure that the color of the icon does not change when it is nested inside a
read-only section, you can set the On load event handler to use the
setEnabled method. For
example:

```
me.setEnabled(true)
```

## Events

- On load: Activated when the page loads. For
example:me.setIcon("gears")
- On click: Activated when the link is clicked, before
leaving the page. If the evaluated expression returns false, the click does not
fire the boundary event. For example: return ${Text1}.isValid();
- On boundary event: Activated when there is a boundary event. This event
handler works best with boundary events that end with a Stay on Page event,
because the logic in this event fires when returning to the page. The On boundary
event event handler is useful in those situations when the logic must occur after
the server-side logic that the boundary event triggers. For
example:alert("Stay on Page status '" + status + "'")

## Methods

For detailed information on the available methods for Icon, see the Icon JavaScript API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.