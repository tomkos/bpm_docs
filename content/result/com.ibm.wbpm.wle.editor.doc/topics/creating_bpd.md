# Creating a business process definition (BPD) (deprecated)

## Before you begin

To perform
this task, you must be in the IBM® Process
Designer desktop
editor, which is deprecated.

Ensure
that you have access to a process application in the IBM Workflow
Center repository.

## About this task

Process modeling captures the ordered sequence of activities
within a process along with supporting information from end to end.
In process modeling, the business process is framed in a BPD to reflect
the activities, the roles that conduct those activities, conditional
branching, and the sequence of the workflow between the activities.

- When you create a BPD, use the Business Process Model and Notation
(BPMN) standards so that everyone who is involved with the process
can interpret and understand the process model. BPMN also compacts
your BPD by using symbols to represent ideas.
- Create BPDs in a process application, not in a toolkit:
    - A BPD in a toolkit can result in process instances running inside
the toolkit. A process instance running in a toolkit cannot be migrated.
    - In Workflow Center, an
exposed BPD or a service that is contained in a toolkit can be started
from the toolkit or from the process application that contains the
toolkit. But, in IBM Workflow
Server,
a BPD or a service can be started only from a process application.

A business process definition needs to include a lane
for each system or group of users who participates in a process. A
lane can be a participant lane or a system lane. However, you can
create a BPD that groups the activities of a group and a system into
a single lane if that is your preference.

You can designate
any specific person or group to be responsible for the activities
in a participant lane. Each lane that you create is assigned to the
All Users group by default. You can use this default group for running
and testing your BPD in the Inspector. The All Users group includes
all users who are members of the tw\_allusers security
group, which is a special security group that automatically includes
all users in the system.

A system lane contains activities
handled by the IBM Business Automation Workflow system.
Each activity needs an implementation, which defines the activity
and sets the properties for the task. During implementation, a developer
creates a service or writes the JavaScript necessary to complete the
activities in a system lane.

System tasks that you place in
a non-system lane are also run by the system by the first configured
system lane user.

For each BPD that you create, you need to
declare variables to capture the business data that is passed from
activity to activity in your process.

You can also add events
to a BPD. Events in Business Automation Workflow can be
triggered by a due date passing, an exception, or a message arriving.
The trigger that you want determines the type of event you choose
to implement.

## Procedure

1. Open the desktop Process Designer (deprecated).
2. Open a process application in the Designer view.
3. Click the plus sign next to Processes and
select Business Process Definition from the
list and complete the fields in the New Business Process
Definition window.
4. Design your process by dragging BPMN elements from the
palette onto the diagram area.
5. To specify the details for an element, select the element
in the diagram and edit its properties in the Properties view.

- Adding lanes to a BPD (deprecated)

 Traditional: 
A Business Process Definition (BPD) can include a lane for each system or team of users who participate in a process. A lane is the container for all the activities to be carried out by a specific team or by a system.
- Adding activities to a BPD (deprecated)

 Traditional: 
In a business process definition (BPD), you can include activities that represent logical work that a specific team or a system completes.
- Adding events to a BPD (deprecated)

 Traditional: 
When modeling a process, you might want to model events that can occur at the beginning, during, or at the end of a runtime process (as opposed to activities that are carried out by participants in the process).
- Example gateways in BPDs (deprecated)

 Traditional: 
The following samples illustrate how to model several types of gateways in BPDs.
- Modeling process execution paths in BPDs (deprecated)

 Traditional: 
Use sequence flows to connect activities and other modeling constructs to establish the process flow.
- Implementing activities in a BPD (deprecated)

 Traditional: 
Choose the implementation for each activity in your process and set the required properties.
- Implementing a BPD activity as a human service (deprecated)

 Traditional: 
If an activity in the business process definition (BPD) is to be completed by a user, you can implement the activity as a client-side human service or a heritage human service.
- Assigning teams to BPDs and lanes (deprecated)

 Traditional: 
Assign teams of users that can start activities, and teams that can work on activities in Process Portal. You can assign a team of instance owners for a BPD, or you can assign teams for individual activities and lanes.
- Assigning teams to BPD activities (deprecated)

 Traditional: 
For any activity with a service implementation, you can designate the users who receive the runtime task by using the Assignments page in the properties for that activity.
- Creating UI for a BPD process instance (deprecated)

 Traditional: 
Create customized user interfaces that a user sees for the process instance in Process Portal.
- Testing and debugging BPDs and services (deprecated)

 Traditional: