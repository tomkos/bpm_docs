<!-- image -->

# Templates and Parameters

The user presentation value provides a string value which can be used for displaying the rule and
different parameters in a easy to use manner. The user presentation, which is a string, has
placeholders to allow for the different parameter values to be replaced and displayed correctly. The
placeholders are in the format {<parameter index>}. For example, if the
presentation string for the init rule is "Base discount is {0} %",
the placeholder {0} could be substituted with the parameter value. The presentation
string cannot be changed for the rule or the template definition. The placeholder values however,
can be modified with the parameter values in a client application per the definition of the
template. The different templates include a convenience method
(getExpandedUserPresentation) that returns a string which has all of the parameter
values correctly placed in the string.

All parameter values have a specific data type, however when retrieving and setting a parameter
value, a string object is used. The parameter value can be treated as string when substituting the
value into the user presentation and also when setting the parameter with a new value. The parameter
is converted to the correct data type at run time in order to correctly issue the rule at execution
time. During validation, the parameter value will be compared to the data type to ensure it is
correct. For example, if a parameter is of type boolean and is set to
"T", validation will not recognize this value and will return a problem.

In the template definition, the parameter values can be restricted by constraints. The
constraints can be defined as a range or an enumeration. The constraints for the parameter will be
enforced when the rule is validated. If a template was not used to define the value definition, only
a user presentation will be available. A value definition cannot have both a template and a user
presentation. Should a template be used, the presentation from the template definition is the only
presentation which is available.

The Template class provides methods that support the following:

- Retrieve the template ID
- Retrieve the name
- Retrieve the parameters
- Retrieve the user presentation

- Retrieve the parameter name
- Retrieve the parameter data type
- Retrieve the constraint for the parameter
- Retrieve the template defining the parameter
- Create a parameter value

- Retrieve the parameter name
- Retrieve the parameter value
- Set the parameter value

Figure 1. Class diagram for Template and Parameter and related classes

<!-- image -->