# Addressing

The addressing scheme is a hierarchical, tree-like structure whose root is defined as
/ at the topmost position in the displayed page. The structure of the addressing
scheme is similar to that used for a directory. Subsequent nodes in the tree are added as the page
is loaded.

Typically, you would use addressing in the UI views when there are functions that are called by
view events or formulas that are used in some views. Functions can be specified inline, as in a
JavaScript script block of a custom HTML on a page, or in the Inline JavaScript section in the
Behavior properties of the view.

## Addressing styles

Relative and absolute addressing styles are supported. Starting a reference with
/ implies an absolute reference, for example, starting at the root level of the
view tree. Omitting the / at the beginning of the path means "from where I
am". Using .. in a reference causes the reference to go back up a level,
as a file directory tree would behave.

- Fields at the same level as the current one are referenced by using the field name (not using
/ at the beginning of the reference).
- Fields that are one level above can be referenced as
../FieldOneLevelAboveMe.
- Fields that are two levels above are referenced as ../../FieldOneLevelAboveMe,
and so on.
- Relative addressing using ../ can be convenient in some cases.

## JavaScript methods to access views

```
var myTextField = page.ui.get("/Text1");
myTextField.getValue() // returns the value in the text field
myTextField.focus() // would set the focus to the text field.
```

```
bpmEventHelper.ui.getView(ControlId [, thisview])
thisview.ui.get(ControlId)
```

```
var thisview = this; // required

this.validateControls = function(button)
{
    var textControl = bpmEventHelper.ui.getView("Text1", thisview);
    var selectControl =  thisview.ui.get("Select1");
    textControl.getValue(); // returns the value of the SPARK control in 
    this coach view with the ControlId "Text1"
    selectControl.getSelectedItem(); // returns the selected value in the 
    SPARK control in this coach view with the ControlId "Select1"
}
```

```
"/Address/FirstName" or "${Address}.ui.get('FirstName')"
```

- ${FieldName} refers to the view whose control id =
FieldName.
- @{FieldName} refers to the value of the view whose
control id = FieldName.
- ${FieldName).getValue() and
@{FieldName} are equivalent.

## Non-addressable layout views

```
this.constructor.prototype.IS\_ADDRESS\_INVISIBLE = true;
```

The non-addressable views that are used for layout only are: Caption box, Collapsible panel, Deferred section, Horizontal layout, Horizontal split, Input group, Modal section, Panel, Panel footer, Panel header, Pop-up menu, Responsive sensor, Stack, Status box, Table layout,
Tab section, Tooltip, Vertical layout, and Well.

## Addressable custom views

```
bpmEventHelper.ui.loadView(this)
```

```
bpmEventHelper.ui.loadContainer(this)
```

```
bpmEventHelper.ui.unloadView(this)
```

```
bpmEventHelper.ui.unloadContainer(this)
```

## References to peer fields in tables

```
@{Quantity=} * @{Cost=}
```

## Helper functions

You can use the helper functions getParent and getSibling
within the bpmext.ui.View namespace as example. In the example, it is easy to get
to the container view or peer view without knowing the entire hierarchy.

For example, say you have a container view named CV, which includes two
views named Button1 and Button2. Assuming
btn1View is the bpmext.ui.View object for
Button1, you can get to CV by using
btn1View.ui.get(“CV”) or btn1View.ui.getParent();. You can get to
Button2 by using bt1View.ui.getSibling(“Button2”).