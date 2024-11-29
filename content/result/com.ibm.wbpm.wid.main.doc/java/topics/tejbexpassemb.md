<!-- image -->

# Creating EJB exports using the assembly editor

You can create an EJB export within an assembly diagram
using IBM® Integration
Designer's
assembly editor.

## About this task

## Procedure

1. Select the Inbound Exports drawer
from the palette of the assembly editor.
2. Drag the Enterprise JavaBeans from
the list of available inbound exports to the canvas of the assembly
editor.
3. The New Enterprise JavaBeans Export
Service window opens. From this window, select an interface from the
drop-down list for the binding to be based on and click Next.
4. From this window, decide whether to create an EJB client
JAR module containing the client interfaces and classes that will
be generated for use in a Java™ platform
application. Click New to create a new module,
or select an existing one from the drop-down list. If you decide not
to create an EJB client JAR module at this time, you can create it
later from the EJB export binding menu (right-click the EJB export
and select Generate EJB Client Interface).
5. Using the check boxes, indicate if the interfaces in the
EJB client JAR module will be remote or local EJB 3.0 interfaces or
remote EJB 2.1 interfaces.
6. Click Finish to create the EJB export.

## What to do next