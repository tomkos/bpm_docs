<!-- image -->

# Notifying an event handler of an escalation

## About this task

To configure an event and
add it to your business application model, follow these instructions.

## Procedure

1 Implement an event handler according to the steps below.You can package the implementation class of the com.ibm.task.spi.NotificationEventHandlerPlugininto the same application as your human task, or you can put it intoa dependent utility project. This section describes how you add thenotification event handler implementation class to the same applicationas the human task. Here is an example of an implementation of the escalationNotificationmethod.public void escalationNotification(Task task, Escalation escalation) { System.out.println("--- Notification event received: " + DateFormat.getDateTimeInstance().format( new Date(System.currentTimeMillis())));; if(task != null) { System.out.println("Task template name: " + task.getTaskTemplateName()); System.out.println("Task name: " + task.getName()); System.out.println("Event handler name: " + task.getEventHandlerName()); System.out.println("Is escalated: " + task.isEscalated()); } else { System.out.println("Task is null"); } System.out.println("Notification event received."); if(escalation != null) { System.out.println("Escalation name: " + escalation.getName()); System.out.println("Escalate within: " + escalation.getDurationUntilEscalated()); System.out.println("Repeat notification every: " + escalation.getDurationUntilRepeated()); } else { System.out.println("Escalation is null"); } System.out.println("--- End notification event");
    1. In the Java™ perspective,
right-click your Java module,
and select New > Class.
    2. In the New Java Class wizard, choose
a Package and a Name for your new Class and click Add beside
the Interfaces field.
    3. In the Implemented Interfaces Selection window, begin
typing notif until a list of matching types appear,
choose NotificationEventHandlerPlugin, and
click Finish.

```
public void escalationNotification(Task task, Escalation escalation) {

  System.out.println("--- Notification event received: " + DateFormat.getDateTimeInstance().format( new   Date(System.currentTimeMillis())));;

  if(task != null)
  {
    System.out.println("Task template name: " + task.getTaskTemplateName());
    System.out.println("Task name: " + task.getName());
    System.out.println("Event handler name: " + task.getEventHandlerName());
    System.out.println("Is escalated: " + task.isEscalated());
  }
  else
  {
    System.out.println("Task is null");
  }

  System.out.println("Notification event received.");

  if(escalation != null)
  {
    System.out.println("Escalation name: " + escalation.getName());
    System.out.println("Escalate within: " + escalation.getDurationUntilEscalated());
    System.out.println("Repeat notification every: " + escalation.getDurationUntilRepeated());
  }
  else
  {
    System.out.println("Escalation is null");
  }
  System.out.println("--- End notification event");
```

2 Create a service provider configuration file for the plug-in. This configuration file provides the mechanism for identifyingand loading the plug-in, and conforms to the Java 2 service provider interface specification.

1. In the META-INF/services/ directory of your JAR file,
create a file with the name com.ibm.task.spi.plug-in\_nameNotificationEventHandlerPlugin,
where plug-in\_name is the name of the plug-in. For example, if your
plug-in is called HelpDeskRequest (event handler
name) and it implements the com.ibm.task.spi.NotificationEventHandlerPlugin interface,
the name of the configuration file is com.ibm.task.spi.HelpDeskRequestNotificationEventHandlerPlugin.
2. In the first line of the file that is neither a comment
line nor a blank line, specify the fully qualified name of your plug-in
class. For example, if your plug-in class is called MyEventHandler,
and it is in the com.customer.plugins package, then
the first line of the configuration file must contain the following
entry: com.customer.plugins.MyEventHandler.
3 Declare a notification event handler for your task as describedhere:

1. In the human task editor click the Details tab.
2. In the Event handler name field,
enter a name for your notification event handler. Note: This
name is not the name of the implementation class, it is the name that
you gave the event handler.
3. Click Save.
4 Add your plug-in to your application:

1. Switch to the Resource perspective.
2. In the Navigator, expand your business integration project.
3. In the META-INF folder, create a new folder services.
4. Right-click the services folder and select New > File .
5. In the File name field of the New
File wizard, enter com.ibm.task.spi.EventHandlerNameNotificationEventHandlerPlugin
Where EventHandlerName is the event handler
name you have specified for your task.
6. Click Finish. The editor opens
for the new file. In the editor, add a line with the fully qualified
class name of your implementation class: bpc.samples.plugin.EscalationNotificationPlugin.
7. Click Save.
5 Specify an escalation with a notification type Event :

1. Switch to the Business Integration perspective and open
your task in the human task editor.
2. In the Escalation settings section, select the escalation.
3. Click the Details tab.
4. Configure the escalation as needed (for help, see the
Related tasks section below). For Notification type,
choose Event from the list of available options.
5. Save your work.

## Example

## Related tasks

- Creating an escalation for your human task
- Selecting a calendar type for your escalation
- Setting duration values for your human task
- Defining timer-driven behavior in a BPEL process
- Using business calendars within human tasks

## Related reference

- Details tab: business state machine editor
- Duration tab: Human Task editor