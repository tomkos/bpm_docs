# Example: styling views

This example contains two sets of the same UI views that demonstrate how you can style the same
view to appear different. In the first set, some of the style configurations optimize the views for
a web page. Some of the style configurations made to the second set optimize them for a mobile
device, such as a smartphone.

The style configurations in the example use definitions in the Classic theme. These definitions
control the look of any views that are using the theme. If your views are using a different theme,
they could look different depending on the differences between the two themes.

1 Open Process Designer and create a view, then addthe following UI views to it: The view looks like this:
    - Text
    - Check Box
    - Button
    - Text
    - Switch
    - Button

<!-- image -->

2. Select the first Text view. In its Appearance configuration properties,
set the text size to Small. While the default size of
Medium is fine, the smaller text lets you have more text on screen while
preserving space. When you make the change, the label text shrinks. If you added placeholder text,
the text inside the Text view also shrinks. In addition to changing the text size, the padding
around the view changes as well. You can see the difference between small and medium text by looking
at the two Text views in the layout.
3. Make the same changes to the first button, changing the size of the text to
Small.
4. Select the second Text view. In its configuration properties, expand the Style section and
change the text size to Large. The larger text is easier to read on
smartphones. However, you can use large text in a web page and small text in a smartphone if that is
what your layout design requires.
5. Select the Switch view. In its configuration properties, expand the Style section and change the
text size to Large.
6. The Switch view uses a color to indicate which part is selected. By default, this is the Primary
color, which the Classic theme defines as a dark blue. Change the Switch on color
property to Info to change it to the information color, which the Classic theme
defines as a light blue. In this case, this is only an aesthetic choice. However, you could choose
to color the view based on the purpose of the view as an Info view, Success view, Warning view, or
an Danger view.
7. Select the second Button view. In its configuration properties, expand the Style section and
change the text size to Large and set the theme color type to
Success. In the layout, the view looks like this:

<!-- image -->

<!-- image -->

| Large screen size   | Small screen size   |
|---------------------|---------------------|
|                     |                     |