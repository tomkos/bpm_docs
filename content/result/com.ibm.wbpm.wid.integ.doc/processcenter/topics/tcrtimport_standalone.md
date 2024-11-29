<!-- image -->

# Creating an import to call a process in a stand-alone module

## Before you begin

For imports that start or interact with a process from a Service Component
Architecture (SCA) module, the authenticated user role must have at least deployer and monitor
roles.

## Procedure

To create an import to start or interact with a process from a stand-alone module,
follow these steps:

1. Open the process application or toolkit containing the process in the IBM® Integration
Designer workspace.
2. Click the module where you want to create the import, and
open the Dependency Editor.
3. Add a dependency to the imported process application or
toolkit library.
4. Open the module assembly editor.
5. Drag an Import onto the canvas.
6. Add an interface.  The interfaces in the library
that you added as a dependency are available. Select the interface
that you want.
7. Right click Import > Generate Binding > SCA
binding.
8 In the Binding tab of the Properties view,enter the following properties: For example, if you want to call the process Standard HR Open NewPosition from the Hiring Sample (HSS) process application, snapshotStandard Hiring Sample v8550 (SHSV855) , you would enter:
    1. For Module name, enter a string
that is composed of the process application or toolkit acronym, the
snapshot acronym, and the static string ProcessApp,
separated by dashes (-).  For example, PA1-SS1-ProcessApp for
a named snapshot and PA1-Tip-ProcessApp for the
tip snapshot.  Note: The acronym of a process application,
toolkit or snapshot is in parenthesis beside the name. For example,
the acronym of the process application Hiring Sample (HSS) is HSS
.
    2. For Export name, enter the name of the process that you want to call.
You can view the available processes under the Processes category of the
process application or toolkit.

Restriction: The export name must be URL encoded. For example, replace spaces with plus
signs (+).
    - Module name:
HSS-SHSV855-ProcessApp
    - Export name:
Standard+HR+Open+New+Position