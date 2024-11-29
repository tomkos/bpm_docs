# The view event handler

## Usage

Use the view function
to perform logic before the view is rendered. For example, you can
show or hide labels depending on the visibility setting.

## Parameters

The view function
does not take any parameters.

By default, if visibility is
not set for the view, it will inherit its parent's visibility. If
you want to have your own view logic in addition to the default logic
of the view() method, you can invoke the super-class
view logic inside your view() function by using the
syntax this.constructor.prototype.view.call(this);

## Sample

```
var labelDiv = this.context.element.querySelector(".outputTextLabel");

if (this.context.options.\_metadata.label == undefined ||
    this.context.options.\_metadata.label.get("value") == "" ||
    (this.context.options.\_metadata.labelVisibility != undefined &&
     this.context.options.\_metadata.labelVisibility.get("value") == "NONE")) {
	// hide the label div
	this.context.setDisplay(false, labelDiv);
} else {
	// show the label div
	this.context.setDisplay(true, labelDiv);
}
```