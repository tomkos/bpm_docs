<!-- image -->

# Developing web applications for BPEL processes and human tasks
by using JSF components

## About this task

You can use IBM® Integration
Designer to build your web
application. For applications that include human tasks, you can generate a JSF custom client. For
more information on generating a JSF client, go to the documentation for Integration Designer.

You
can also develop your web client using the JSF components provided
by Business Process Choreographer.

## Procedure

1. Create a dynamic project and change the web Project
Features properties to include the JSF base components.
For more information on creating a web project, go to the documentation for Integration Designer.
2 Add the prerequisite Business Process Choreographer Explorer Java™ archive (JAR files). Addthe following files to the WEB-INF/lib directoryof your project: In IBM Business AutomationWorkflow , all ofthese files are in the following directory:
    - bpcclientcore.jar
    - bfmclientmodel.jar
    - htmclientmodel.jar
    - bpcjsfcomponents.jar
    - On Windows platforms:
install\_root\ProcessChoreographer\client
    - On Linux®and UNIX platforms:
install\_root/ProcessChoreographer/client
3. Add the EJB references that you need to the web application
deployment descriptor, web.xml file.   <ejb-ref id="EjbRef\_1">
    <ejb-ref-name>ejb/BusinessProcessHome</ejb-ref-name>
    <ejb-ref-type>Session</ejb-ref-type>
    <home>com.ibm.bpe.api.BusinessFlowManagerHome</home>
    <remote>com.ibm.bpe.api.BusinessFlowManager</remote>
  </ejb-ref>  
  <ejb-ref id="EjbRef\_2">
    <ejb-ref-name>ejb/HumanTaskManagerEJB</ejb-ref-name>
    <ejb-ref-type>Session</ejb-ref-type>
    <home>com.ibm.task.api.HumanTaskManagerHome</home>
    <remote>com.ibm.task.api.HumanTaskManager</remote>
  </ejb-ref>
  <ejb-local-ref id="EjbLocalRef\_1">
    <ejb-ref-name>ejb/LocalBusinessProcessHome</ejb-ref-name>
    <ejb-ref-type>Session</ejb-ref-type>
    <local-home>com.ibm.bpe.api.LocalBusinessFlowManagerHome</local-home>
    <local>com.ibm.bpe.api.LocalBusinessFlowManager</local>
  </ejb-local-ref>
  <ejb-local-ref id="EjbLocalRef\_2">
    <ejb-ref-name>ejb/LocalHumanTaskManagerEJB</ejb-ref-name>
    <ejb-ref-type>Session</ejb-ref-type>
    <local-home>com.ibm.task.api.LocalHumanTaskManagerHome</local-home>
    <local>com.ibm.task.api.LocalHumanTaskManager</local>
  </ejb-local-ref>
4 Add the Business Process Choreographer Explorer JSF componentsto the JSF application.

1 Add the tag library references that you need for yourapplications to the JavaServer Pages (JSP) files. Typically,you need the JSF and HTML tag libraries, and the tag library requiredby the JSF components.
    - <%@ taglib uri="http://java.sun.com/jsf/core" prefix="f"
%>
    - <%@ taglib uri="http://java.sun.com/jsf/html" prefix="h"
%>
    - <%@ taglib uri="http://com.ibm.bpe.jsf/taglib" 	prefix="bpe"
%>
2. Add an <f:view> tag to the body
of the JSP page, and an <h:form> tag to the <f:view> tag.
3. Add the JSF components to the JSP files. Depending
on your application, add the List component, the Details component,
the CommandBar component, or the Message component
to the JSP files. You can add multiple instances of each component.
4. Configure the managed beans in the JSF configuration
file. By default, the configuration file is the faces-config.xml file.
This file is in the WEB-INF directory of the
web application. 
Depending on the component that you add to
your JSP file, you also need to add the references to the query and
other wrapper objects to the JSF configuration file. To ensure correct
error handling, you also need to define both an error bean and a navigation
target for the error page in the JSF configuration file. Ensure that
you use BPCError for the name of the error bean and error for the name of the navigation target
of the error page.<faces-config>
...
<managed-bean>
  <managed-bean-name>BPCError</managed-bean-name> 
  <managed-bean-class>com.ibm.bpc.clientcore.util.ErrorBeanImpl
  </managed-bean-class> 
  <managed-bean-scope>session</managed-bean-scope>
</managed-bean>

...
<navigation-rule>
...
<navigation-case>
<description>
The general error page. 
</description>
<from-outcome>error</from-outcome>
<to-view-id>/Error.jsp</to-view-id>
</navigation-case> 
...
</navigation-rule>
</faces-config>
In error situations that trigger the error page, the exception
is set on the error bean.
5. Implement the custom code that you need to support the
JSF components.
5. Deploy the application. If you are deploying
the application in a network deployment environment, change the target
resource  Java Naming and Directory Interface
(JNDI) names to values where the Business Flow Manager and Human Task
Manager APIs can be found in your cell. If your process containers
are configured on a cluster named clusterName in
the same cell, the names have the following structure:cell/clusters/clusterName/com/ibm/bpe/api/BusinessFlowManagerHome
cell/clusters/clustername/com/ibm/task/api/HumanTaskManagerHome
Map the EJB references to the JNDI names or manually
add the references to the ibm-web-bnd.xmi file.
The
following table lists the reference bindings and their default mappings.
Table 1. Mapping of the reference bindings to JNDI names

Reference binding
JNDI name
Comments

ejb/BusinessProcessHome
com/ibm/bpe/api/BusinessFlowManagerHome
Remote session bean

ejb/LocalBusinessProcessHome
com/ibm/bpe/api/BusinessFlowManagerHome
Local session bean

ejb/HumanTaskManagerEJB
com/ibm/task/api/HumanTaskManagerHome
Remote session bean

ejb/LocalHumanTaskManagerEJB
com/ibm/task/api/HumanTaskManagerHome
Local session bean

## Results

## What to do next

- Business Process Choreographer Explorer components

The Business Process Choreographer Explorer components are a set of configurable, reusable elements that are based on the JavaServer Faces (JSF) technology. You can embed these elements in web applications. The web applications can then access deployed BPEL process and human task applications.
- Error handling in JSF components

The JavaServer Faces (JSF) components exploit a predefined managed bean, BPCError, for error handling. In error situations that trigger the error page, the exception is set on the error bean.
- Default converters and labels for client model objects

The client model objects implement the corresponding interfaces of the Business Process Choreographer API.
- Adding the List component to a JSF application

Use the Business Process Choreographer Explorer List component to display a list of client model objects, for example, BPEL process instances or task instances.
- Adding the Details component to a JSF application

Use the Business Process Choreographer Explorer Details component to display the properties of tasks, work items, activities, process instances, and process templates.
- Adding the CommandBar component to a JSF application

Use the Business Process Choreographer Explorer CommandBar component to display a bar with buttons. These buttons represent commands that operate on the details view of an object or the selected objects in a list.
- Adding the Message component to a JSF application

Use the Business Process Choreographer Explorer Message component to render data objects and primitive types in a JavaServer Faces (JSF) application.