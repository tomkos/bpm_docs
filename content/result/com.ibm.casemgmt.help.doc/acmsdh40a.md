# Adding steps that use case properties in IBM
FileNet Process Designer

## About this task

## Procedure

To map step properties to a case folder in IBM
FileNet Process Designer so that they display
properly in Case Client:

1 Open the workflow activity by using the stand-alone IBMFileNet Process Designer Restriction: Do not open a workflow in Step Designer at the same time that you open theworkflow in IBMFileNet Process Designer . Never open the PEConfiguration file or the XPDL file in another application when the solution is open inCase Builder .
    1. In IBM
FileNet Process Designer, go to
File, click Solution, then
edit
    2. In Design object store, click Browse to
browse the Root Folder, click IBM Case Manager, click
Solutions, enter the solution name, and select the
solution definition file to open the solution.
2. Select Case Type and the activity workflow that you want to add.
If your activity is not displayed, click View Workflows.
3. Add a general step and assign the step to a role, workgroup,
or participant.
4. Go to General  > Step
Processor  > case\_prefixCmAcmSTEP\_DEFAULT\_PAGE to assign the step processor.
5. In the Parameters tab, select the case parameters, and then click the Business
Objects icon in the Selected Parameters window.
F\_CaseFolder is already selected.
6. Select the case properties that you want, and then click
the arrow icon to move the properties to the Selected Parameters box.
7. In the Selected Parameters box, select all the properties that you added, and then use the
Access Rights icon in the selected fields section to change the access to
read/write.
8. Validate the workflow.

Tip: These
property changes might cause errors when you validate the workflow
in Step Designer. The errors do not prevent the solution from being
deployed.
9. Commit the changes in Case Builder to save the changes in
IBM
FileNet Process Designer.