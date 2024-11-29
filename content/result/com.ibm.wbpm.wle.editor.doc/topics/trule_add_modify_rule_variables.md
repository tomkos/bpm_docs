# Adding and modifying Decision service variables 
(deprecated)

## Before you begin

To perform
this task, you must be in the IBM Process
Designer desktop
editor, which is deprecated.

## About this task

## Procedure

To add or modify variables for a Decision service, complete
the following steps:

1. Open the desktop Process Designer (deprecated).
2. Open a process application that contains a business process
definition (BPD) in the Designer view.
3. Make sure you have selected the Decision service where
you want to add or modify variables.
4. Click the Variables tab.
5. Existing variables are organized into three sections: Input,
Output, and Private, as shown in the following example. Click
the plus sign next to a section to see the variables in that section.
6 You can add a variable to the Decision service by completingone of the following steps: The following information applies to variables:
    - Click Add Input to add a variable that
you can use for input into a rule.
    - Click Add Output to add a variable
that you can use for output from the rule.
    - Click Add Private to add a variable
that applied only to the current Decision service.
    - Variables are mapped to the IN, OUT or IN-OUT parameter directions
automatically, depending on how the variable is used in the rule.
For example, a variable that is referenced in a rule but is not updated
at run time is identified as an IN variable. For more information
about parameters, refer to the related topic "Adding variable types
and business objects to a Decision service."
    - The input or output designation for variables might affect the
way the Decision service runs, but the designation is not significant
when you are authoring BAL rules because input, output and private
variables are all referenced identically in a BAL rule.
    - If you create an input and an output variable that have the same
name, only one variable is actually created. The variable is used
for both input and output at the Decision service level.
    - Exposed Process Variables (EPVs) are managed at the process application
level, and allow the IBM Business Automation Workflow administrator
to specify designated users who can set or alter variable values using
the Process Admin Console while instances of a process are running.
The Decision service can pick up an EPV variable that has been created
in a process application and use the variable in a rule to affect
the way that the Decision service runs. For more information about
EPVs, refer to the related topic "Creating exposed process values."
7. You can modify or view the properties of an existing variable.
Click to highlight the variable name, then modify the variable
properties under the Details section, or view
the Default Value of the variable if a default
value has been defined, as shown in the following example:
8 Select an existing Variable Type ,or define a new variable type.

1. Click Select to set or modify
the current variable type.
2. Click New to define a new variable
type. For more information about defining a new variable
type using the Business Object editor, refer to the related topic
"Adding variable types and business objects to a Decision service."

## What to do next

- Default rule variables and parameters (deprecated)

 Traditional: 
Pre-defined variables and variable types are deployed from the System Data toolkit when IBM Business Automation Workflow is installed.
- Adding variable types and business objects to a Decision service (deprecated)

 Traditional: 
In IBM Business Automation Workflow, you can create a custom business object (variable type) for the Decision service. The variable type becomes part of the data for the process application, and is available for all business process definitions (BPDs) and services included in the process application.
- Variable types (deprecated)

 Traditional: 
You can define a Decision service variable by first specifying the name of the variable, then setting the variable type. The variable value can be a simple data type such as a string, integer, or date. You can also define a complex variable type using a business object that contains parameters.