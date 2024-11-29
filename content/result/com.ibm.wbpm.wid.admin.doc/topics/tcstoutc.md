<!-- image -->

# Stepping out of component elements in the integration debugger

## Before you begin

The elements that you can step out of for each kind of
business integration component are listed in the following table:

| Business integration component   |  Elements that can be stepped out of         |
|----------------------------------|----------------------------------------------|
| Business processes               | Java™ snippets                               |
| State machines                   | None                                         |
| Business object data maps        | Submaps, Java snippets                       |
| Business rules                   | Rule set templates                           |
| Visual snippets                  | Custom visual snippets, Java visual snippets |
| Mediation flows                  | Subflows                                     |

## About this task

To step out of component elements:

## Procedure

1. In the Debug view, ensure that the correct stack frame
is selected.
2. Click the Step Return icon . The component thread resumes and steps out of the element
that you had stepped into and it pauses at the next available component
element. For example, if you had stepped into a Java snippet
in a business process, the component thread steps out of the Java snippet and pauses at the next available
process activity.