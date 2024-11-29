<!-- image -->

# Creating notification event handlers for Business Process Choreographer

## About this task

To implement notification event handlers, you can implement
the NotificationEventHandlerPlugin interface, or you can extend the
default com.ibm.task.spi.NotificationEventHandler service provider
interface (SPI) implementation class.

Complete the following
steps to create a notification event handler.

## Procedure

1. Write a class that implements the NotificationEventHandlerPlugin
interface or extends the NotificationEventHandler implementation class.
This class can invoke the methods of other classes.If you
use the NotificationEventHandlerPlugin interface, you must implement
all of the interface methods. If you extend the SPI implementation
class, overwrite the methods that you need. 
This class runs
in the context of a Java™ Platform, Enterprise Edition ( Java EE) Enterprise application. Ensure that this class and its helper
classes follow the EJB specification.
 The plug-in is invoked
with the authority of the EscalationUser role. This role is defined
when the human task container is configured.
Note:  If you want to call the HumanTaskManagerService
interface from this class, do not call a method that updates the task
that produced the event. This action might result in inconsistent
task data in the database.
2 Assemble the plug-in class and its helperclasses into a JAR file. You can make the JAR file availablein one of the following ways:
    - As a utility JAR file in the application EAR file.
    - As a shared library that is installed with the application EAR
file.
    - As a shared library that is installed with the TaskContainer application.
In this case, the plug-in is available for all tasks.
3. Assemble the plug-in class and its helper classes into
a JAR file. If the helper classes are used by several Java EE applications, you can package these
classes in a separate JAR file that you register as a shared library.
4 Create a service provider configuration file for the plug-inin the META-INF/services/ directory of your JARfile. The configuration file provides the mechanismfor identifying and loading the plug-in. This file conforms to the Java EE service provider interface specification.

The configuration file provides the mechanism
for identifying and loading the plug-in. This file conforms to the Java EE service provider interface specification.

1. Create a file with the name com.ibm.task.spi.plug-in\_nameNotificationEventHandlerPlugin, where plug-in\_name is the name of the plug-in. For example,
if your plug-in is called HelpDeskRequest (event
handler name) and it implements the com.ibm.task.spi.NotificationEventHandlerPlugin interface, the name of the configuration file is com.ibm.task.spi.HelpDeskRequestNotificationEventHandlerPlugin.
2. In the first line of the file that is neither a comment
line (a line that starts with a number sign (#)) nor a blank line,
specify the fully qualified name of the plug-in class that you created
in step 1. For example, if your plug-in class is called MyEventHandler and it is in the com.customer.plugins package, then the first line of the configuration file must contain
the following entry: com.customer.plugins.MyEventHandler.

## Results

You can implement both
plug-ins using a single class, or two separate classes. In both cases,
you need to create two files in the META-INF/services/ directory
of your JAR file, for example, com.ibm.task.spi.CustomerNotificationEventHandlerPlugin and com.ibm.task.spi.CustomerAPIEventHandlerPlugin.

Package
the plug-in implementation and the helper classes in a single JAR
file.

To make a change to an implementation effective, replace
the JAR file in the shared library and restart the server. If the
plug-in is part of the application EAR file, it is sufficient to reinstall
the updated application.

## What to do next