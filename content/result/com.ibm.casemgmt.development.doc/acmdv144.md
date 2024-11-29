# Defining external properties at run time

## About this task

## Procedure

To define and bind an external property at run time:

1. Log on to Case Builder.
2. From the Add Case page or the Case Details page, add a Script Adapter widget to the page.
3 On the Script Adapter widget:
    1. Click the Edit Wiring icon and wire the widget to receive 'Send new case
information' events.
    2. Click the Edit Settings icon and paste the following JavaScript in the
window. This JavaScript defines an external property called PhoneNumber.

require([
 "icm/model/properties/controller/ControllerManager",
 "icm/base/Constants"], function(ControllerManager, Constants) {
    // Get the editable and coordination objects from the event payload.
    var coordination = payload.coordination;
    var editable = payload.caseEditable;
    var model;

    // Participate in the BEFORELOADWIDGET topic to bind the external
    // properties into the controller.
    payload.coordination.participate(Constants.CoordTopic.BEFORELOADWIDGET,
         function(context, complete, abort) {
       model = {
          properties: {
             "PhoneNumber": {
                 id: "PhoneNumber",
                 name: "Phone Number",
                 type: "string",
                 cardinality: "single",
                 value: "949-559-2213"
             }
         }
     };
     var collectionController = ControllerManager.bind(editable);
     collectionController.bind("External", "External", model);
     complete();
 });

 // Participate in the AFTERLOADWIDGET topic to release 
 // the controller binding.
 payload.coordination.participate(Constants.CoordTopic.AFTERLOADWIDGET,
    function(context, complete, abort) {
       ControllerManager.unbind(editable);
       complete();
 });
}); 
Important: All external property-related binding typically should happen in the handler
for the BEFORELOADWIDGET.
4. Save the page, then save and deploy your changes to the solution.
5. Open the solution in Case Client and add a case. Notice that the external property, Phone
Number, appears with the case properties on the page for the new case.