# Enhancing case solutions that use  
FileNet

processes

## About this task

- In the Manage Solutions page, click More actions > Open Process Designer from the solution that you want to edit. By opening IBM
FileNet Process Designer from here, you can select the case type and update
the activity process maps or add non-activity maps, roles, in-baskets, and other items. In addition,
you can open different case types without closing IBM
FileNet Process Designer.
- In the Activities page, click the Open
Process Designer icon for the activity that you want to edit.
If you open IBM
FileNet Process Designer from
here you can edit the workflow for that actiity and other activities in the
case type. However you cannot view configuration, roles, or in-baskets.

- Specifying credentials for a web service

By default, the FileNet P8 Component Manager service user credentials are used for authentication with a web service on IBM Business Automation Workflow. However, you can use the Component Manager in Process Task Manager to configure different credentials for the web service.
- Primary queue

To support multiple in-baskets for one role that might not be from the same role-based queue, you can use primary queues. In the Case Builder Step Designer a nonsystem step in a task process map is assigned to a queue or a workgroup, not a role. When you add a step on a role swimlane, an attribute for the role indicates the primary queue that the step will be assigned to. For each role, there is only one primary queue.
- Creating more than one in-basket in IBM FileNet Process Designer

IBM Business Automation Workflow supports roles with multiple in-baskets enabling different views in Case Client. You can define more in-baskets and associate more in-baskets to a role in IBM FileNet Process Designer.
- Assigning a primary queue to more than one role

When you define a role, Case Builder defines the CB\_PrimaryQueue attribute for the role with value of <solution prefix>\_<normalized version of role name>. You can assign the same primary queue to more than one role by setting the same CB\_PrimaryQueue attribute on each role in IBM FileNet Process Designer so that those roles share the queue.
- Disassociating a role’s primary queue

If you have a role that is not completing the work, you can disassociate the role’s primary queue in IBM FileNet Process Designer so that the role is not an option as a swimlane in the Step Designer and no work can be assigned to that role.
- Defining a custom role

You can create a custom role, queue, and in-basket in IBM FileNet Process Designer. If you want to use the role in the Step Designer, you must add the CB\_PrimaryQueue attribute for the role to indicate the primary queue for the role.
- Changing primary queue definitions after upgrade

When you upgrade a solution from a previous version of IBM Business Automation Workflow, Case Builder creates the primary queue value for the role by searching for the queue of the first in-basket with the CB\_Inbasket attribute in the in-basket list that is associated to that role. The upgrade process might assign the same primary queue for different roles depending on the order of the in-baskets in the in-basket list and their CB\_Inbasket attributes. If you want each role to have a unique primary queue, you must update the CB\_PrimaryQueue attribute in IBM FileNet Process Designer.
- Adding case operations to a FileNet process

You can use case operations to automate specific steps in an activity that has a  FileNet  process. For example, you can use case operations to create an insurance claim case when an accident report is received or to start a discretionary activity based on the value of a document property.