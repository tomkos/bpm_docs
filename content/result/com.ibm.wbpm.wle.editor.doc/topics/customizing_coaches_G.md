# Enhancing interface layout using custom attributes (deprecated)

## About this task

You can add a custom attribute to enable users to expand and collapse a section in a
heritage coach as described in the following procedure:

## Procedure

1. Open the service that contains the heritage coach that you want to work with and then click the
Coaches tab.
2. In the design area, click to select the heritage coach section that you want to
customize.

Note: This example requires a heritage coach section with a visible title that is nested within
another section.
3. Click the Customization option in the properties.
4. Click the Add Attribute button.
5. Type showHide in the Name text box. 
By default, this field includes the name, key .
You need to replace this text with the key name that you want.
6. To make the section collapsible, type true in
the Value text box. By default, this field includes the
text, value . You need to replace this text with
the value that you want. Note: To make the section collapsible and
collapsed by default, type hidden in the Value text
box.
7. Save the heritage coach and then run the service to test the custom attribute.

## What to do next

The custom attributes that you add when building a heritage coach pass information to the
XSL about how the page should be rendered. When you switch to the heritage coach XML view, you can
see any name-value attributes in the XML. IBM® Business Automation Workflow provides the following attributes that you
can use just as the showHide attribute is used in the preceding steps:

| Attribute   | Description                                                                                                                                                                                  | Applies to                 | Example value       |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------|---------------------|
| cssStyle    | Overrides a CSS style                                                                                                                                                                        | Input Text (or equivalent) | width: 100px        |
| cssClass    | Overrides a CSS class (be sure to include the standard CSS class if you want the default functionality as well)                                                                              | Input Text (or equivalent) | inputText important |
| height      | Enables scrollable tables and sections (the table or section will always be the given height, even when there is not enough data to fill it. The header of the table scrolls with the data.) | Table or Section           | 200px               |
| width       | Sets the width of a table column                                                                                                                                                             | Cell                       | 75%                 |
| precision   | Displays numbers with the specified number of digits after the decimal                                                                                                                       | InputText or Output Text   | 2                   |
| symbolPre   | Displays the given symbol before a value                                                                                                                                                     | InputText                  | $                   |
| symbolPost  | Displays the given symbol after a value                                                                                                                                                      | InputText                  | %                   |
| position    | Specifies the location of a label, such as on top (the label must be visible)                                                                                                                | Label                      | top                 |

You can create completely new attributes and extend the capabilities of the Coach Designer
by adding XML attributes directly to a heritage coach's XML. When you add attributes to a heritage
coach's XML, you need to customize the heritage coach XSL to support the new attribute.