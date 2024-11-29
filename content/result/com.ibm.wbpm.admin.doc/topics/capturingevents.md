# Capturing Business Automation Workflow events for external
consumption

## About this task

1. Create a target JMS queue to receive events.
2. Configure the DEF to JMS event listener.
3. Provide a custom event collector to read the events from the target JMS.

| Script                        | Purpose                                                                                           |
|-------------------------------|---------------------------------------------------------------------------------------------------|
| SampleConfigureEventsToJMS.py | Defines the queue connection factory, queue, event subscriptions, and authentication alias to use |
| SampleReloadDEF.py            | Causes the DEF to refresh its configuration dynamically                                           |

1. Log in to the WebSphere®
Application Server administrative
console.
2. Click Servers > Clusters > WebSphere application server clusters  > cluster name > Business Process Choreographer > Business Flow Manager.
3. Make sure that Enable Common Event Infrastructure logging is
selected.
4. Click Servers > Clusters > WebSphere application server clusters  > cluster name > Business Process Choreographer > Human Task Manager.
5. Make sure that Enable Common Event Infrastructure logging is
selected.
6. If you made some updates, save the configuration and restart the cluster.

## Procedure

1 To create the required WebSphere resources:
    1. Create a JMS queue connection factory at the cell scope level.
In the Business Automation Workflow administrative console,
click Resources > JMS > Queue connection factories.
    2. Create a JMS queue at the cell scope level.
Click Resources > JMS > Queues.
    3. Define a destination on the Business Automation Workflow
deployment environment bus.
Click Service integration > Buses and click the bus. Click Destinations and add a new queue
destination.
2 Update the SampleConfigureEventsToJMS.py script.

1. Specify the following values:

defListenterId
A string value that uniquely identifies this listener
eventQueueJndiName
A string value that refers to the JNDI name of the queue resource created in WebSphere
eventQueueCFJndiName
A string value that refers to the JNDI name of the queue connection factory resource created in
WebSphere
eventQueueCF\_AuthorizationAlias
A string value that refers to the authorization alias created in WebSphere

Tip: You can create a second copy of this script to define more applications as your
needs change. Create a unique defListenerId value for each application but use
the same queue resource, which means the other three values can stay the same.
2. Specify the subscription array.

Each subscription in the subscriptions array is a single string with a forward-slash (/)
character used as a separator for each of the seven part keys. A comma is used to separate each
subscription. The seven part keys are
Application Name / Version / ComponentType / Component Name / Element Type /
Element Name / NatureFor
a description of each of the parts, see Event point key and filter. 
To listen for every event for all applications, use the wildcard character as shown in the
following example:subscriptions=[
'*/*/*/*/*/*/*'
] The following example
shows how you might register to receive events for the Hiring
Sample:subscriptions=[
'HSS/*/BPD/*/PROCESS/*/*',
'HSS/*/BPD/*/ACTIVITY/*/*',
'HSS/*/BPD/*/GATEWAY/*/*',
'HSS/*/BPD/*/EVENT/*/*'
]
3 Run the script to configure DEF. After you run the sample script, a defconfig.xml file is created inthedmgr\_profile\_home /config/cells/cellName directory.

1. At a command line, go to the bin directory under your deployment manager
profile home directory. Run the SampleConfigureEventsToJMS.py script.

wsadmin –lang jython –f c:\SampleConfigureEventsToJMS.py
2. Run the SampleReloadDEF.py script to cause the DEF to refresh dynamically. 

wsadmin –lang jython –f c:\SampleReloadDEF.py

## What to do next

1. Click Service integration > Buses and click the Business Automation Workflow deployment
environment bus.
2. Click Destinations and find your destination queue. Click
Queue points. Click the Runtime tab. Under
General Properties, you can set the Current message
depth. Under Additional Properties, click
Messages to see the messages.

- Filtering DEF events by using event point key values

Ensure the required Dynamic Event Framework (DEF) events can be emitted by editing the defconfig.xml file to include the event point key values, which you can obtain from the trace.