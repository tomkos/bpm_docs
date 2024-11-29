# Calling another service from a client-side human service

## About this task

## Procedure

To call another service or service flow from a
client-side human service:

1. Open the appropriate process application.
2. Click User Interface and open the client-side human service that you
want to work with, or build a client-side human service. See Building a client-side human service.
3. In the Diagram view, use Service  to add an activity to the diagram, and wire it as required.
4 Click the new activity in the client-side human service diagram to open it. In theImplementation properties, click Call a service andspecify the service or service flow you want the activity tocall. Note: If the client-side human service is used as an instance details UI or a task for a process,the Implementation properties provide the following options under Behavior > Work with the process instance variables :
    - Refresh the instance variables: If updates to
the instance variable values are made at run time, you can select this option to update the
client-side human service variables with the latest values in the process instance variables. The
refresh option takes effect for both instance details user interfaces and tasks.
    - Send variable updates to the instance: If your
client-side human service modifies the values of its input variables at run time, you can select
this option to update the process instance variables with the latest values in the client-side human
service. The send option takes effect only for instance details user interfaces.
    - Map input data automatically: If you want the input variables be mapped
automatically in the client-side human service, select this option. Or, to enter the data mapping
yourself, clear the check box and switch to Data Mapping in the
Properties view.
5. Under Data Mapping, set the input and output mapping for the
service-calling activity.

Important:  If the called service uses the system
business object Map for output, the JavaScript representation is an array of objects that contain a
key and value property and not an ES6 Map data type. The following example is a JSON string that
shows the JavaScript
representation:  [{"key":"myKey","value":"myValue"}]There is no JavaScript
API to access the values of the map directly, therefore you might need to iterate over the array to
find the object with the matching "key", and then use the corresponding
"value".
If the map contains only a single entry, the value can be
accessed directly using tw.local.<variableName>[0].value.
6. Click Save or Finish Editing.