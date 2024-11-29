<!-- image -->

# Optimizing a mediation flow for team development

## Before you begin

## About this task

## Procedure

1. In the Business Integration view, right click and select File
> New > Mediation Flow.
2. Choose a module or mediation module to contain the mediation
flow.
3. Enter a name for the mediation flow.
4. Click Next
5. Select the source interfaces and target references.
6. Click Next
7. Choose the option Save the mediation flow as
multiple files. Click OK.
8 In the mediation flow editor, click the canvas and switchto the Properties view. In the Description page, you can see thatthe flow has been saved as a multiple file, and from there you canchoose to save the flow as a single file. Similarly, for flows that have been saved as single files, youcan choose to save them as multiple files.

<!-- image -->

    1. Click the link shown previously to change the mediation
flow development option. The Mediation Flow Development
Option page appears.
    2. Select Save the mediation flow as a single
file.
    3. Click Finish.
9 By default, new mediation flows are saved as single files.You can optionally change the default in the preferences page:

1. Go to Window > Preferences
2. Under Business Integration, navigate
to Mediation Flow Editor
3. Select the check box Save new mediation flow
as multiple files.

## Results

- Considerations for team development of mediation flows

When you choose to save a mediation flow in multiple files, the mediation flow is split into several files to facilitate team development. A specific file with an extension of .mfcflow is created for each source operation, and a common file with an extension of .mfc is created for the mediation flow. Depending on the type of change you make, you may need to synchronize the common file in addition to updating the changes to the operation .mfcflow file.
- Example: Team development of mediation flows

This topic provides an example scenario for a team of developers that work concurrently on the same mediation flow.