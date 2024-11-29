# Defining ad hoc actions (deprecated)

While a process is running, a user might need to launch a new activity or set of
activities, such as updating a customer's contact information or canceling the process instance. The
designer can define a set of these unplanned, or ad hoc, actions to be launched by the
user fromProcess Portal.

## Before you begin

To perform
this task, you must be in the IBM® Process
Designer desktop
editor, which is deprecated.

To
use ad-hoc tasks, Process Portal users
must be members of a security group that is configured for the ACTION\_INJECT\_TOKEN
policy.  For information about security groups, see Setting up users, groups, and teams. For information about the ACTION\_INJECT\_TOKEN
configuration, see Configuration properties for action policies.
For information about managing the security groups, see Creating and managing groups.

## Procedure

To model a new activity or set of activities that a user
can launch in the normal process flow, complete the following steps:

1. Open the desktop Process Designer (deprecated).
2. Open the BPD in the Designer view.
3. Add an ad hoc start event to your process diagram by dragging
a start event from the palette and specifying an implementation type
of Adhoc in the Implementation tab of the Properties
view.
4. Add the activity or set of activities that occur when the
start event is triggered. For example, if you are designing a process
application where business users can look up a customer order history
at any time in the normal processing of a customer order, you might
include a set of tasks for logging into the order history database
and submitting a query.
5. Connect the task or tasks to the new start event. 
When you deploy your process application to Process Portal, business
users can launch the set of activities from the current application.
New task instances are created and appear in the task list for the
user or team that is assigned to the new ad hoc task.Important: Ad hoc task instances that were created during the
running of a process instance must be complete before the process
instance completes.
6 Optional: Ad hoc actions might be associatedonly with a particular phase of the process. For example, an ordercan be canceled before it has been sent out for delivery, but afterit has been delivered, the order can no longer be canceled. To makean action available for only a certain phase of the process, completethe following steps: In Process Portal , thead hoc action is available only while the running process instanceis in the specified phase.
    1. Add phases to your BPD to define the different phases
in the running process. For example, you might have a pre-delivery
phase that contains all the customer order activities that occur before
the order ship, and a post-delivery phase that contains the activities
that occur after the order ships.
    2. Move the ad hoc start event to the phase in which it
should be available.
    3. In the Event Visibility section, to restrict the visibility
of the event by phase, select phase.
7 Optional: Limit the type of users that runad hoc actions in your process. For example, you might want to limita credit check override action to users who belong to the managersteam. To make an action available to only a certain team of users,complete the following steps:

1. Add swimlanes to your BPD diagram and associate each
swimlane with a specific team. For example, you might have a swimlane
for customer service representatives and a swimlane for managers.
2. Move the ad hoc start event to the swimlane that is
associated with the team that should be able to launch the action
in Process Portal.
3. In the Event Visibility section, to restrict the visibility
of the event by swimlane select swimlane.
8. Click Save or Finish Editing.

## Results