# Interacting with cases and activities from processes or service flows

- Example of a script that interacts with case and activity property values
- Examples of scripts for updating multiple properties
- Examples of scripts that create a new case and initialize its values
- Example of a script for searching case activities

## Example of a script that interacts with case and activity property values

```
tw.local.caseProperties.Payout.value -= tw.local.activityProperties.Deductible.value;
```

1. Obtain a value of an activity property from the parent activity.
2. Obtain a value for a case property.
3. Calculate a new value of a case property based on the value of the retrieved activity
property.
4. Set a new value for a case property.
5. Set a new value for an activity property of a parent activity.
6. Obtain a value of an activity property from a specified activity.
7. Set a new value for an activity property of a specified activity.

```
// Obtain the deductible amount from a parent activity:
var interestingActivityPropertyNames = new tw.object.listOf.toolkit.TWSYS.String();
interestingActivityPropertyNames[0] = "S1\_Deductible";
var interestingActivityPropertyValues = tw.system.currentProcessInstance.parentCase.getParentActivityPropertyValues(interestingActivityPropertyNames);
var deductible = parseInt(interestingActivityPropertyValues[0]);

// Obtain the payout amount from the parent case:
var interestingCasePropertyNames = new tw.object.listOf.toolkit.TWSYS.String();
interestingCasePropertyNames[0] = "S1\_Payout";
var interestingCasePropertyValues = tw.system.currentProcessInstance.parentCase.getCasePropertyValues(interestingCasePropertyNames);
var payout = parseInt(interestingCasePropertyValues[0]);

// Calculate the updated payout amount:
payout = payout - deductible;

// Set the updated payout amount on the parent case:
var casePropertyValuesToUpdate = new tw.object.listOf.toolkit.TWSYS.String();
casePropertyValuesToUpdate[0]=payout.toString();
tw.system.currentProcessInstance.parentCase.setCasePropertyValues(interestingCasePropertyNames, casePropertyValuesToUpdate);

//Set a new value for an activity property of a parent activity:
var interestingActivityPropertyNames = new tw.object.listOf.toolkit.TWSYS.String();
interestingActivityPropertyNames[0] = "S1\_Deductible"; //The list (String) of property names for which a value is to be set
var ActivityPropertyValuesToUpdate = new tw.object.listOf.toolkit.TWSYS.String(); 
ActivityPropertyValuesToUpdate[0]=payout.toString(); //The list (String) of property values to set
tw.system.currentProcessInstance.parentCase.setParentActivityPropertyValues(interestingActivityPropertyNames, ActivityPropertyValuesToUpdate);

// Obtain the deductible amount of an activity property from a specified activity:
var interestingActivityID = "A01E758B-0000-C4DF-9D9D-B8320585E550" ;// The unique identifier or GUID of the case activity
interestingActivityPropertyNames[0] = "S1\_Deductible"; //The list (String) of property names whose value is to be retrieved 
var interestingActivityPropertyValues = new tw.object.listOf.toolkit.TWSYS.String(); 
interestingActivityPropertyValues = tw.system.currentProcessInstance.parentCase.getActivityPropertyValue(interestingActivityID , interestingActivityPropertyNames); //returns a list of values for a given list of activity property names
var deductible = parseInt(interestingActivityPropertyValues[0]);

//Set a new value for an activity property of a specified activity:
var interestingActivityID = "A01E758B-0000-C4DF-9D9D-B8320585E550"; // The unique identifier or GUID of the case activity
interestingActivityPropertyNames[0] = "S1\_Deductible"; //The list (String) of property names for which a new value is to be set
var interestingActivityPropertyValues = new tw.object.listOf.toolkit.TWSYS.String(); 
interestingActivityPropertyValues[0] = "8.9"; // The list (String) of new property values
tw.system.currentProcessInstance.parentCase.setActivityPropertyValues(interestingActivityID , interestingActivityPropertyNames, interestingActivityPropertyValues);
```

## Examples of scripts for updating multiple properties

The following is an example of string and multi-value string properties that are updated by using
Content objects properties.

```
tw.local.caseProperties.Name.value= "Andrew Smith";
tw.local.caseProperties.Address.value[0]= "Street No 1";
tw.local.caseProperties.Address.value[1]= "Road No 2";
```

```
tw.local.caseProperties.Name.value= "Andrew Smith";

var casePropertyNames = new tw.object.listOf.String();
var casePropertyValues = new tw.object.listOf.String();
casePropertyNames[0] = "LO\_Address";
casePropertyValues[0] = "{'Street No 1 ','Road No 2'}";
tw.system.currentProcessInstance.parentCase.setCasePropertyValues(casePropertyNames, casePropertyValues, true);
```

## Examples of scripts that create a new case and initialize its values

- A multi-value property.
- A business object that contains a multi-value property and some single-value properties.

```
var propertyNames = new tw.object.listOf.String(); // The list of property names to set during the case creation.
var propertyValues = new tw.object.listOf.String();// The list of property values to set during the case creation.

propertyNames[0] = "S1\_Destination";
propertyValues[0] = "YYZ"; // Single String value
propertyNames[1] = "S1\_DepartureDate";
var depDate= new Date(Date.now() + 24 * 60 * 60 * 1000);
propertyValues[1] = depDate.toISOString().replace(/\.\d+/, ""); // DateTime in the format yyyy-MM-dd'T'HH:mm:ss'Z'

propertyNames[2] = "S1\_Shippers";
propertyValues[2] = "{'ABC Logistic','XYZ Freight'}" // Multiple values

propertyNames[3] = "S1\_Closed";
propertyValues[3] = false.toString(); // Boolean value

propertyNames[4] = "S1\_Packages";
propertyValues[4] = "{\
    \"objects\": [{\
            \"properties\": [{\
                    \"name\": \"S1\_TrackingNumber\",\
                    \"value\": \"T100001\"\
                }, {\
                    \"name\": \"S1\_MinimumTemperature\",\
                    \"value\": \"-40\"\
                }, {\
                    \"name\": \"S1\_ItemDescription\",\
                    \"value\": \"{'Foo','Bar'}\"\
                }, {\
                    \"name\": \"S1\_Value\",\
                    \"value\": \"150,000.00\"\
                }\
            ]\
        }, {\
            \"properties\": [{\
                    \"name\": \"S1\_TrackingNumber\",\
                    \"value\": \"T100002\"\
                }\
            ]\
        }\
    ],\
    \"requiredClass\": \"S1\_Package\"\
}"; // Multiple business object values

tw.system.currentProcessInstance.createCaseUsingSpecifiedCaseType("S1\_Shipment", propertyNames, propertyValues);
```

```
tw.local.newCaseProperties = new tw.object.Record();

tw.local.newCaseProperties.setPropertyValue("S1\_Destination", "YYZ");

var depDate = new tw.object.Date();
depDate.setUTCTime(depDate.getUTCTime() + 24 * 60 * 60); // tomorrow
tw.local.newCaseProperties.setPropertyValue("S1\_DepartureDate", depDate);

var shippers = new tw.object.listOf.String();
shippers[0]="ABC Logistic";
shippers[1]="XYZ Freight";
tw.local.newCaseProperties.setPropertyValue("S1\_Shippers", shippers);

tw.local.newCaseProperties.setPropertyValue("S1\_Closed", false);

var packages = new tw.object.listOf.Record();
packages[0] = new tw.object.Record();
packages[0].setPropertyValue("S1\_TrackingNumber", "T100001");
packages[0].setPropertyValue("S1\_MinimumTemperature", -40);
var descriptions = new tw.object.listOf.String();
descriptions[0]="Foo";
descriptions[1]="Bar";
packages[0].setPropertyValue("S1\_ItemDescription", descriptions);
packages[0].setPropertyValue("S1\_Value", 150000.00);
packages[1] = new tw.object.Record();
packages[1].setPropertyValue("S1\_TrackingNumber", "T100002");
tw.local.newCaseProperties.setPropertyValue("S1\_Packages", packages);

tw.system.currentProcessInstance.createCase("S1\_Shipment", tw.local.newCaseProperties);
```

## Example of a script for searching case activities

```
var returnedActivityIdList = new tw.object.listOf.toolkit.TWSYS.String();
var interestingActivityNames = new tw.object.listOf.toolkit.TWSYS.String(); 
interestingactivityNames[0]= "S1\_ActivityName1"; // A list of symbolic activity names
var propertyFilter = "[TaskState]=4 OR [TaskState]=5 OR [TaskState]=6" ;// The string must conform to the Content Platform Engine SQL syntax, for example: '([prop1] = 1 AND [prop2] &lt;&gt; 3)'
returnedActivityIdList = tw.system.currentProcessInstance.parentCase.searchActivities(interestingActivityNames, propertyFilter); //Returns a list of activity IDs that match the given conditions.
var activityID = parseString(returnedActivityIdList[0]);
//The sample result of variable  activityID will be  "A01E758B-0000-C4DF-9D9D-B8320585E550"
```