- Overview
- Package
- Class
- Tree
- Deprecated
- Index
- Help

- Prev Class
- Next Class

- Frames
- No Frames

- All Classes

- Summary:
- Nested |
- Field |
- Constr |
- Method

- Detail:
- Field |
- Constr |
- Method

## Interface Template

- All Superinterfaces:
java.io.Serializable

All Known Subinterfaces:
DecisionTableRuleTemplate, RuleSetRuleTemplate, RuleTemplate, TreeActionValueTemplate, TreeConditionValueTemplate

public interface Template
extends java.io.Serializable
This is the base interface for all templates.  A template defines the basic structure
 of a part of a business rule.  It defines a set of one or more parameters that are used 
 to complete the structure.  An instance of a template can be created by giving specific
 values for each of the template's parameters.  The template instance can then be used as
 part of a ruleset or decision table.  For example, an instance of a rule template can be
 created by giving specific values for the parameters associated with the rule template.
 This template instance can then be used as a rule within a ruleset.  There can be zero 
 or more instances of any given template.
 
 The main purpose of a template is to allow a piece of a ruleset or a decision table
 to be changed dynamically at runtime without having to completely redeploy the
 application.  There are two aspects to this.  First, an existing template instance can
 be changed by updating the parameter values associated with it.  This will cause that
 template instance to be executed with the new values the next time the ruleset or
 decision table is run.  Second, a new template instance can be created dynamically to
 allow new pieces of logic to be added to a ruleset or a decision table.  For example,
 a new template instance rule can be created and added dynamically to a ruleset without
 having to redeploy the entire application.
 
 A template has a list of parameters that define the values that
 can be changed at runtime for this template.  The values for these parameters are 
 specified in the template instances created from the template.  A template also has a
 user presentation string which specifies how the template should be presented to the
 end user.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary

Methods 

Modifier and Type
Method and Description

java.lang.String
getDescription()
Get the description for this template.

java.lang.String
getDisplayName()
Get the display name for this template.

java.lang.String
getId()
Get the system-assigned ID of this template.

java.lang.String
getName()
Get the name of this template.

Parameter
getParameter(java.lang.String parameterName)
Get the parameter with the specified name from this template.

java.util.List<Parameter>
getParameters()
Get the parameters for this template

java.lang.String
getUserPresentation()
Get the user presentation string for this template.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getName
java.lang.String getName()
Get the name of this template.  This is the user-assignable name of the template.
 This value is not guaranteed to be unique.
Returns:The name of this template.
    - getId
java.lang.String getId()
Get the system-assigned ID of this template.  This is guaranteed to be unique.
Returns:The ID of this template.
    - getUserPresentation
java.lang.String getUserPresentation()
Get the user presentation string for this template.  The returned presentation string
 makes use of a convention where template parameters are represented by the index of the
 parameter in the template's parameter list surrounded by curly braces ('{' and '}').  For
 example, consider the following user presentation string: "set output1 to {0} and output2
 to {1}".  "{0}" represents the first parameter in the template's parameter list and "{1}" 
 represents the second parameter in the list.  Note that the API ensures that the order
 of the parameters in the template is the same as the order of the parameter values in
 the construct based on the template, such as a template instance rule.  This means that
 you can always use the parameter index from the presentation string as an index into
 either the list of parameters from the template or the list of parameter values from
 the construct based on the template.
Returns:The user presentation string for this template.
    - getDescription
java.lang.String getDescription()
Get the description for this template.
Returns:The description for this template.  May be null.
    - getDisplayName
java.lang.String getDisplayName()
Get the display name for this template.  The display name may have been
 specified during development of the template to give a name that is more
 understandable to the business user.
Returns:the display name of this template.  May be null.
    - getParameters
java.util.List<Parameter> getParameters()
Get the parameters for this template
Returns:A List of Parameter objects representing the parameters
 for this template.  The returned List is unmodifiable.
    - getParameter
Parameter getParameter(java.lang.String parameterName)
Get the parameter with the specified name from this template.
Parameters:parameterName - The parameter name to search for.
Returns:The parameter in this template with the specified name. null is
         returned if there is no parameter with the specified name in this
         template.
Throws:
java.lang.IllegalArgumentException - If parameterName is null