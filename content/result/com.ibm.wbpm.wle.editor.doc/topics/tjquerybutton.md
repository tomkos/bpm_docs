# Example: creating a jQuery button control

## About this task

- Adding custom HTML code to a view
- Uploading a managed file with the external library assets
- Configuring the load method
event handler with a custom code

## Procedure

1 Add custom HTML code to a view:
    1. In the Layout page, add the Custom
HTML Advanced item to the canvas.
    2. In the HTML properties,
select the Text option and then provide your
custom HTML code. For this example, you can use
the following code to define a jQuery button:<input type="button" class="Jquerybutton" name="jbtnName" value="default"></input>
2 Upload a compressed (.zip) file that contains the jQuerylibrary assets and style sheets and then select the individual filesto include:

1. From the list of library assets, click the plus sign
next to Files and select Server
File from the list of components.
2. Select your compressed jQuery library assets file (jQuery.zip for
this example) and then click Finish.
3. After the upload is complete, switch to Behavior page of the view and
click the plus sign next to Included Scripts.
4. In the list of server files, click the twistie next
to jQuery.zip to view the
contents of the uploaded file.
5 Select a file to include. Each file to includeis selected individually. The .css files areincluded in a specific order. For this example, the following filesare included in the order that they are listed:
    - jquery-1.4.js
    - jquery-ui-1.8.custom.min.js
    - core.css
    - jquery-ui-1.8.custom.css
3. In the Behavior page, under Event Handlers, select
load and then provide the custom script.
For this example, you can use the following
script:var \_this = this;
$('.Jquerybutton', this.context.element).button(
{label: this.context.options.\_metadata.label.get("value")}).bind('click', function() {
\_this.context.trigger(function() { console.log("jQuery button boundary event handled");})
}); 

Table 1. Notes about the script

Item
Description

this.context.options.\_metadata.label.get("value") 
Retrieves the label value from the configuration options.

this.context.trigger(...) 
Triggers a boundary event when the button is clicked. If the boundary event is
wired to the next step in a Human service diagram, clicking the button triggers a transition (to the
next step).
4. Click Save or Finish Editing.

## Results

The custom button will be available in the palette.