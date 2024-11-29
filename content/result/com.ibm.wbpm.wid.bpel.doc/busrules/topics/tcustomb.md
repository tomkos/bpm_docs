<!-- image -->

# Customizing algorithms for date and time selection

## About this task

- A date as specified using the tool.
- A date returned from a Java™ expression
- A date stored in an attribute of the incoming business object.

By default, scheduling is based on the Current
date. To change this, proceed as follows:

## Procedure

1. In the rule logic area of the rule group editor, create
a new Scheduled Rule Logic by clicking the  icon.
Date fields will appear with the current date.
2. In the Selection Criteria field,
click Current date. You will then
have the following choices:

Option
Description

Current date
Choose this to use the inline interactive calendar to select
the dates graphically. If you choose this, then the system will create
a Java snippet that will return
a current java.util.date object.

Java
Choose this to use the visual snippet editor to graphically
compose your own Java code that
will obtain a date and a time, and return a java.util.date to the
selector component.

XPath
Choose this to specify an XPath to a xsd:datetime (java.util.date)
parameter. The parameter can either be a stand-alone, or it can be
embedded within a Business Object.

## Related concepts

- Rule group editor
- Using rule set names in a rule group

## Related tasks

- Specifying the rule logic for a rule group
- Scheduling rules using the rule group editor
- Creating custom selectors