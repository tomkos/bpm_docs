# Setting up a team filter service

## Before you begin

The following procedure describes how to set up a team filter service that is implemented as a
service flow. To complete the procedure, you must be in Process Designer.

To set up a team filter service that is implemented as a heritage
integration service, you must create the integration service in the Process Designer desktop editor. See
Building an Integration service.

## About this task

- Group membership for a task's team that is assigned using a team filter service is fixed at the
time of task creation and cannot be changed.
- A task's manager team that is assigned using a team filter service is bound to the snapshot
associated with the task at the time of task creation. The team membership can change depending on
the values for that snapshot.
- Process instance and task migration will not migrate teams or manager teams to a new snapshot
context when a team filter service is used. The manager team of the task will always point to the
original snapshot where the task was created regardless of the current snapshot context for the
task.
- The teams associated with a task that uses a team filter service will block snapshot deletion
for the snapshot where the task was created. Snapshots can only be deleted after the tasks for these
teams are deleted.

## Procedure

1. Open the appropriate process application in the Designer
view.
2 In the library, click the plus sign (+) next to Services andcreate a service flow. Complete the wizard to configure the serviceflow as a team filter service:
    - Enter a suitable name for the service flow, for example, High
Value Claims Team Filter or Separation
of duties - filter out previous user.
    - Select Use as a team service. Additional
setup options are displayed. From the Service type list,
select Team filter. The default template for
the team filter service is Team Filter Service Template.
    - Click Finish.
3. Select the Variables tab. The mandatory input and output variables are already present and locked. If the new team
filter service requires information from the activity, click the plus sign next to
Input to add more input parameters. In the Details
section, specify the name of the variable, its type, and any default value. Limitation: Updating shared business objects in a team filter service or team retrieval
service is not supported when the same shared business object is updated within the same execution
unit in the process beforehand. Shared business objects can either be saved explicitly or
automatically by enabling "Automatically sync shared business objects" in the team retrieval service
or team filter service. In general, consider the team retrieval service or the team filter service
conceptually as read-only service flows.
Tip: The input variables that are required depend on the policy that the filter must
implement. If, for example, certain users cannot work on tasks that are above a certain value, the
service flow might need the process variable tw.local.estimatedClaimAmount as an
input parameter that the service flow implementation uses to determine which users to eliminate from
the input team. Similarly, for example, to implement a separation of duties policy, where the user
who completed the previous activity cannot be assigned to the following one, you might specify an
input variable previousUser that you map to the process variable
tw.system.user.id so that the service flow implementation can remove the previous
user from the input team.
4. Click the Diagram tab and provide
the implementation of the service flow. Based on the input parameters,
the service flow must return a Team object that contains
a list of team members. It can also optionally include the name of
a team of managers, and optionally the name of the team (this parameter
is ignored).
5 If you want the results of the service flow to be cached foreach combination of input variables, select the Overview tab,then in the Results Cache section, select Enablecaching of service flow results to display the cache configurationfields. By default, caching is disabled.

- When caching is disabled, the results caching section is not displayed.
- When caching is enabled, the results caching section is displayed. By default, the cached
results for each combination of input parameter values are stored for 12 hours. To change the
caching period, use the Days, Hours,
Minutes, and Seconds fields to select the duration
that you want.Important: Depending on the size of the results, you
might need to tune the size of the service flow results cache to avoid memory problems. By default,
the cache stores up to 4096 results. You can change the size of the cache by setting a different
value for <service-result-cache-size> in the
100Custom.xml file, inside the <server
merge="mergeChildren"> section. 
Limitation: The
results cache setting works only for top-level services or service flows. When a service flow is
called by another service flow, the results for the linked service flow are not cached.
6. Click Save or Finish Editing.

## Results

## What to do next