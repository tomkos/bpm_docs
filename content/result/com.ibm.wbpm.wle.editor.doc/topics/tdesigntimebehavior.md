# Configuring the design-time appearance of views

## Basic preview options

### About this task

### Procedure

- Specify an image file to use as an icon for your view.
- If the view has a UI that is a result of HTML or JavaScript code and not other views, specify a layout image to display on the canvas at design
time.
- If you want to bind the view to a managed asset at design time, select Use URL
binding. For example, the image views use this setting so that they display the image
that they are bound to in the canvas.
- If your view supports a label, you can set the position of the label on the canvas byspecifying the Preview Label Position . Typically, you use the center label position for UI elements like buttons.
    1. If you specified a layout image and you set the preview label position to
Center, the layout image stretches to fit the label text. By default, the
entire image is stretched.
    2. If you are using the Process Designer web editor and you
have specified an HTML snippet file or the Helper JS file (or both), any code in these files
that position the label overrides the value specified for Preview Label
Position.

## Advanced options for configuring design-time appearance of views

You have more advanced options for configuring the design-time appearance of your views.
Using HTML and JavaScript code, your views can have a
design-time appearance that more closely resembles the view's runtime appearance, giving interface
developers a more accurate idea of how their views will look to application users. In some cases,
the exact same code that is used for the runtime view can be leveraged in the coach
canvas.

### Procedure

- The simplest way to provide a design-time appearance for views that accurately reflect the runtime appearance is through an HTML snippet. The HTML snippet is uploaded as a managed asset, thenselected in the advanced preview section in the view editor. This file should be an HTML file with asnippet that represents the view.
    1. Create an HTML snippet.
This file should be an HTML file with a snippet that represents the view. For example:
<div>
<button class="DesignLabel"></button>
</div>The HTML snippet has some features that enable content boxes and labels to
be placed appropriately.
Class: DesignLabel
This class is placed on the HTML element that represents the label, if the view supports a
label. The editor places the label string at the inner HTML content of this element. A snippet can
have multiple labels, and the label is applied and updated to all elements.
Class: DesignContentBox
This class is used to indicate where a declared content box should be located in the preview. If
this class is used, then the element must also have the data-designContentBoxID
attribute defined. This attribute should be set to the control ID of the declared content box. If
multiple content boxes are declared, each can be uniquely placed in the HTML preview. If a content
box is declared in the layout of the view, but there is not a div in the HTML template with the
DesignContentBox class and matching data-designContentBoxID, then
the editor will place the content box instance at the end of the view's rendering.

Note: The Design* class names are reserved by the editor. Snippets should not
use classes matching this pattern. Similarly, the data-design* attribute names
should be avoided.

The following is an example HTML snippet: <div>
<h2 class="DesignLabel"></h2>
<div class="DesignContentBox" data-designContentBoxID="ContentBox1">
</div>
    2. Add external files to your process application or toolkit, as described in Adding managed files.
    3. Switch to Overview and, under Advanced Preview, select the file that
contains the HTML snippet.
- If an HTML snippet alone cannot provide the design-time preview experience that you want,
you can also specify a managed file containing a JavaScript handler. 

A JavaScript handler allows for manipulation of the
design time DOM in reaction to model changes. The JavaScript handler can work in conjunction with an HTML snippet or it can handle the entire
preview itself. 
The JavaScript handler consists of a JavaScript file with a mixObject defined. The
mixObject can implement one or more functions which the editor calls during the
editor lifecycle. You can also define additional functions, but the names must be prefixed with
coachViewImpl, for example, coachViewImpl\_calcValue(). If you want
to store additional information on this, then it should be placed in the
this.context.coachViewData object. Both the function naming convention and instance
variable storage location are used to prevent conflicts in future versions of the product.
The following is an example of a simple JavaScript handler that provides a preview label and image for a button
control.var mixObject = {
	createPreview:function(containingDiv, labelText, callback){
		require([ "dojo/dom-construct"], this.lang.hitch(this, function(domConstruct){
			var buttonDiv = domConstruct.create("div");
			domConstruct.place(buttonDiv, containingDiv);
			var button = domConstruct.create("button");
        	
			domConstruct.place(button, buttonDiv);
			this.context.coachViewData.labelTextDom = document.createTextNode(labelText);
			button.appendChild(this.labelTextDom);
			callback();
		}));	
	},
	propertyChanged:function(propertyName, propertyValue){
		if(propertyName=="@label" && this.context.coachViewData.labelTextDom){
			this.context.coachViewData.labelTextDom.data = propertyValue;
		}
	},
};For more information about the design-time preview APIs, see Event handlers for coach view design-time preview.