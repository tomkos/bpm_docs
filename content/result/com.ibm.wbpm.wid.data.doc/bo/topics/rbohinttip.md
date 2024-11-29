<!-- image -->

# Hints and tips for the Business Object editor

- The Business Object editor supports a set of keyboard equivalentsto mouse commands to facilitate keyboard only creation. These include:
    - Use Ctrl+Enter to
create new fields when the main business object is selected.
    - Use Tab/Shift-Tab to cycle between editable
business object fields.
    - Use +/-  to expand/collapse business objects
in the graph view.
    - Use Ctrl-T to toggle between graph and
table view.
- Find support is now available in the Business Object editor. Openthe Find window by clicking Edit > Find or Ctrl+F .The find function supports:

- Forward/Backward searching
- Case sensitivity
- Whole word searching
- Wrap searching
- Incremental searching
- Scoped searching
- When working with schemas in the Business Object editor, you can
open a business object in the XML Schema editor by right-clicking
on the business object and selecting Show in XML Schema
editor from the menu:
- IBM® IntegrationDesigner providesa validator for XML schemas, which define business objects. This validatoris enabled by default, but you can use the former validator if youchoose. Although the XML schema validator provides better performanceunder most conditions than the standard XML schema validator in Rational® ApplicationDeveloper , youcan change the default setting for this and many other propertiesused for the development of modules and libraries. Properties thatyou set for a module or library override general preferences set inthe Windows Preferenceswindow.

1. In the Business Integration view, select a component or module
and right-click to see the context menu.
2. Select Properties to open the Properties
window for that project.
3. Select Override validation preferences if
you want to change the default setting, and select or clear the appropriate
check box.
- When using the business object API, you must use the name "value"
to actually get the value:BOXX.get("value") This
should be used when an XSD type extends a simple XSD type.