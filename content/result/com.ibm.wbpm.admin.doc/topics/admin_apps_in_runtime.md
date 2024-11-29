# Administering applications and processes in the runtime environment

The tools you use depend on the type of administration task that you are doing. These topics
include information on using commands, Process Admin Console, Workflow Center, WebSphere® Application
Server administrative console,
Business Process Choreographer Explorer, Process Inspector, and business rules manager.

- Managing persisted data

Whenever data is persisted into a database, a time comes when its important to delete or archive some of that data. Periodically cleaning up saves disk space and improves performance.
- Cleaning up shared business objects

 Traditional: 
When a new version of a shared business object is saved, older versions of the shared business object that are no longer required are automatically deleted. The system performs the cleanup based on the cleanupMaxVersionCount and cleanupMinAge configuration parameters. To specify the versions of the business objects that you want to keep, use wsadmin scripting to modify these configuration parameters. If you migrated your Business Automation Workflow from a version earlier than version 8.5.6, you must change cleanupMaxVersionCount to explicitly enable cleanup.
- Managing installed snapshots

Use the Process Admin Console to administer and configure runtime settings for snapshots installed on a workflow server.
- Administering service applications and service modules

Use the administrative tools to view and manage service applications and their associated service modules.
- Administering IBM Business Automation Workflow tasks

IBM® Business Automation Workflow tasks integrate with BPEL processes through a web service. After you deploy the web service module for a case management task to a production server, you use the Workflow Server administrative console to make changes to the module properties.
- Administering processes with Process Inspector

Use Process Inspector to view and manage process instances for process applications that are running on a specific workflow server. You can use Process Inspector to troubleshoot process instances that have problems.
- Administering BPEL processes and human tasks

BPEL processes and human tasks are deployed as part of an application. You can use the administrative console or the administrative commands to administer process templates and task templates. Use Business Process Choreographer Explorer to work with process instances and task instances and to report on BPEL processes and human tasks.
- Administering business state machines

You can view the correlation set values and display states variables to debug and administer business state machine instances.
- Administering business rules and selectors

Business rules and selectors provide flexibility in a business process by changing the results of a process based on a criteria. Before installing applications that contain business rules and selector components, you must install the business rules dynamic repository. You can install the business rules dynamic repository for a stand-alone server or for network deployment.
- Managing relationships

A relationship correlates at least two or more semantically equivalent business objects, which are represented in different physical formats. The relationship service maintains relationships and roles in the system, and the relationship manager provides a way to configure, query, view, and perform operations on relationship runtime data, including roles.
- Monitoring the number of process instances and tasks

You can create alert definitions to generate alerts when certain conditions apply such as the number of process instances or tasks goes beyond a threshold. The resulting alerts can be displayed or sent to administrators so that they can investigate and take action.