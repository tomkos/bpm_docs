# Overriding CSS styles for selected controls and fields (deprecated)

## About this task

You can create a CSS override for either the label of a heritage coach control or for the
control itself as described in the following procedure:

## Procedure

1. Open the service that contains the heritage coach that you want to work with and then click the
Coaches tab.
2. In the design area, click to select the heritage coach control that you want to
customize.
3. Click the Customization option in the properties.
4. Click the Add Class button.
5. Under Class Details, type a name in the Class Name text
box. By default, this field includes the name, class .
You need to replace this text with the class name that you want.
6. To override the CSS styles for the label of the heritage coach control, click the
Create label override button.
This creates a . class\_name .twLabel { } CSS class, which is
stored directly within the heritage coach and can be accessed as described in the following
step.
7. In the design area, click the top-level section of the heritage coach (named IBM® Business Automation Workflow Coach by default) and then click the
CSS option in the properties.
8. In the CSS text box, type your CSS override settings. 
For example, the following CSS override changes the color
of the label text to red and the typeface of the label text to bold: . class\_name .twLabel
{ color:red; font-weight:bold; }
9. To override the CSS styles for the heritage coach control itself, go back to the Customization
properties for the selected control and click the Create control override
button.
This creates a . class\_name .twControl { } CSS
class.
10. In the design area, click the top-level section of the heritage coach (named Business Automation Workflow Coach by default) and then click the
CSS option in the properties.
11. In the CSS text box, type your CSS override settings.
For example, the following CSS override changes the typeface
of the text in the control to italic: . class\_name .twControl
{ font-style:italic; }
12. Save the heritage coach and then run the service to test the CSS overrides.