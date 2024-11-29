# Converting the target environment of projects

## Before you begin

## About this task

- Traditional: The project is designated to be installed and run on
Workflow Server in the traditional WebSphere
runtime environment.
- Traditional or Container: The project is designated to be installed and
run on either Workflow Server in the traditional
runtime environment or Workflow Server in the
container runtime environment.

When you change the target environment for a project in Process Designer, the dependent toolkit
versions and artifacts for the project are automatically validated to ensure that they are
compatible with the corresponding runtime environment. If some of the dependent toolkit versions or
artifacts are not compatible, a Target Environment Conversion tab is
displayed where you can make the modifications that are required for your project to be successfully
installed in the runtime environment. The Target Environment Conversion tab
is composed of the following two sections:

- Toolkit Dependencies : This section is only displayed in the followingconditions:
    - There are dependent toolkit versions that have a target environment that is not compatible with
the target environment selected for the associated project.
    - There are critical validation errors that will prevent the toolkit from being installed.
- Conversion Actions: This section is only displayed when there are
artifacts that are not compatible with the selected target environment.

The Conversion Actions section contains several list boxes for converting,
manually fixing, or deleting artifacts to enable the project to be installed in the runtime
environment. In the title bar of each list box, the number in parentheses to the right of the title
indicates how many artifacts need to be converted, manually fixed, or deleted. For information about
artifact support in the runtime environments, see Artifact support in traditional and container runtime environments.

## Procedure

To convert a project target environment, complete the following steps:

1. Convert all desktop Process Designer artifacts into Web
Process Designer artifacts,
such as converting business process definitions into processes and service types into service flows.
Remove any artifacts that are not supported in Web Process Designer.
2. Open your project in Process Designer.
3. Open the Process App Settings editor to the Overview
tab.
4 In the Target Environment drop-down list, select one of thefollowing target environment options:
    - Traditional
    - Traditional or Container
5. Click the Finish editing icon.
At the bottom of the editor, there is a Validation errors and warnings
icon that is used to open the "Validation errors and warnings" view, which displays all errors in
the project as an expandable tree. In the tree, the Unsupported Artifacts
category lists artifacts that are not supported in the selected target environment and in the web
Process Designer. If your project contains artifacts that
are not compatible with the selected target environment, the Target Environment
Conversion tab is displayed in the Process App Settings editor.
6. Select the Target Environment Conversion tab.
7 In the Toolkit Dependencies section, complete the followingsteps:

1. In the list box, select an incompatible toolkit version.
2. Click the Change the version of the toolkit icon. The Change
Dependency dialog box opens and lists any toolkit versions that are compatible with the target
environment.
3. In the Change Dependency dialog box, select a compatible toolkit version. If there is
no compatible toolkit version to select, complete the remaining substeps in this
step.
4. Click the Open the toolkit in Designer icon. The toolkit opens
in another browser tab and the Toolkit Settings editor is displayed.
5. Convert the toolkit to the new target environment as described in this
topic.
6. When you have finished converting the toolkit, create a new snapshot of the
toolkit.
7. Return to the browser tab that has the Process App Settings editor open and click the
Target Environment Conversion tab (if not already open).
8. In the Toolkit Dependencies list box, ensure that the
appropriate dependent toolkit is selected in the list.
9. Click the Change the version of the toolkit icon. The Change
Dependency dialog box opens.
10. In the Change Dependency dialog box, select the new toolkit version that you just
created. The incompatible toolkit version is removed from the list box because it has been replaced
with a new toolkit version that is compatible with the target environment.
8 In the UI, BPD, or Service Conversion Required list box, completethe following steps:

1. Select a UI, BPD, or Service link to open the appropriate conversion
tab.
2. Select one or more of the listed artifacts that require conversion.
3. Click Convert.
4. Select the Target Environment Conversion tab. The selected link
is removed from the list box because the associated artifacts are now compatible with the target
environment.
9 In the Manual Fixes Required list box, complete the followingsteps:

1. Hover your cursor over the link for an artifact that requires manual fixes. The hover
help provides additional information about the manual fixes that are required.
2. Select the artifact link to open the artifact in the appropriate
editor.
3. In the "Validation errors and warnings" view, click the Switch to the
current artifact view icon to restrict the displayed errors and warnings to only those
associated with the opened artifact.
4. Fix the critical errors.
5. In the upper-left corner of Process Designer, select
Process App Settings to return to the Target Environment
Conversion tab. The selected link is removed from the list box because the associated
artifact is now compatible with the target environment.
10 In the Other Conversions Required list box, complete the followingsteps:

1. Select one or more artifacts that require conversion.
2. Click Convert. The selected artifacts are removed from the list
box because they are now compatible with the target environment.
11 In the Deletions Required list box, complete the followingsteps:

1. Select one or more artifacts that require deletion.
2. Click Delete. The selected artifacts are removed from the list
box.