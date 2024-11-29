<!-- image -->

# Associating a module or library with a process application
or toolkit

## Before you begin

- If you want to migrate the process instance, you must create a new process version before you
associate the module with the process application. You can create a new process version by
right-clicking your module in the Business Integration view and selecting New Process
Version.
- If you do not want to migrate the process instance, you can proceed to associate the module with
the process application by following the instructions in this topic.
- See the guidance and limitations topics listed in the Related reference links for
information on working with Workflow Center.

## Procedure

To associate a module or library with a process application
or toolkit, complete the following steps:

1. In the Business Integration view, right-click the module or
library that you want to add to your process application or toolkit. From the menu, click
Associate with Workflow Center. The Associate with a Process
Application or Toolkit window opens. 
Tip: The Associate with a Process Application or Toolkit window
also appears when you use the wizard to create new artifacts in IBM Integration Designer such as
modules, libraries, and monitor models.
2. From the Select the process application or toolkit
that will contain the projects list, select a process
application or toolkit.
3. In the Select the projects to associate pane,
you can see the projects in your workspace that are available for
association. Select the modules or libraries that you want to associate
with your selection. Click Select All  to select
all the modules or libraries that have not been associated with a
process application or toolkit. Click Select Referenced to
select modules or libraries referenced to the selected item. For example,
click Select Referenced to add a library to
the selected list if a selected module had a dependency on that library. 
Tip: You stop sharing certain file types by setting
IBM Integration Designer preferences in Windows > Preferences > Business Integration.
4. Click Finish. The process application
or toolkit is brought into the workspace and you can see the associated
modules and libraries below it in the Business Integration view.
Tip: IBM® Integration
Designer aggregates
all artifacts into one integrated process. See the Guidance topic
for more details. For information about limitations that may exist
when associating projects with process applications, see the topic
"Limitations when working with process applications and toolkits."

## What to do next