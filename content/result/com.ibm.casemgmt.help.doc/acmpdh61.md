# addDependentObject operation

| Parameter      | Type     | Description                                                                                                                                                                                                                                                 |
|----------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| boPropValue    | String   | The value of the case property to which the dependent object is to be added.Use the getCasePropertyValues operation to obtain the value of the business object property.                                                                                    |
| index          | Integer  | The index at which the dependent object is to be added.                                                                                                                                                                                                     |
| propertyNames  | String[] | The names of the properties in the dependent object that is being added.                                                                                                                                                                                    |
| propertyValues | String[] | The values that are to be assigned to the properties in the dependent object. You must specify a value for every property that is listed in the propertyNames parameter.For a multiple value property, the property value format is {'value1','value2'...}. |

1. Run ICM\_Operations > getCasePropertyValues. You
are trying to get the value of a Business Object property from a Case. For the
customPropertyNames  parameter, pass in the symbolic name of a Business Object
property. For example, {"TEST\_BOProp"} and use {} around the
property, since the parameter expects an array.
A value for the Business Object property in
JSON format is returned.
2 Run ICM\_Operations > addDependentObject .TheaddDependentObject method adds content to an existing Business Object propertyvalue in JSON format. The method only updates a JSON value, it does not update the Business Objectproperty on the Case:
    - boPropValue - This is a JSON format of a Business Object property value.
You have this value from running step 1 after running getCasePropertyValues.
For example, if the name of the return array in step 1 is propValues, then you
would pass in propValue[1], as it is the first element of the results.
    - index - This is the location where you want to add the new Business Object
property value. An index value of 0 would add the new values at the beginning.
    - propertyNames and propertyValues - Business Object property names and
values you are trying to add to the Business Object property. For example, if you have Age and Name
properties for your Business Object, then you need to pass in
{"TEST\_Age","TEST\_Name"} for propertyNames. The
propertyValue would coincide with the names.
    - return\_value - A JSON format of the Business Object property value that
contains the newly added values.
3. Run ICM\_Operations > setCasePropertyValues. Finally,
to set the updated Business Object property on the Case, run
setCasePropertyValues with the returned updated JSON from
addDependentObject as a value. For example,
casePropertyNames, use {"TEST\_BOProp"}, and for
casePropertyValues, you set it to be {returned\_JSON}, which
is the JSON returned from addDependentObject.