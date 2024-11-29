# Administering the Process Portal index

Indexing on
an Business Automation Workflow system is
enabled by default. Process instances and tasks are indexed according to a time interval that you
can specify. To change the indexing behavior, you must edit the 100Custom.xml
configuration file. If a problem occurs with the index, commands are available for updating and
rebuilding it.

- A task is assigned.
- A task is completed and the business data is updated.
- The due date or at-risk date of a task is changed.
- The priority of a task is changed.

- An instance is started, completed, suspended, resumed, terminated, or restarted.
- An instance failed.
- The due date or at-risk date of an instance is changed.

For example, business data for a process instance that exists when a task and its corresponding
process instance activity are completed gets indexed with both the task and instance. Process
participants can find the task or instance by searching the instance business data. If a task form
consists of several coach views but only one coach view is complete, the updates from this coach
view are not searchable until all the coach views in the task form are complete.

By default, the previous tasks in a process instance are not re-indexed when later tasks are
completed and the business data for the process instance is updated. If you want the updated
business data to be searchable from previously completed tasks, change the value of the
<task-index-update-completed-tasks> configuration setting to
true in the 100Custom.xml file. If the process instance has a
lot of previous tasks, re-indexing these tasks might degrade the system performance.

To make particular business data searchable in Process Portal, use Process Designer to make the
appropriate process instance variable visible in Process Portal and to set the alias
name that is used to search for the business data.

- If you are still using Process Portal, disabling the
Process Portal search index
will remove the full text search input field and the Process Portal dashboards. Instead of
using Process Portal,
consider using Workplace
along with the enabled federated data repository BPD indexing, and then disable the Process Portal search index without
degrading the user experience.
- If you are still using the /rest/bpm/wle/v1/tasks REST API, disabling the
Process Portal search index
will remove the full text search support with this API. Instead of using the
/rest/bpm/wle/v1/tasks REST API, switch to the advanced search API that is exposed on
/rest/bpm/wle/v2, which offers a richer set of search capabilities, and then
disable the Process Portal
search index and enable the federated data repository BPD indexing to improve the overall
performance and benefit from a richer search REST API.

- Updating the Process Portal index

If a problem occurs with the Process Portal index, you might need to run a command to rebuild it. You can also update the index for an instance or task, remove an instance or task from the index, or clean up the index tables.
- Configuring the Process Portal index

You can change where the index on an Business Automation Workflow system is stored by modifying an environment variable. To change the index behavior, such as the length of the update interval or including completed tasks in the index, you must edit the 100Custom.xml configuration file.
- Process Portal index: Default indexed fields

The Process Portal index on an Business Automation Workflow system contains fields for tasks and processes that are indexed by default. These indexed fields are available in Process Portal as field names that can be used in search filters. Your index will also include business data that was made available for searching when the process was modeled.