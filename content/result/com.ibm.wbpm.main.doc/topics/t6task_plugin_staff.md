<!-- image -->

# Using a plug-in to post-process people query results

## About this task

To modify the results that are returned by people assignment
and people substitution, you must write a class that implements the
plug-in interface, assemble a JAR file for the plug-in, then install
and activate it.Draft comment: 
7.0.0.2: This topic was rewritten/restructured
for US20600 - the StaffQueryResultPostProcessorPlugin2 interface. The conceptual information was moved to People query result post-processing plug-in.

Complete the
following steps to create a plug-in to post-process people query results.

## Procedure

1. Implement your people query result post-processing plug-in.
Write a class that implements either the StaffQueryResultPostProcessorPlugin interface or the StaffQueryResultPostProcessorPlugin2 interface.
2 Create an installable JAR file. You have an installable JAR file that contains a plug-inthat post-processes people query results and a service provider configurationfile that can be used to load the plug-in.
    1. Assemble your plug-in class and its helper classes into
a JAR file.
    2 Create a service provider configuration file for theplug-in in the META-INF/services/ directory ofyour JAR file. The configuration file provides the mechanism for identifyingand loading the plug-in. This file must conform to the Java™ EE service provider interface specification.
        1. In a text editor, create a service provider configuration file
with the name com.ibm.task.spi.plug-in\_nameStaffQueryResultPostProcessorPlugin, where plug-in\_name is the name of the plug-in. The name
of the configuration file does not depend on the name of the interface
that you implemented. For example, if your plug-in is called MyHandler and it implements the com.ibm.task.spi.StaffQueryResultPostProcessorPlugin2 interface, the name of the configuration file is com.ibm.task.spi.MyHandlerStaffQueryResultPostProcessorPlugin.
        2. In the first line of the file that is neither a comment line (a
line that starts with a number sign (#)) nor a blank line, specify
the fully qualified name of the plug-in class that you created in
step 1. For example, if your plug-in class is called StaffPostProcessor and it is in the com.customer.plugins package,
then the first line of the configuration file must contain the following
entry: com.customer.plugins.StaffPostProcessor.
3 Install the JAR file in a shared library in the applicationserver and associate it with the Human Task Manager application.

1. Define a WebSphere® Application
Server shared library for the plug-in on the scope of
the server or cluster where Business Process Choreographer is configured.
For more information about using shared
libraries, see the related task link.
2. Associate the shared library with the TaskContainer application.
3. Make the plug-in JAR file available to each affected Workflow Server
that hosts a server or a cluster member.
4 Configure the Human Task Manager to use the plug-in. The plug-in is now available for post processing peoplequery results.

1. In the administrative console, go to the Custom
Properties page of the Human Task Manager.  Click Servers > Clusters > WebSphere application server clusters > cluster\_name,
then on the Configuration tab, in the Business Process Manager section, expand Business Process Choreographer, and click Human Task Manager. Under Additional Properties, select Custom Properties.
2. Add a custom property with the name Staff.PostProcessorPlugin, and a value of the name that you gave to your plug-in, for example, MyHandler.
5. Restart the server to activate the plug-in.  The post processing plug-in is invoked after both the people assignment
and people substitution have run.Note: If you modify the plug-in,
you must replace the JAR file in the shared library, and restart the
server.

- People query result post-processing plug-in

Use the people query result post-processing plug-in service provider interface (SPI) to create a plug-in to change the results of people queries returned. For example, to improve workload balancing, you might have a plug-in that removes users from the query result who already have a high workload.
- Developing a plug-in using the StaffQueryResultPostProcessorPlugin2 interface

The StaffQueryResultPostProcessorPlugin2 interface provides optimized performance for cases where the post-processing will yield the same result for a specific task role or escalation role across all task instances or escalation instances that are based on the same task template.
- Developing a plug-in using the StaffQueryResultPostProcessorPlugin interface

The StaffQueryResultPostProcessorPlugin interface allows you to modify the people query results. This interface does not offer the performance optimizations that are available in the StaffQueryResultPostProcessorPlugin2 interface.