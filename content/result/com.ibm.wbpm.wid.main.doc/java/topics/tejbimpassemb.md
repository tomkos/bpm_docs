<!-- image -->

# Creating EJB imports using the assembly editor

You can create an EJB import within an assembly diagram
using the IBM® Integration
Designer assembly
editor.

## About this task

1. Select the Outbound Imports drawer from
the palette of the assembly editor.
2. Drag the enterprise bean from the list of available outbound imports
to the canvas of the assembly editor.
3. The New Enterprise JavaBeans Import
Service window opens and lists all the EJB remote and local interfaces
available in the workspace. From this window, select an EJB remote
or local interface as a reference that the enterprise bean is accessed
through and provide the JNDI name (if it was not automatically discovered).
4. Click Finish to add the EJB import to the
assembly diagram.

1. Drag an EJB session bean object on to the canvas of the assembly
editor.
2. The New Enterprise JavaBeans Import
Service window opens. From this window, indicate the type of interface
for the EJB import (WSDL or Java™)
and select the EJB interface. Note that there might be more than one
EJB interface discovered (for example, EJB 3.0 local interface, EJB
3.0 remote interface, and so on).
3. Click Finish to add the EJB import to the
assembly diagram.

1. Drag an EJB session bean file on to the canvas of the assembly
editor.
2. The New Enterprise JavaBeans Import
Service window opens. From this window, indicate the type of interface
for the EJB import (WSDL or Java)
and select the EJB interface. Note that there might be more than one
EJB interface discovered (for example, EJB 3.0 local interface, EJB
3.0 remote interface, and so on).
3. Click Finish to add the EJB import to the
assembly diagram.

1. Drag a local or remove interface on to the canvas of the assembly
editor.
2. The New Enterprise JavaBeans Import
Service window opens. From this window, indicate the type of interface
for the EJB import (WSDL or Java)
and provide the JNDI name if it cannot be automatically discovered
by the wizard.
3. Click Finish to add the EJB import to the
assembly diagram.

## Results

## What to do next