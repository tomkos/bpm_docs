# Themes

A theme definition is a set of theme variables and their values. For example, a theme definition
can have a background variable and a value of white. A view can
have a dynamic stylesheet that uses the variables from the theme definition. When a number of views
use the same theme definition, you can have a set of views that have a consistent visual appearance.
Additionally, it is easy to make a global visual change to these views by changing the theme
variable values without touching the view definitions. Theme definitions and dynamic stylesheets
support the Less stylesheet language so that you can use its syntax and functions to enhance your
custom views.

<!-- image -->

<!-- image -->

Theme definitions and dynamic stylesheets are combined to automatically generate a set of .CSS
files. When a process application displays a page, it uses these CSS files to style the views that are contained in
the page. Generating the CSS takes some time, so if you are viewing the process application in designer, you might see
the views in the page use default or old theme values until the new CSS is available. At run time,
the CSS is already generated for deployed process applications and a delay does not occur.

When the designer displays a view, it uses the theme of the currently open process application or
toolkit to style views in the layout. This feature means that the same view can look different in
the designer depending on which process application or toolkit you have open. The
Carbon theme in the System Data toolkit is the default theme for newer process application, which
provides the theme definitions for your views. The Carbon theme provides the visual assets (colors,
icons, typefaces, and so on) that align the interactions and the look and feel of your process applications and
views with the guidelines of the IBM Design System. For more information, see Carbon Design
System. For an example, see Example: applying the Carbon theme.

- If you open the toolkit in designer and add the button to a page or view, the layout shows the
button as blue.
- If you open the process application in designer and add the button to a page or view, the layout shows the button as
orange.
- If you run the process application, the browser shows the button as orange.

1. Classes and attributes added in the HTML Attributes page of the view
layout properties.
2. Styling included in the inline CSS of the view behavior. To avoid class name collisions, use
inline CSS to temporarily develop the CSS styles. After you develop the styles, put them into an
included script.
3. CSS in the included scripts of the view behavior.
4. Style definitions set in the dynamic styling of the view behavior.
5. CSS definitions set by the theme of the process application or toolkit.