<!-- image -->

# Migrating a custom mediation primitive

## Before you begin

## About this task

Custom mediation primitives
created in prior versions will work in IBM Integration
Designer 6.0.2,
however the only change that you can make to the primitive's properties
is to edit the Java or Visual
snippet.

- Convert your custom Java code
to an embedded snippet.
- In the mediation flow editor, identify the service reference used
by the old custom mediation primitive. If the service reference is
no longer used in the mediation flow, delete it.
- In the assembly editor, remove the reference from the mediation
flow component, if necessary, and delete the Java component.

## Procedure

1. Select the custom mediation primitive on the canvas to
view its properties. In the properties view, click the Details tab.
The implementation is set to Java or
Visual, and the custom code appears as a snippet in the embedded editor.
2. Click the Convert to Embedded Snippet button
to convert the Java or Visual
code to an embedded Java or
Visual snippet. Save the changes.
3. After conversion to a Java or
Visual snippet, all the classes in the snippet need to be fully qualified.
If you see errors in the Java snippet
code indicating that an object cannot be resolved or is not a type,
use code assist (ctrl-space) to add the package qualifier.
4. In the top section of the mediation flow editor, delete
the service reference used by the old custom mediation primitive,
if the reference is no longer used in the mediation flow. Save your
changes.
5. If you deleted the service reference in the mediation flow,
you need to synchronize the references in mediation flow component.
In the assembly editor, select the mediation flow component, right-click,
and select Synchronize Interfaces and References > from
Implementation.
6. Delete the Java component,
and save the changes in the assembly editor.