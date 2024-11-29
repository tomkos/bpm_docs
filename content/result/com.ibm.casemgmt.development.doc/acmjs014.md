# Example: Working with case Management business objects in JavaScript

```
/* Sample script */

require(["icm/base/Constants", "icm/model/properties/controller/ControllerManager"],
function(Constants, ControllerManager) {
   /* Get the coordination and editable objects from the event payload: */
   var solutionPrefix = payload.caseType.getSolution().getPrefix();
   var coordination = payload.coordination;
   var editable = payload.caseEditable;

   /* Use the LOADWIDGET coordination topic handler to obtain the controller binding */
   /* for the editable object and to update the properties: */
   coordination.participate(Constants.CoordTopic.LOADWIDGET, function(context, complete, abort) {
      /* Obtain the controller binding for the editable object: */
      var collectionController = ControllerManager.bind(editable);

      /* Start a batch of changes: */
      collectionController.beginChangeSet();

/* Build the values for the business object members. */
/* Assume all members will contain data for all rows.     */
/* In the view, output two rows like the following rows: */
/* 10, Baker Street, Costa Mesa, Oasis, California, USA*/
/* 20, Ebay Street, Costa Mesa, Lotus, California, USA */
      var propValues = {};
      propValues.SAT\_HouseNumber = ["10","20"];
      propValues.SAT\_StreetName = ["Baker Street","Ebay Street"];
      propValues.SAT\_CityName = ["Costa Mesa","Costa Mesa"];
      propValues.SAT\_PropertyName = ["Oasis","Lotus"];
      propValues.SAT\_StateName = ["California","California"];
      propValues.SAT\_CountryName = ["USA","USA"];

/* Get the property controller of the business object. For instance, SAT\_Residence: */
      var residenceController = collectionController.getPropertyController(solutionPrefix + "\_Residence");

/* Get the members of the business object: */
      var children = residenceController.getAttribute("boChildren").get();

/* Set the individual value arrays to the child controllers: */
/* This helps in displaying the changes on Add Case:  */
        for(var j=0;j < children.length; j++) {
       var childController = collectionController.getPropertyController(children[j]);
var propname = solutionPrefix + "\_" +  childController.getAttribute("name").get();
childController.set("value",propValues[propname]);
        }

      var num\_values = propValues.SAT\_HouseNumber.length;

/* Loop through the values and set them to the business object controller: */
var values = [];
      for(var i=0;i < num\_values; i++) {
          var updateJson = {};
          updateJson.id = null;
          var props = [];
          updateJson.properties = props;
          for(var j=0;j < children.length; j++) {
var prop = {};
var childController = collectionController.getPropertyController(children[j]);
prop.name = solutionPrefix + "\_" +  childController.getAttribute("name").get();
prop.dataType = childController.type;
prop.cardinality = childController.cardinality;
prop.value = propValues[prop.name][i] ;
props.push(prop);
          }
          values.push(updateJson);
      }

      residenceController.set("value", values);

      /* Complete a batch of changes. This tells all subscribed widgets to refresh. */
      collectionController.endChangeSet();

      /* Call the coordination completion method: */
      complete();
   });
  
   /* Use the AFTERLOADWIDGET coordination topic handler to release the controller binding for the  */
   /* editable object: */
   coordination.participate(Constants.CoordTopic.AFTERLOADWIDGET, function(context, complete, abort) {
      /* Release the controller binding for the editable: */
      ControllerManager.unbind(editable);

      /* Call the coordination completion method: */
      complete();
   });
});
```