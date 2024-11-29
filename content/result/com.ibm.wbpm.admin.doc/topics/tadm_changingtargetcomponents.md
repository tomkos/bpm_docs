# Changing
import targets

## Before you begin

- Make sure the new target uses the same data object type
- Know
whether the module is synchronously or asynchronously invoking
the target
- Know whether the reference targets a single or
multiple services

## About this task

## Procedure

1 Stop the module that contains the reference that you arechanging.
    1. Using the administrative console,
display the Service
Component Architecture (SCA) modules. Navigate to this
panel using Applications > SCA Modules
    2. Select your module and press Stop.
The display updates to show the application as stopped.
2 Change the target destinationof the reference. Howyou make the change depends on how the module invokes the target. Type of invocation How to change Singletarget service Multiple target services

How
you make the change depends on how the module invokes the target.

| Type of invocation       | How to change                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Single target service    | Using the administrative console, display the SCA Modules. Navigate to the panel using Applications > SCA Modules. From the displayed list, select the module that contains the import that references the target to change. Expand the list of imports by clicking the plus sign (+) next to Imports. Select the import to change from the list. In the Target area, select the Module from the list. After the Export list refreshes, select the export for the new target. Save the change by clicking OK.                                                                                                                                                                       |
| Multiple target services | Display the buses on the system on which the module resides. Navigate to the panel using Service Integration > Buses. Select the SCA.System.cellname.Bus Display the destination targets for the bus by clicking Destinations. Select the destination that represents the import that connects the calling module to the targets. This identifier will contain the word import. Display the list of properties by clicking Context properties. Select the property to change by clicking on the targets property in the list. Change the Context value field to the new destination targets. Return to the Context properties panel by clicking OK. Save the change by clicking OK. |

3. Save your changes. Click Save when
prompted.

## What to do next