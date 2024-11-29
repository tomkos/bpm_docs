<!-- image -->

# Installing API event handler and notification event handler
plug-ins for human tasks

## About this task

The way in which you install the plug-in depends on whether
the plug-in is to be used by only one Java™ Platform,
Enterprise Edition (Java EE)
application, or several applications.

Complete one of the following
steps to install a plug-in.

## Procedure

- Install a plug-in for use by a single Java EE application. Add your
plug-in JAR file to the application EAR file. In the deployment descriptor
editor in IBM® Integration
Designer,
install the JAR file for your plug-in as a project utility JAR file
for the Java EE application
of the main enterprise JavaBeans (EJB)
module.
- Install a plug-in for use by several Java EE applications.
Put the plug-in JAR file in a WebSphere® Application
Server shared
library and associate the library with the applications that need
access to the plug-in. To make the JAR file available in a network
deployment environment, manually distribute the JAR file on each node
that hosts a server or cluster member on which any of your applications
is deployed. You can use the deployment target scope of your applications,
that is the server or cluster on which the applications are deployed,
or the cell scope. Be aware that the plug-in classes are then visible
throughout the selected deployment scope.

## What to do next