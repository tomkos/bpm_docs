# Adding activities with workflow processes

In the workflow environment, there are several key features that enable the tight integration
between cases and business processes. These features include:

- Data objects
- Roles and teams
- Activities implemented with processes

The data objects enable process instances to interact with case and activity properties. These
data objects are described in the topic Data objects and its subtopics.

Roles in Case Builder are
mapped to teams in the designer, which enables the Case Client to display both case steps and
process tasks in a unified role in-basket. The relationship between roles and teams is described in
the topic Roles and teams.

Activities can be implemented with either new or existing processes. New processes have access to
case and activity properties, but existing processes can only be passed case and activity properties
as input. Information about creating activities with new or existing processes is found in the
topics Adding an activity with a new process and Adding an activity with an existing process.

- Adding an activity with a new process

You can add a case activity and implement it with a new process that is created locally in the same case solution as the activity. You can manage and deploy your process and case solution together.
- Adding an activity with an existing process

You can create a new activity for a case type and implement the activity with an existing workflow process. The existing process and the activity reside in different projects, and the process has no access to the case properties (although the properties can still be passed as input).
- Working with variables for content objects

Data objects that are defined in a case solution are also available in the designer, where you can use them to implement case activities that use a process and build user interfaces. The data objects include content objects that represent the set of properties that are associated with a case and activity.
- Interacting with a parent case from a process

In workflow processes that implement case activities, you can interact with case operations through the new operations that have been added to the TWProcessInstance JavaScript API.
- Troubleshooting case and process integration

Troubleshoot typical errors that might surface when you integrate cases with processes.