# Cloning projects and toolkits

In IBM® Workflow
Center, you can produce
a clone or copy of either a project or toolkit by using the Clone and
Create Copy features. These functions allow for the convenient replication of
projects or toolkits, and the efficient generation of more instances of case projects as
needed.

To clone a process application in the classic Workflow Center, use the
Clone option and complete the following steps:

1. Select the Process Apps or Toolkits tab.
2. Click the project that you want to clone.
3. Click Clone from the snapshot menu (). Workflow Center
opens the Process Apps or Toolkits tab and displays
the cloned project with COPY added to the end of the original name and the number
2 added to the end of the original acronym.
4. To change the name and acronym of the cloned project, click the application to open it, click
Manage and then edit the text in the appropriate fields.
5 To create library items in the process application or make other edits, click Open inDesigner . Cloning does not change the namespace of the cloned project. One reason tokeep the namespace the same in the cloned project is that other project might refer to thatnamespace. To change the namespace in the cloned project, you can update it from the XMLSettings section of the Process App Settings page.Tip:
    - You might receive a log exception similar to
com.lombardisoftware.expimp.jaxb.ibminterchng.DependencyManager updateExternalDependencies Service with ID TWProcess.3c4810a7-c8a4-44e6-b93f-d1ee84cb3b40 not found.
You can safely ignore this exception. The process application is still cloned successfully.
    - You might receive the following error:
CWLLG1274E: An exception occurred. com.ibm.bpm.pal.PALException: RepositoryServicesCore.cloneProcessApp.fail: Number of Objects to copy 1200 
is larger than max-cached-objects-during-refactoring 256s are checked by the server that runs the service.
To fix or avoid this error, increase the value of the
max-cached-objects-during-refactoring setting. For more information, see Increasing the maximum number of cached objects during refactoring.

1. In the details of the case solution, from the snapshot menu (), go to the overflow menu for the solution to be copied and click Create
Copy. The Create a copy of the case solution page opens.
2. Give your solution copy a name, and add an acronym and a description to it, if needed.
3. Click Create Copy. The solution copy is created with all the artifacts
and logic of the original solution.