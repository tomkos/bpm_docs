# Style

- To specify styles at the page level.
- If you have more than one entry, to switch between themes by using the setTheme (String
theme) method to change styles at run time.

## Configuration properties

- Select among the existing files or add your own files of cascading stylesheets.
- Select a CSS type. The available options are Web and
External.
- Optionally, you can provide an acronym for the application or toolkit that contains the CSS
file. By default, the CSS file is in the current application or toolkit. No acronym is necessary for
the External CSS type.
- Select a theme name.

## How to add CSS files

1. In the navigation sidebar, click the plus (+) sign next to
Files and select Web File.
2. Browse to the .css file that you want.After you close the file chooser,
the selected file is appended to the Web File list.

## Example

```
body {
    background: white;
}
.CSS1a div {
    background: rgb(51, 102, 153);
    border-radius: 10px;
    padding: 15px 20px 15px 20px
}
```

## Methods

For more information about the available methods, see the Style JavaScript API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.

For more information about input views, see Plain text, Text area, Date/time picker, Integer.