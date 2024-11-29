# Providing information about views

## Procedure

Provide information such as tags, documentation, and icon images for the view in its
Overview properties:

- Add one or more tags to the view.
These tags are used to categorize the view on the palette and within the library. If you do
not specify a tag, you can find your view in the Uncategorized category. For more information
about view categories, see Categorizing views.
- In the Documentation field, provide information about the view that
helps people who reuse your view in their own pages or views.
For example, describe the boundary events that your view fires.
- If you want your view to use named boundary events to move to the next step in the service
flow, select Can Fire Boundary Event.
In a human service diagram, you see these boundary events as
wires. This diagram also shows the control that fires the boundary event.
- If you want your view to be selectable as a template when someone creates a view, select
Use as a Template.

Tip: Add a content box to your view so that views that are based on the template have an
area in which users can drop content.
- If you want pages or views that contain your view to display a label at design time, select
Supports a label.
To have the view access the label value in the runtime environment, switch to
Behavior and add the following code as inline JavaScript:
this.context.options.\_metadata.label.get("value");Also, see Example: showing the label of a complex view for information on how to display the label at run
time.
- If you want to improve performance for the view, select Prototype-level eventhandlers . Selecting this option means that the event handlers for the view are in the prototype and notin every instance. The performance gain comes from having one set of the event handlers per viewdefinition instead of having a set per view instance. However, the JavaScript code that you use to create and access variables differsbetween view instance-level event handlers and prototype-level handlers. For prototype-level eventhandlers, you must use the this keyword. The following table shows the codingdifference for the two levels of event handlers: Instance-level event handlers Prototype-level event handlers You can also look at the views for examples of the coding difference. The deprecated coach views of the Coaches toolkit in version 8.5.0 and higher haveprototype-level event handlers. The deprecated coach views in earlier versions of the Coachestoolkit have instance-level event handlers. Remember: The Coaches toolkit is deprecated. For newcoaches, use the views in the UI toolkit . For information on how thedeprecated coach views map to views in the UI toolkit, see Mapping deprecated functions to UI functions .

| Instance-level event handlers                                                                                                                                   | Prototype-level event handlers                                                                                                                                        |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Define the variable in the inline JavaScript of the view:var myVariable = "123"; Access the variable in the load event handler:if(myvariable == "123") {  ... } | Define the variable in the inline JavaScript of the view:this.myVariable = "123"; Access the variable in the load event handler:if(this.myvariable == "123") {  ... } |

You can also look at the views for examples of the coding difference. The deprecated coach views of the Coaches toolkit in version 8.5.0 and higher have
prototype-level event handlers. The deprecated coach views in earlier versions of the Coaches
toolkit have instance-level event handlers.

- You can specify HTML and JavaScript to create and
enhance the design-time appearance of your view. For information, see Configuring the design-time appearance of views.