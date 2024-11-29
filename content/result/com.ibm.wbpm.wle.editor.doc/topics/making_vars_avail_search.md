# Making business data available in searches and views

## About this task

- By default, you use a workflow server without IBM Process Federation
Server. In this case,
all modeled business data fields of process applications that are deployed to the workflow server are detected,
even if no instance of the process application is running.
- If you use Process Federation Server as a back end
server, business data fields are detected if two conditions are met: a task is created for an
instance of the process application and the business data fields of the instance have nonnull values.

## Procedure

1. Open a process that includes the variables you want to configure and go to the
Variables tab.
2. For each variable whose runtime values you want to search or to make viewable in the task list,
select the Expose in work environments checkbox in the
Details section. For complex variables, be sure to select the checkbox for
each parameter you want to make available.

Note: Only process-level variables can be made available as business data for searches, but not
variables that are defined, for example, inside human services.
3. In the Alias text box, type a name for the variable. This is the
name to use when you perform searches.
This is also the name that users see when they view the data that is related to tasks in their
task list. If you use a mix of uppercase and lowercase letters to indicate word boundaries, the
label for the variable is parsed into a multi-word string. For example, if your search alias is
customerName, the label for the variable is Customer Name.
Note: The search alias must be unique to the variable type throughout the workflow server on which
the process runs. If a variable is shared by multiple processes (for example, a parent process and
its linked processes) and you want the variable to be searchable in all of those processes, you must
define the same search alias for the variable in each of the processes where it is used. However,
defining same search aliases in multiple processes (for example, a parent process and its linked
processes) is not recommended. That is because there can be only one alias value for the process
instance. If you update the alias value both from parent process and the linked processes, the alias
value may be confusing. The search result may not be what you expected.
4. Click Save or Finish Editing.

## Results

## What to do next

If you are a business user and own a saved search, you can select which columns to display in the
search results.

1. In Process Portal, in
the saved search area, click Edit Columns. In the Available
Columns window, each business data object is marked with an asterisk.
2. Select a column label and type in the Display name field.