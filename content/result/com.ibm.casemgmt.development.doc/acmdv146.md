# Retrieving and persisting external properties

In one scenario, external properties might be located in a database. In another scenario, they
might be from a web service. A third scenario might simply use the data to update the visible status
of a widget.

```
require(["icm/base/Constants", "icm/model/properties/controller/ControllerManager"],
   function(Constants, ControllerManager) {
      /* Get the coordination and editable objects from the event payload. */
      var coordination = payload.coordination;
      var editable = payload.caseEditable;
      /* Use the BEFORELOADWIDGET coordination topic handler to obtain the
           controller binding for the editable and to update the properties. */
      coordination.participate(Constants.CoordTopic.BEFORELOADWIDGET,
         function(context, complete, abort) {
            /* Obtain the controller binding for the editable. */
            var controller = ControllerManager.bind(editable);
            /* Retrieve the external properties and bind them to the controller. */
            var externalProperties = getExternalProperties();
            /* You must provide this function. */
            controller.bind("Ext1", "Ext1", externalProperties); 
            /* You can optionally provide an integration object if a 
               non-standard model is used. */
            /* Call the coordination completion method. */
            complete();
         });
   /* Use the SAVE coordination topic handler to release the controller binding
      for the editable. */
   coordination.participate(Constants.CoordTopic.SAVE, 
         function(context, complete, abort) {
      /* Release the controller binding for the editable. */
      ControllerManager.unbind(editable); 
      /* Will automatically release the external properties binding. */
      /* Save the external properties. */ 
      saveExternalProperties(externalProperties); 
      /* You must provide this function. */
      /* Call the coordination completion method. */
      complete();
   });
});
```