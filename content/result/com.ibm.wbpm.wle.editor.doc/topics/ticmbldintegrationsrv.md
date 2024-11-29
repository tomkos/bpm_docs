# Building the IBM Business Automation
Workflow integration
service (deprecated)

## Before you begin

To perform
this task, you must be in the IBM Process
Designer desktop
editor, which is deprecated.

Should you
rename the IBM Business Automation
Workflow solution
in future you will also need to rename the corresponding process application,
and vice-versa.

## About this task

To build an IBM Business Automation
Workflow integration
service, follow these steps:

## Procedure

1. Open the desktop Process Designer (deprecated).
2. Open a process application in the Designer view.
3. Click the plus sign next to Implementation and
select IBM Business Automation
Workflow Integration
Service from the menu to create a service that the business
process could use later. The library section is found in the upper
left area of Process Designer. Enter
a name for the service on the following dialog box and click Finish.
The IBM Business Automation
Workflow Integration
Service editor opens with the Diagram tab
in focus.
4. From the palette, drag an IBM Business Automation
Workflow Integration step
onto the canvas. The initial IBM Business Automation
Workflow Integration step
is named Untitled which you can rename to something
more appropriate.
5. Click Implementation in the Properties view.
Under IBM Business Automation
Workflow Server,
select a case management server from the list of known servers. The
drop-down list of servers is located in the Server field.
These servers are initially defined under Process App Settings (see Adding an IBM Case Manager server (deprecated)). Should there be no entries in the
list that means that no servers have been specified. Click Use
Process Application Settings to add a server and add a
server.
6 Under Case Operation , select theappropriate operation.
    - Create case: This operation lets you create
a new case. A case is an instance of a case type.
    - Search case: This operation retrieves a
set of case references according to a query. See Building a query for a search case operation. The case references are returned
in an array object.
    - Retrieve case: This operation retrieves
a case, that is, a case instance, based on a case reference. It can
be used with a search case operation which provides the case references.
    - Update case: This operation lets you modify
a case. See Processing a search case operation result if you want to
search for cases and then perform multiple updates by iterating through
the array object that is returned.
7. Beneath Case Type, select the type
of case to use. For example, a case type for a case pertaining to
insurance claims might have an Auto Claim case type. Should
your case type change in the future you will need to repeat the previous
steps for the new case type name and regenerate the business objects
which you do in the next step. In other words, changing a case type
name in an IBM Business Automation
Workflow solution
is independent of creating this service.
8. Click Generate Types. This generation
creates the business objects which are used by variables to contain
the data transferred between your service and the case management
server. To see the business objects, click Data.
Note that generating the business objects does not mean that
you have created variables with these business objects as types. You
still need to create those variables to handle the input and output
data for each operation. In the next step on data mapping, you can
create these variables quickly by using an auto-map function.
9. Click Data Mapping. This section
lets you create the map between the variables for input and output.
As stated previously, these variables need to be created. A simple
way to both create and map the input and output variables for an operation
is to use the auto-map function. The auto-map function creates private
variables for the business objects, which are used by the IBM Business Automation
Workflow integration
service. Click the auto-map icon to create these private variables.

The mapping
structure for each operation is discussed in Data mapping in case operations.
10. If you do not want to automatically synchronize shared business objects that are inputs to this
service when the business object is changed in other instances, switch to
Overview and clear Automatically sync shared business
objects.

Important: Nested services inherit the synchronization behavior of the starting service.
In addition, if you have a service that runs custom logic and then explicitly saves your shared
business objects, always clear the automatic synchronization option. Otherwise, the shared business
object is automatically saved and the code in your service will not run.
11. Save your work to update the process application with any
changes to your service.