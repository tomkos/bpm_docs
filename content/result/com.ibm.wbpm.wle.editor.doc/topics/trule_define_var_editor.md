# Defining variables in the rule editor (deprecated)

## Before you begin

## About this task

## Procedure

To define a variable, complete these steps:

1. In the definitions part of the rule, press Ctrl+Spacebar,
and double-click to select set from the Content
Assist menu. The content of the Content Assist menu
changes to show the default name for new variables, variable1.
After the definitions are specified, the Content Assist menu changes
to show the closing semicolon.
2. Double-click in the Content Assist menu to insert the placeholder
variable name variable1 in the rule.
3. Type over the placeholder variable name to replace variable1 with
the name of your variable. If your variable is only one
word, quotation marks are not required. If your variable is a phrase
containing more than one word, you must put the phrase between quotation
marks.
4. Press Ctrl+Spacebar, and select
a variable type from the menu. In Business Automation Workflow, every
variable name is associated with a variable type, which determines
what values are legal for the associated variable. For more information,
refer to the related topic "Variable types."
5. After the variable type is specified, the Content Assist
menu changes to show the closing semicolon, or the optional building
blocks from, in, and where. If you
have finished defining the variable, select the closing semicolon.
To define a variable using the optional building blocks, continue
by selecting from, in, or where.
6. The variable definition ends with the closing semicolon.
Once a variable is defined, you can use the variable in
all parts of the business rule.

## Example

## What to do next

You must initialize complex variable structures before
running the Decision service. In Business Automation Workflow, all
complex variables and all lists (arrays) must be initialized before
you use them in a BPD or service. If you do not initialize a complex
variable or list, you may receive runtime errors or notice that the
controls to which the variables are bound do not behave as expected.
For more information, refer to the related topic, "Initializing complex
variables and lists."