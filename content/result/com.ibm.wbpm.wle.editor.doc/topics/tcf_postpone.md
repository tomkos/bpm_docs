# Enabling work to be postponed and resumed at run time

## About this task

When a
postpone event is reached, the service state is saved for later retrieval and the task is returned
to the inbox where it can be claimed again. Any associated coach is closed. When the task is opened
later, the execution of the service resumes at the node specified by the postpone event. When you
add pre- and post-execution scripts to a postpone event, the event runs the scripts before saving
the execution context and before navigating to the specified URL.

## Procedure

To enable users to postpone work on a task:

1. Open the human service that you want to work with.
2 In the Diagram view, add the postpone node:
    - In a client-side human service, add an intermediate event  to the diagram. The default implementation of the intermediate event is a stay-on-page
event. Select the event and, in its Implementation properties, under
Event Type, select the Postpone Event .Tip: If the postpone option is not available under Event
Type, switch to Overview and check your Use
as setting. The postpone event takes effect when you selected Task (Service
contained in a process). See Defining usage settings for client-side human services.
    - In the Diagram view of a heritage human service, add a
Postpone Task
 activity to the diagram.
3. Wire the postpone node as required.
 In a client-side human service, for example, you can connect the postpone event to the node
where you want the task work to be postponed, and add an outgoing connection from the postpone event
back to the node where you want work to be resumed later.
4. (For client-side human services only) Select a navigation option for the
postpone event, which determines what the user will see after the service is postponed. In the
Implementation properties of the postpone event, under Event
Navigation, select one of the following options:

Table 1. Navigation options available for postpone events

Option
Description

Default (behavior provided by the hosting UI) 
Go to the default page provided by the hosting user interface, such as
Process Portal.

Go to the instance details UI
Go to the instance details user interface for the process instance within
which the client-side human service is running.

Go to a specified URL
Specifies a relative URL to go to when the service is postponed. The URL is
relative to the hosting user interface, such as Process Portal.
Because the URL is specified as a JavaScript expression,
surround any literal values with quotation marks.

Important:  Navigation occurs only if the hosting user interface provides navigation
support.
5. Click Save or Finish Editing.