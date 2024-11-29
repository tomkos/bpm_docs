# Section (deprecated)

When users view a Section instance, they see its label
on a background color by default.

## Restrictions and limitations

## Data binding

If the section is bound to a list, the section
repeats its contents to display each item in the list.

## Theme definitions

The design mode of the theme editor contains a simulation of this view. If you hover over the
simulation, it lists the theme definitions that determine the appearance of the view. For
information on the theme editor, see Creating themes.

## Configuration properties

<!-- image -->

| Configuration property   | Description                                                                                                                                                                                                                                                                                       | Data type   |
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Layout                   | Set whether the section arranges its contents vertically or horizontally.The default value is Vertical.                                                                                                                                                                                           | LayoutTypes |
| Automatic wrap           | Set whether the content in the section wraps when there is not enough horizontal space to contain it. This property applies only when you set the Layout property to Horizontal.                                                                                                                  | Boolean     |
| Collapsible              | Select this option to have the section collapse or expand when users click or tap the section header. The default value is that the section does not collapse (False). If you set this property to True, the label for the section is always visible even if the label visibility is set to Hide. | Boolean     |
| Collapsed                | Set the section to hide its content until the user taps or clicks the section header to expand the section.The default value is expanded (False).                                                                                                                                                 | Boolean     |
| Style > Theme color type | The color of the header defined in the theme for a particular type. In the BPM Theme in the System Data toolkit, the colors are: Dark blue for primary (default) White for alternate Light blue for info Green for success Yellow for warning Red for alert                                       | String      |
| Style > Align            | Set how the section aligns its contents.The default value is Default.                                                                                                                                                                                                                             | AlignTypes  |
| Style > Header text size | Set the size of the text in the section header. For example, to make the text and label more readable on smart phones, you can set this configuration option to Large for the small screen size. The default value is Medium.                                                                     | String      |
| Style > Show border      | Select this option to add a visible border to the section.                                                                                                                                                                                                                                        | Boolean     |