<!-- image -->

# Stepping into component elements in the integration debugger

## Before you begin

The elements that you can step into for each kind of business
integration component are listed in the following table:

| Business integration component   |  Elements that can be stepped into           |
|----------------------------------|----------------------------------------------|
| Business processes               | Java™ snippets, visual snippets              |
| State machines                   | None                                         |
| Business object data maps        | Submaps, Java snippets,                      |
| Business rules                   | Rule set templates                           |
| Visual snippets                  | Custom visual snippets, Java visual snippets |
| Mediation flows                  | Subflows                                     |

## About this task

To step into component elements:

## Procedure

1. In the Debug view, ensure that the correct stack frame
is selected.
2. In the component editor, ensure that the component thread
is paused at a position immediately before the element that you want
to step into. For example, if you want to step into a Java snippet in the business process editor,
you must ensure that the Java snippet
activity has an entry breakpoint on it and that the component thread
is paused before the breakpoint.
3. In the Debug view, click the Step Into icon . The element that you are stepping into
opens and the component thread pauses at the first location where
a breakpoint exists or can be set. For example, if you step into a Java snippet, the component thread pauses at
the first line of code that contains a breakpoint or where you could
set a breakpoint.