# Horizontal Section (deprecated)

As of V8.5.5, coach views that are in a horizontal section no longer have their styling
properties ignored. The implementation of the Horizontal Section control changed to no longer use
table styling.

- Configure the section to wrap by selecting the Automatic
Wrap configuration property. This is the simplest option.
- Configure the section to not show its border.
- Reduce the number of elements in the section.
- Add width settings to the horizontal section using HTML Attributes to override the style that sets the default
width, or specify width values on the Positioning tab in the Properties view.
- Reduce the width of individual elements using HTML
Attributes to override the styles that set their width.
- Create your own horizontal section control.
- If you have added other custom CSS to the horizontal section control,
you might have to adjust the CSS to get the desired behavior.

By default, the horizontal section spaces
out its child views by adding 0.5em to the left padding
of the second and subsequent coach views. (In previous releases, a
border-spacing property served this purpose.) You can use the options
on the Positioning tab in the Properties view
or HTML Attributes to override the default
padding and space out the elements to suit your needs.

## Restrictions and limitations

None

## Data binding

| Binding description                                                                                                       | Data type   |
|---------------------------------------------------------------------------------------------------------------------------|-------------|
| Binding has no affect unless the section is bound to a list, in which case the section repeats for each item in the list. | ANY         |

## Configuration properties

<!-- image -->

| Configuration property   | Description                                                                                                                                                                   | Data type   |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Show Border              | Select this option to add a visible border to the section at run time.                                                                                                        | Boolean     |
| Square Border Corners    | Select this option to make the corners of the visible border square. By default, the corners are rounded.                                                                     | Boolean     |
| Align Right              | Select this option to align the content of the section to the right. By default, the content is aligned to the left.                                                          | Boolean     |
| Collapsible              | Select this option to have the section collapse or expand when users click the header. The default value is not collapsible (False).                                          | Boolean     |
| Initially Closed         | Select this option to have the section collapsed when users first see it. Only the header is visible. The default value is expanded (False).                                  | Boolean     |
| Automatic Wrap           | Select this option to have the section wrap its contents if there is not enough room to show the contents on one line. The default value is to not wrap the contents (False). | Boolean     |