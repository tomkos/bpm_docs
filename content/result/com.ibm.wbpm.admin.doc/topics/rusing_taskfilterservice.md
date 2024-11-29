# Prioritizing work

The task filter service allows you to gain programmatic control over the saved search result set
and to do your own sorting and filtering of the task list. When the task filter service is enabled,
the default template service flow uses the prioritization function to sort the task list. For more
information about Intelligent Task Prioritization, see Installing, configuring, and administering Machine Learning Server.

| Custom property                  | Mashup equivalent                                   | Description                                                                                                                                          |
|----------------------------------|-----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| task-filter-service- name        | com.ibm.bpm.portal. task.filter.service. name       | The name of the task filter service, specified as a string with the <project-acronym>@<service-name> format. For example, SYSRP@Task Filter Service. |
| task-filter-service- always-run  | com.ibm.bpm.portal. task.filter.service. alwaysRun  | Specifies whether the task filter service is called after every saved search execution (Boolean).                                                    |
| task-filter-service- show-toggle | com.ibm.bpm.portal. task.filter.service. showToggle | Specifies whether the task filter service toggle is displayed to the user (Boolean).                                                                 |

- If task-filter-server-always-run is used,
task-filter-service-show-toggle is ignored and the toggle is not displayed to
the user.
- The service that is used must meet the following requirements:
    - It is a service flow with AJAX options that is configured to allow all callers to call the
service.
    - The input is a string that can accept the JSON payload received from the saved search
execution.
    - The output is a list of business objects of type Task Identifier . The listorder determines the order of the tasks in the task list. The Task identifier consists of the following properties:
        - systemID: This property may or may not be present in the input string.
Consequently, it needs to be passed in the output to correctly identify the task.
        - TKIID: This property is present in the input string under two possible
names, TKIID or "TASK.TKIID". Either one of these values must be
used to populate the output business object.
        - PI\_PIID: This property is present in the input string under two possible
names, PI\_PIID or "PROCESS\_INSTANCE.PIID". Either one of these
values must be used to populate the output business object.
- In the SYSRPC project, an out-of-the-box template service flow named Task Filter
Service Template is available for you to use.
- If task-filter-service-show-toggle is used and
task-filter-server-always-run is not set, your choice of running the filter
service is stored in the user preferences and will be persisted across login sessions.