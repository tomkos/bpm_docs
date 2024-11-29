# Setting the length of input text fields (deprecated)

## About this task

Setting the maximum length for an Input Text control
does not restrict the number of characters that a user can type into
the text box.

## Procedure

1. Open the service that contains the heritage coach that you want to work with and then click the
Coaches tab.
2. In the design area, click to select the heritage coach control that you want to
customize.
3. Click the Customization option in the properties.
4. Click the Add Class button.
5. Under Class Details, type a name in the Class Name text
box.  By default, this field includes the name, class .
You need to replace this text with the class name that you want.
6. To override the CSS styles for the heritage coach control, click the Create control
override button. 
This creates a . class\_name .twControl { } CSS
class.
7. In the design area, click the top-level section of the heritage coach (named IBM BPM
Coach by default) and then click the CSS option in the properties.
8. In the CSS text box, type the CSS override settings to
specify the maximum input length (in pixels) for the control's input
text box. For example, the following CSS override sets
the length to 110 pixels: . class\_name .twControl {
width:110px; }
9. Save the heritage coach and then run the service to test the CSS overrides.