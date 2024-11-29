<!-- image -->

# XML Map: Using user-defined variables

1. In the XML map editor, click the Add a global variable icon in the
toolbar.
2. In the Add Variable window, enter a unique string for the name and an
XPath expression as the value that you want to assign to the variable.
3. Choose to keep the dynamically populated return type, or override the return type to provide
your own. If you provide your own return type, select only the simple type because the complex type
is not supported. For more information, see Properties of variables.
4. The variables that you created will be shown in the Variables container object on the input side
of the editor.
5. When you select a variable in the editor, a General properties page will appear in the
Properties view showing information about the selected variable.
6. You can use variables in transforms just like regular source data structures.

## Properties of variables

| Property                               | Description                                                                                                                                                                                                                                                                                                                                       |
|----------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Name                                   | The name of the variable.  The name must be unique from all other variable names in the map.                                                                                                                                                                                                                                                      |
| Value                                  | An XPath expression that you want to assign to the variable.  Enter Ctrl+space in this field to enable content-assist so that you can create an XPath expression based on the input data structures. Click Edit to use the XPath expression builder.                                                                                              |
| Return Type                            | The schema type that the XPath expression will return. This field is dynamically populated based on the evaluation of your XPath expression.  You cannot edit this field.  If the XPath expression cannot be properly evaluated for any reason (or if the evaluation is incorrect), you can override the return type with a value of your choice. |
| Override with user-defined return type | Allows you to override the Return Type field and select a return type of your choice.  Use this field if the return type dynamically calculated in the Return Type field is either unknown or incorrect.  You can specify the return type that you know your XPath expression will return.                                                        |
| Built-in Simple Type                   | This option is enabled only if the Override with user-defined return type option is selected.  This option allows you to select any built-in Schema simple type that you know your XPath expression will return.                                                                                                                                  |
| Element from input radio button        | This option is enabled only if the Override with user-defined return type option is selected.  This option allows you to select any input element that is available in any input data structure.  You can reference Schema global element declarations, along with local elements that may also have anonymous complex types.                     |
| Is an array                            | This option is enabled only if the Override with user-defined return type option is selected.  Select this option to specify that the return type of your XPath expression is repeatable.                                                                                                                                                         |