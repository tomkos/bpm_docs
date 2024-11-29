# Building a query for a search case operation (deprecated)

## About this task

Follow these steps to add a query that can be used in
a search case operation.

## Procedure

1. In the IBM Business Automation
Workflow editor,
click the Case Filters tab.
2. In the left column, select the search node you want to
create your query for, if you created more than one search service.
3 Beneath Build Case Filter completethe fields appropriate to your query.
    - Use Mapping Variable (String): Select this
check box only if you are experienced in writing Content Management
Interoperability Services (CMIS) queries and want to write your own
hand-coded query (see the query section of the CMIS specification for
information on the syntax). You can improve your response time by
qualifying your SELECT clause as follows: SELECT CmAcmCaseIdentifier,
cmis:objectId FROM ...The case type in your query takes
precedence over the case type specified in your service. If there
is a difference between the case type in your query and the case type
in your service, the case type in your query will be used.
Selection
will disable the fields in case filter and make the Input
Mapping field editable. Select the Data Mapping tab in the Properties view to see the Input Mapping field.
    - Match criteria: Lets you select all or
any as a match criteria. All returns cases matching all the criteria
specified in the case filter. Any returns cases matching any single
field in the case filter.
    - Case ID: Lets you specify a case.
    - Case State: Lets you specify the state
of a case: working, complete or failed.
    - Date added between: Lets you specify a
period of time when a case was added to the case management solution.
    - Added by: Lets you specify a userid that
added a case.
    - Date modified between: Lets you specify
a period of time when a case was modified.
    - Modified by: Lets you specify a userid
that modified a case.
    - User-specified properties: Lets you specify
custom properties found in the case type selected for the node.
4. Save your work. File > Save All.