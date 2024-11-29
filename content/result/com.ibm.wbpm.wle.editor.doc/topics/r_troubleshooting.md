# Troubleshooting user interfaces

For more help troubleshooting coaches, see Enabling tracing for coaches.

## viewScope.context is null message

This message can occur when registered event listeners are not unregistered. For example, you
have a view, and you register event listeners for your view in its load event
handler. The unload event handler releases the resources used by the view. If you
do not unregister the event listeners, they might try to access these resources, which causes the
viewScope.context is null message.

## Views that are bound to re-initialized complex objects might contain old data

Views that are bound to complex objects might not refresh data when the runtime flow returns to a
coach that contains these views. An example of a complex object is a business object.

To make your view aware of changes to a complex object, use one of the following techniques:

- Create a callback to capture changes to the complex object:
    1. In the load event handler of the view, add the following code:
this.context.binding.get("value").bindAll(this.myChange, this);
    2. Define the myChange event handler in the view JavaScript. Add the logic to handle properties changes.
    3. In the change event handler, call bindAll() to rebind to the
properties. This step is necessary because the previous binding subscriptions are lost when the
complex object is replaced.
- Create a flag to indicate that the complex object has changed:

1. Add a variable of a simple type such as Boolean or String to the human service.
2. Bind the variable as a configuration option to the view.
3. Add server-side scripting that updates the variable when the complex object changes. The change
in the configuration option variable invokes the change event handler for the view.
4. Add code to handle the changes in the complex object.

## System toolkit upgrade in migrated process applications

```
Error: Unable to load /rest/bpm/wle/v1/service/1.3402b466-ea01-464c-bc00-317677d58a67 status:404
     Coach framework caught exception when calling Life cycle API load() on view div\_1\_1, Exception: TypeError: this.nlsMsgs is undefined
```

Support for custom context root configuration was added in the latest versions of the product.
Process applications that are
migrated from earlier versions might depend on earlier toolkit snapshots.

To ensure predictable user interfaces and consistent artifact behavior in the migrated process applications, upgrade the
dependencies of the corresponding system toolkits to the latest version.

## A table in a Section view that has a horizontal layout requires width setting

A Table view that is rendered in a horizontally laid out section might occupy the full width of
the page. If the table width is not specified, other views that are included in the same horizontal
layout might be partially rendered off the edge of the screen.

To control the correct rendering of the views, specify width values in the
Positioning properties so that each view occupies its allotted width within
the horizontal layout. For example, if you include two text fields and one table in the horizontal
layout, you can set their widths to 25%, 25%, and 50%, respectively. This ensures that all three
views occupy the widths that are allotted for them.

For more information, see Table.

## Control the width of pop-up windows by using Bootstrap variables

Bootstrap LESS variables are used to control the visual appearance of views. To customize the
visual appearance, you can specify values for Bootstrap variables in your custom theme file. For
example, you can customize the width of validation pop-up windows by setting or modifying the
existing value of the @popover-max-width variable in the custom theme file. Refer
to the Bootstrap specification for a list of customizable properties.

## Use unique control IDs across views inside a content box and views in the content box
container

To ensure that the content of a responsive template view can be reused, you typically place this
content inside a content box. The content box is a placeholder for content that the container view
defines. As you contribute views to the content box, you define their configuration and visibility
properties at the content box level. If the layout of your template contains other views, which you
placed outside of the content box, you define their settings at the container view level.

At run time, when you change the screen size, for example, when you rotate your mobile device,
you might notice that user interface elements might behave unexpectedly. This occurs when you used
the same control ID for a view inside the content box and a view outside of the content box. Using
the same control ID for two view instances causes the settings defined on the contributed content
(inside the content box) to override the settings of the view instance in the layout of the content
box container, or vice versa.

```
dojo.js?build=201707181206:2 TypeError: Cannot read property '0' of undefined
              at Object.\_448.resolveDeviceSpecificOptionValue (dojo.js?build=201707181206:2)
              at Object.engine.initConfig (VM1685
              debugcf?locale=en&attachPt=INSWidgetID&devDbg=true&containerRef=2063.7f0ae305-bbc5-45dd-b19f…:229)
              at Object.\_448.start (dojo.js?build=201707181206:2)    at VM1685
              debugcf?locale=en&attachPt=INSWidgetID&devDbg=true&containerRef=2063.7f0ae305-bbc5-45dd-b19f…:299
              at \_1031 (dojo.js?build=201707181206:2)    at Function.\_102e [as \_onQEmpty]
              (dojo.js?build=201707181206:2)    at \_88f (dojo.js?build=201707181206:2)
              at HTMLDocument.\_891 (dojo.js?build=201707181206:2)
```

To avoid this behavior, make sure that control IDs are unique across the views in the content box
and the views in the content box container. For more information about content boxes, see Content box.

## A Next service item not defined error occurs when you migrate a process
instance with a stay-on-page event to a new snapshot version

When you migrate a process instance that contains an active heritage human service task with a
stay-on-page event to a new snapshot version, a Next service item not defined error might occur. The meaning of
this error is that the instance does not have a valid token path and cannot be routed after the
migration has completed.

Typically, the Next service item not defined error occurs when a new instance
version deletes a destination, which results in migrated instances not having a valid destination.
This situation can also occur when the destination is recreated due to the destination ID being
different. To avoid this issue, use policy files, as described in the Generating an instance migration policy file to manage orphaned tokens topic.

However, the stay-on-page event is a transient concept that implies that it is dynamically linked
to the coach that it will return to. Instance migration does not handle the flow state within a
service, so when a heritage human service task for a migrated instance is stopped between a coach
and its stay-on-page event, the coach is no longer a valid destination after instance migration.
This can occur when a postpone activity is used before a stay-on-page event or when the stay-on-page
event follows a nested service that also displays a coach. The task will need to be reset after
instance migration. It cannot be remedied by using policy files. For information about resetting the
task, see Managing tokens. 
For more
information about the tools that are available in the heritage human service editor palette, see
Tools for heritage human services.