# Working with variables for content objects

## About this task

To access the properties of a case solution, in the Workflow Center,
open the case solution in the designer. In the library for the opened case solution, under
Data, you can see a list of all the data types that have been defined in
Case Builder and brought in to the
designer. The Content Object section of the list includes all the business
objects, case types, and activities. The Property section of the list
includes all the case properties that have been "mirrored" in the designer.

To understand how the content objects for case types, activities, and business objects can be
used in the designer, say you want to leverage some of the exposed content objects in a process that
implements a case type activity. By default, processes created in Case Builder include a reference to the
corresponding content objects. In the Variables view of the process, under
Content Objects, you can see the content objects that you can work with. In
the Definition view, the user task for the process is implemented as a
client-side human service, which models the user interface (UI) for the specified case activity
implementation.

If you are creating a new client-side human service for one of the following entities in a
process that implements a case activity, the New Client-Side Human Service wizard enables you to
select content objects as well as variables to use as inputs or outputs for the new client-side
human service:

- User task
- Details UI
- Launch UI

In the Variables view of the client-side human service, all the content
object variables are passed by reference between the process implementing the case type activity and
the service and they are listed as input variables. You can select the properties of each content
object to specify which case data to expose to the client at run time, as described in the procedure
below.

Note that you can also use views to represent the different case properties. When you create a
client-side human service for your case solution UI, you can use the views that have the case
properties.

## Procedure

For security or privacy purposes, to reduce the exposure of customer data at run time,
for example, you might want to filter out some of the case properties that you don't want to expose
to the client through the UI. To specify which case properties to pass to the client-side human
service and expose at run time:

1. Open the client-side human service for the process that implements the case type activity in
the designer.
2. Click Variables to see the input content objects.
3. In the input variable list, select a top-level content object, then click
Configuration
.
4. In the Filter Content Object Properties dialog, select the properties that
you want to use in the service, and then click Save.
 The properties that you did not select will not be passed to the service at run time.
5. Repeat steps 3 and 4 for each input content object.
6 Add content to the default coach in the client-side human service:
    1. In the coach layout, click the appropriate insertion point to display the view palette.
    2. Add case content to the coach directly from a variable: click the
Variable
 category in the palette toolbar to display the list of available content objects, then
click a variable to add it to the coach layout.
    3. For the case properties that you have added to the coach, under Behavior,
the properties are already bound to the correct values, and the labels are bound to the correct
display names.

- Data objects

Specific data objects are used to enable cases and business processes to work closely together in the integrated workflow environment. These data objects include content objects, properties, and choice lists.
- Roles and teams

When a new role is created for a solution in the Roles tab of Case Builder, a corresponding team and group are automatically created for the local application in Process Designer. Also, if a role exists for a solution that was authored in an earlier release, the role is automatically mapped to a team when the solution is promoted to a workflow project. This role-to-team mapping enables the Case Client to display process tasks and case steps in a unified roles in-basket.
- Content object support

When business objects, roles, properties, and choice lists are defined in Case Builder, corresponding content objects, teams, properties, and choice lists are automatically created in Process Designer. However, if content object support is disabled in IBM Business Automation Workflow, these corresponding artifacts will not be automatically created.