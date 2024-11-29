# Configuring the IBM Business Automation
Workflow
Box Event Listener

## About this task

You run the IBM Business Automation
Workflow
Box Event Listener as a task. Therefore, the task manager
component must be available in IBM Content
Navigator.

## Procedure

To configure the IBM Business Automation
Workflow
Box Event Listener:

1 If the optional task manager component is not available in IBM ContentNavigator , configure and deploy the component. For more information, see Configuring and deploying the task manager component .Theevent listener requires the task manager URL to the HTTPS protocol:https://server\_host\_name :port\_number /taskManagerWeb/api/v1/tasks/ping .If the task manager service uses the HTTP protocol, the event listener encounters errors.

The
event listener requires the task manager URL to the HTTPS protocol:
https://server\_host\_name:port\_number/taskManagerWeb/api/v1/tasks/ping.
If the task manager service uses the HTTP protocol, the event listener encounters errors.

    1. Log in to IBM Content
Navigator administration tool and click
Settings.
    2. In the Task Manager Configuration section, ensure that the URL in the
Task manager service URL field has the following format:
https://server\_host\_name:port\_number/taskManagerWeb/api/v1/tasks/ping
2. Assign the user who will run the event listener to the task manager administrator role 
For information on assigning the user on the WebSphere® Application
Server, see
Associating users with task manager roles (WebSphere Application
Server).
3 In the Case configuration tool , register the eventlistener to make the plug-in available to a desktop.

1. Run the Register the IBM Business Automation
Workflow
Box Event Listener Plug-in task to register the
event listener.
2. Run the Register Project Area task or Register Target Environment task to make the event
listener plug-in available to the desktop.
This step adds the event listener to the Case Manager administration desktop.
4 To run the event listener from a custom desktop, enable the event listener plug-in in thatdesktop:

1. Log in to IBM Content
Navigator administration tool, click
Desktops, and double-click the desktop to which you want to add the event
listener.
2. In the Plug-ins section on the General tab, select
the IBM Business Automation
Workflow API plug-in check box and
the IBM Business Automation
Workflow
Box Event Listener plug-in check box.
The event listener requires the IBM Business Automation
Workflow API
plug-in.
3. On the Layout tab, select the Asynchronous tasks
check box to add the task manager feature to the custom desktop.