# Building heritage human services (deprecated)

## Before you begin

You can create and edit heritage human services from the designer.

You
can change a preference setting so that heritage human services always open in the web editor. See
Setting preferences in the desktop Process Designer.

## About this task

A heritage human service consists of a server-based flow
that can include scripts, events, decisions, and coaches. When the
flow reaches a coach, users see the web-based form that is defined
in the coach layout. The form displays process-related data to users
and collects input from those users.

## Procedure

1. Open a process application in Process Designer.
2. Click the plus sign next to User Interface,  select Heritage
Human Service, and complete the wizard.
3. In the heritage human service diagram, add elements and wire them together to create a
flow.
For information about the elements that you can add to the diagram, see Tools for heritage human services.

Restriction: In the desktop Process Designer, you cannot wire out from a coach unless the
coach (or one of its child views) contains at least one element that fires a boundary event. You can
use the Button view to fire a boundary event, or you can create a custom view that fires a boundary
event. For more information, see Button control.
4. In the Variables view, add business process variables to support your
service.

Tip: If you provide HTML code as a default value for a variable, wrap the code using the
other type of quotation mark. For example, if the HTML values use double quotation marks, wrap the
entire code in single quotation marks as shown in the following
example:'<font color="#f08080"><b>Some text!</b></font>'
5. Create the user interfaces used in the service.
 See Building coaches.

Note:  Heritage coaches are deprecated and are not
supported in the Process Designer. Only basic
support is provided to open and edit the XML model of heritage coaches in Process Designer.
6. Optional: 
If necessary, validate the data in the coach.
See Validating coaches in heritage human services.
7. Click Save or Finish Editing.
8 To test the service and user interfaces, click Run Service . Note: The following limitations apply when you run a heritage human service in playbackor debug mode in the Process Designer :
    - The human service starts as a task instead of a stand-alone service. If the playback session
does not complete, you must manually close the task in Process Portal.
    - The first coach step in the human service flow runs twice before the coach user interface
displays. However, the session can complete as expected without any negative impact.
9. Iterate through steps 3 - 7 until the service runs correctly and the user interface is
correct.
10 If you want to expose the heritage human service outside of the business process (for example,in the Process Portal ), set the exposure in theOverview properties of the service. See Exposing heritage human services . If you are building the heritage human service in a toolkit instead of in a process application,to expose the heritage human service in Process Portal , you must also do the following steps:

1. Create a snapshot of the toolkit.
2. Activate the toolkit snapshot. See Activating snapshots for use with IBM Process Portal.
3. Add the toolkit snapshot as a dependency to a process application. See Managing toolkit dependencies.
11. If you do not want to automatically synchronize shared business objects that are inputs to this
service when the business object is changed in other instances, switch to
Overview and clear Automatically sync shared business
objects.

Important: Nested services inherit the synchronization behavior of the starting service.
In addition, if you have a service that runs custom logic and then explicitly saves your shared
business objects, always clear the automatic synchronization option. Otherwise, the shared business
object is automatically saved and the code in your service will not run.

You can also create a heritage human service from a BPD in the desktop Process Designer:

1. Open an existing BPD or create one.
2. In the diagram, drop an activity into a non-system lane and then rename the activity.
Activities dropped into any lane but System have the default client-side human service
implementation. In the remaining steps, you replace the default human service with your own.
3. Right-click the activity and select Activity
Wizard from the list of options.
4. In the Set up an activity page of
the wizard, select Create a heritage human service.
5. If the BPD has variables that are defined, click Next.
In the Parameters page of the wizard, set whether
each business process variable is an input or output of the heritage
human service. For example, if you have business process
variable that is named request and the heritage human
service is to collect data to create that request for the server,
set its Input to false and Output to true.
The heritage human service then provides the data for the subsequent
process activities to act upon.
6 Click Finish . The activity now has an associated heritage human service that includes a simplediagram. The content of the default coach can vary, as follows: The default content is provided for your convenience, and you can use it or replace it.

<!-- image -->

    - If you added one or more business process variables that are primitive types, the coach has an
appropriate view in the layout for each of these variables.
    - If you added one or more business process variables that are complex types and they have an
associated view, the coach has that view for each of these variables.
    - If you added one or more business process variables that are complex types and they do
not have an associated view, the coach has a placeholder message for each of these variables.
When you are building the coach, you replace each placeholder with a view that is appropriate for
the variable and how the coach is using it. For example, if you have a
Customer business object, you could replace the placeholder with a
Customer View that displays customer data in a set of text fields.
    - A button that provides the boundary event that you can use to wire the coach to the end node.

- Tools available for building heritage human services (deprecated)

Use the tools that are available in the heritage human service editor to build heritage human services in the Process Designer. Add objects to compose the structure of your heritage human service.
- Mapping heritage human service artifacts (deprecated)

When you develop heritage human services in the Process Designer, you can take advantage of the direct equivalence between the artifacts in the desktop Process Designer and the artifacts in the Process Designer.
- Validating coaches in heritage human services (deprecated)

To ensure that a coach that you use in your heritage human service passes valid data in the flow, use validation to check the coach data.