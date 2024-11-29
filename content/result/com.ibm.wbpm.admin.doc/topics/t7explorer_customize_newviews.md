<!-- image -->

# Creating customized views for Business Process Choreographer
Explorer or Business Process Archive Explorer

## About this task

If you have one of the system administrator roles, you
can create customized views for a client instance. To create customized
views for this instance, complete the following steps.

## Procedure

1. Click Manage Views in the taskbar.
2. In the Manage Views page, expand the Define
Customized Views section, and select the type of view
that you want to create.
3. In the Search For ... And Define Customized Views page,
where ... is the type of view, for example Process Templates, select
a query table for your view. A default query table is
set for your view definition. You can either select a different query
table, or choose not to use query tables in your view definition. Note: If
you use a query table, you cannot specify additional search criteria
here for the view. All the search criteria must be defined in the
query table definition.

If you are not using a query
table, specify search criteria. Use the Process Criteria tab,
the Task Criteria tab, and the Property
Filters tab to limit the search results, for example, to
a specific process template. When defining instance views, you can
also use the User Roles tab to limit the search
results to users, groups, or roles.
4. If you are using query tables and the query table definition
has parameters, specify the query parameters that are needed on the Query
Properties tab.  The parameter names that
you specify must match the names in the query table definition. You
can also provide default values for the parameters, and specify whether
a default value can be overwritten when the query for the view is
run.
5 In the View Properties tab, selectthe list columns, list properties, such as ordering properties andthe results threshold, and action bar actions to include in the view. If this is a task, process, or activity instance view, youcan use the View Settings pane to specify whichitems are shown to users in the system administrators and system monitorsrole.
    - To show all items that match the search criteria in the view,
select All Instances.
    - To show only the items that the logged-on user is assigned for
a specific role, select Personal Instances.
6. Enter a display name for the view in the View
Name field, and click Check and Save.
The search is run to check for errors. If it runs without
errors, the view is saved. Use the Summary tab to check the settings
that are currently set for the view.
If you are using a
query table and you have specified query parameters that can be overwritten,
the Specify Query Parameters page for the new
view is displayed after you click Check and Save.
Enter a value for each of the query parameters, and click Check
and Save again.

## Results

The new view appears in your navigation pane. Your users
see this view the next time that they log in to the instance of the
client that you added the view to. Do not prompt for the parameter
values when using the view

- Creating customized views in Business Process Choreographer Explorer or Business Process Archive Explorer for process templates for state machines

Although a predefined view is provided for the process templates for state machines, you might want to define your own views for this type of template.
- Creating customized views in Business Process Choreographer Explorer or Business Process Archive Explorer for process instances for state machines

Although a predefined view is provided for the process instances for state machines, you might want to define your own views for this type of process instance.

<!-- image -->