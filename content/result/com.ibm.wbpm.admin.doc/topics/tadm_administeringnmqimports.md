<!-- image -->

# Viewing and updating WebSphere MQ bindings

## Before you begin

You must have permission to make and save changes to the profile on the administrative console.

The queue and queue manager are not automatically generated and must be created in WebSphere MQ by your
WebSphere MQ
administrator.

## About this task

## Procedure

1. Open the default messaging provider settings page in the administrative console.

Expand JMS Providers and click WebSphere MQ.
2. Optional: 
Administer WebSphere MQ connection factories.

Click WebSphere MQ connection factory in the list of additional
properties. This page shows a list of WebSphere MQ connection factories with a summary of their
configuration properties. Click the MQ connection factory that you want to administer, or click
New to create a new connection factory.
Use the subsequent page to browse or change the configuration properties of the selected
connection factory for use with WebSphere MQ as a JMS provider. These configuration properties control
how connections are created to associated queues. 
You set these properties in the bindings for the resource reference of the application. If you do
not want to modify the bindings for an existing application, locate this connection factory in the
JCA pages where you can find these properties.
3. Optional: 
Administer WebSphere MQ queue connection factories.

Click WebSphere MQ queue connection factories in the list of
additional properties. This page shows a list of WebSphere MQ queue connection
factories with a summary of their configuration properties. Click the WebSphere MQ queue connection
factory that you want to administer, or click New to create a new queue
connection factory.
Use the subsequent page to browse or change the configuration of the selected queue
connection factory for use with the WebSphere MQ JMS provider. These configuration properties control how
connections are created to associated queues. 
A WebSphere
MQ queue connection factory is used to create JMS connections to queues provided by WebSphere MQ for
point-to-point messaging. Use WebSphere MQ queue connection factory administrative objects to manage
queue connection factories for the WebSphere MQ JMS provider.
4. Optional: 
Administer WebSphere MQ queue destinations.

Click WebSphere MQ queue destinations in the list of additional
properties. This page shows a list of the WebSphere MQ queue destinations with a summary of their
configuration properties. Click the queue destination that you want to administer, or click
New to create a new WebSphere MQ queue destination.
New WebSphere
MQ queue destinations must be configured with the custom properties in the following table.
Table 1. Custom properties for WebSphere MQ queue destinations

Destination Type
Property Name
Property Value
Property Type

Send destination
MDWRITE
YES
java.lang.String

MSGBODY
MQ
java.lang.String

MDMSGCTX
SET\_ALL\_CONTEXT
java.lang.String 

Receive destination
MDREAD 
YES
java.lang.String

MSGBODY
MQ
java.lang.String

MDMSGCTX
SET\_ALL\_CONTEXT
java.lang.String 

Use the subsequent page to browse or change the configuration properties of the selected
queue destination for point-to-point messaging with WebSphere MQ as a messaging provider.
A WebSphere
MQ queue destination is used to configure the properties of a queue. Connections to the queue are
created by the associated queue connection factory for WebSphere MQ as a messaging provider.
5. Select the module
that contains the binding by navigating to Applications > SCA Modules and clicking the
module name.
6 Select the binding by performingthe following steps:
    1. In the Module components section,
expand Imports or Exports.
    2. Expand the import or export,
and then expand Binding.
    3 Click the binding to view informationabout its properties. The general properties of the bindingare displayed: Note: You can also access a resource by typing the JNDI namein the text box. Doing so, however, allows you to enter the name ofa resource that is not yet configured.
        - The Send Resources category contains the
Connection Factory and the Send Destination.
        - The Receive Resources category contains
the Response Connection Factory and the Activation Specification.
        - The Advanced Resources category contains
Callback resources and other available resources.
7 Make any required changes to the resources:

1. Click Browse to open a window with a list of JNDI names; then, select
the required JNDI name.
The selected name will populate the appropriate text field.
2. Click Configure to open the corresponding page referred to by
the JNDI name.

Note: Most resources can be configured at the cluster scope. However, when you select the
Configure option for the activation specification, a page is displayed
that shows all activation specifications for all members of the given cluster; you can then
select one activation specification.
8. Save your changes to the master configuration.

## Results

To ensure
that the changes you made remain with the module across deployments,
use IBM Integration Designer to make the changes in the source code
for the module.