# Input and output data mapping in nested client-side human services

## About this task

In a hierarchy of nested client-side human
services, variables are defined in isolation and are not automatically
shared between the parent client-side human services and their nested
services. To pass variables between a parent client-side human service
and its nested services, you must set the data mapping. By setting the
input and output data mapping in the parent service, you can pass variables from the parent to the
child services and vice versa, and determine how variables are passed.

- The set of declared variables in a parent service is not visible to its nested services. Input,
output, and private variables in the parent service are defined in isolation and cannot be accessed
by its nested services.
- When you define an input mapping, you make two variables synonyms, with both variables using the
same value. An input mapping pairs a variable (input, output, or private) in the parent client-side
human service with an input (input or input and output) variable in the nested client-side human
service. Input mappings receive the value when leaving the nested service, regardless of whether the
service completes successfully or not. Output mappings apply only when the nested service completes
successfully.
- The variable that you select in the parent service for mapping must be of the same data type as
the input variable in the nested service. Variable type mismatches are flagged in the Data
Mapping properties.
- Output variables that are also mapped as input variables do not require mapping and are not
shown under Output Mapping.

For more information about nested client-side human services, see Reusing client-side human services.

The following procedure describes how to map both input and output data for an activity or a
step. Depending on the logic of your service, an activity or step may only require input or output
data and not both.

## Procedure

To define input and output mapping in a client-side human service that contains nested
client-side human services:

1. In the diagram view of the parent client-side human service, select the activity for the nested
client-side human service, and switch to Data Mapping.
2. Under Input Mapping, use the picker to select any variable (input,
output, or private) in the parent service that you want to map to a specified input variable in the
nested service.
 The selected parent variable receives the value when it leaves the nested
service.
3. Optional: Alternatively, if you want the data mapping to be done
automatically, click the auto-map icon  to automatically map all the input or output nested variables that
do not have a mapping to variables of the same name and data type in the parent service. Existing
mappings are not replaced.
4. Under Output Mapping, use the picker to select any variable in the
current service that you want to map from the specified output variable in the nested
service. Or you can use the auto-map function . The output mapping
applies when the nested service completes successfully.
5. Click Save or Finish Editing.