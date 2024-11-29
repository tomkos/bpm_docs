<!-- image -->

# Stepping over component elements in the integration debugger

## Before you begin

The elements that you can step over for each kind of business
integration component are listed in the following table:

| Business integration component   |  Elements that can be stepped over                                                                         |
|----------------------------------|------------------------------------------------------------------------------------------------------------|
| Business processes               | Activities                                                                                                 |
| State machines                   | States                                                                                                     |
| Business object data maps        | Transformations                                                                                            |
| Business rules                   | Rule sets (rules, templates, conditions, actions) and decision tables (conditions, actions, values, terms) |
| Visual snippets                  | Nodes                                                                                                      |
| Mediation flows                  | Mediation primitives, nodes                                                                                |

## About this task

To step over a component element:

## Procedure

1. In the Debug view, ensure that the correct stack frame
is selected.
2. In the component editor, ensure that the component thread
is paused at a position immediately before the element that you want
to step over.
3. In the Debug view, click the Step Over icon . The component thread resumes and steps over the element
and then pauses at the next element where a breakpoint either exists
or can be added. For example, if the component thread is paused at
an activity in a business process, the component thread steps over
the activity and pauses at the next available activity. (Similarly,
if the component thread is paused at a code execution point inside
a Java™ snippet, the component thread steps over
the code statements and pauses at the next point in the code where
a breakpoint either exists or can be added. When the last line of
execution is reached in the Java snippet,
the component thread exits the Java snippet
and pauses at the next element in the component where a breakpoint
exists or can be added.)