<!-- image -->

# Viewing the service integration bus

## Before you begin

Make sure you understand how the Service Integration Bus
is used. Each deployment environment has its own bus. The single bus
is called BPM.deployment\_environment\_name.Bus.

## About this task

The Service Integration Bus Browser provides a single
location for browsing and performing day-to-day operational tasks
on service integration buses.

Viewing the service integration
bus is a useful way to determine if messages are accumulating on the
destinations.

The accumulation of messages on the SCA Module
destinations is a strong indication that there maybe a performance
problem or an application defect.

It is a good idea to periodically
view the messages and determine if there are any messages have become
locked for an extended duration of time as this may indicate that
there are "indoubt transactions".

## Procedure

1. From the administrative console, expand Service
integration.
2. Select Buses.
3. Select the appropriate messaging bus for the service.
For example, for a messaging engine that is named DE1Cluster1.000-BPM.DE1,
the name of the bus would be, BPM.DE1.Bus.
4. Select Destinations.
5. Review the relevant information.  You should
look at the destinations named sca/XYZ, where XYZ is
the name of the module.
6. Select the link text for the destination that you are interested
in viewing.  This will link you to a general properties
page for the destination that you want to view.
7. From the general properties page of the destination, select
the Queue points.
8. From the Queue points page, select the link for the message
point.
9. Select the Runtime tab. From
this screen you can see the current message "depth" and the threshold.
Selecting
the Messages link lets you view the message
contents.

Ideally, use an appropriate IT monitoring tool
and set alert thresholds for these destinations.  The threshold value
would be established during the performance test phase for the application.
Messages
on a production system should never be deleted unless explicitly directed
to do so by the L3 team.